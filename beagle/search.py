#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

import fnmatch
import logging

from cliff import columns
from cliff import lister

from beagle import hound
from beagle import openstack


class MultiLineText(columns.FormattableColumn):

    def human_readable(self):
        return '\n'.join(self._value)


class Search(lister.Lister):
    """Search for a pattern and show the results.

    """

    log = logging.getLogger(__name__)

    # Set the command so that when we run through
    # python-openstackclient we do not require authentication.
    auth_required = False

    def get_parser(self, prog_name):
        parser = super().get_parser(prog_name)
        parser.add_argument(
            '--ignore-comments',
            default=False,
            action='store_true',
            help='ignore comment lines',
        )
        parser.add_argument(
            '--comment-marker',
            default='#',
            help='start of a comment line',
        )
        parser.add_argument(
            '--file', '--file-pattern',
            dest='file_pattern',
            help='file name pattern',
        )
        parser.add_argument(
            '--ignore-case',
            default=False,
            action='store_true',
            help='ignore case in search string',
        )
        parser.add_argument(
            '--repo',
            dest='repos',
            default=[],
            action='append',
            help='limit search to named repositories (option can be repeated)',
        )
        parser.add_argument(
            '--repo-pattern',
            dest='repo_pattern',
            default='',
            help=('glob pattern to match repository names '
                  '(filtered on client side)'),
        )
        parser.add_argument(
            '--context-lines',
            default=0,
            type=int,
            help='number of context lines',
        )
        parser.add_argument(
            'query',
            help='the text pattern',
        )
        return parser

    def _flatten_results(self, results, parsed_args):
        interesting_repos = results.items()
        if parsed_args.repo_pattern:
            def check_repo(repo):
                return fnmatch.fnmatch(repo[0], parsed_args.repo_pattern)
            interesting_repos = filter(check_repo, results.items())

        for repo, repo_matches in sorted(interesting_repos):
            for repo_match in repo_matches['Matches']:
                for file_match in repo_match['Matches']:
                    if (parsed_args.ignore_comments and
                        file_match['Line'].lstrip().startswith(
                            parsed_args.comment_marker)):
                        continue
                    if parsed_args.context_lines:
                        yield (repo,
                               repo_match['Filename'],
                               file_match['LineNumber'],
                               file_match['Line'].strip(),
                               MultiLineText(file_match['Before']),
                               MultiLineText(file_match['After']))
                    else:
                        yield (repo,
                               repo_match['Filename'],
                               file_match['LineNumber'],
                               file_match['Line'].strip())

    def take_action(self, parsed_args):
        if parsed_args.repos:
            repos = ','.join(n.strip() for n in parsed_args.repos)
        else:
            repos = '*'

        try:
            server_url = self.app.options.server_url
        except AttributeError:
            # running via the openstack CLI
            server_url = openstack.DEFAULT_URL

        results = hound.query(
            server_url=server_url,
            q=parsed_args.query,
            files=parsed_args.file_pattern,
            ignore_case=parsed_args.ignore_case,
            repos=repos,
            context_lines=parsed_args.context_lines,
        )
        columns = ('Repository', 'Filename', 'Line', 'Text')
        if parsed_args.context_lines:
            columns = columns + ('Before', 'After')
        return (
            columns,
            self._flatten_results(results, parsed_args),
        )
