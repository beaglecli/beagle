# All Rights Reserved.
#
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

"""Query a hound server

"""

import requests


def query(server_url, q, repos='*', ignore_case=False, context_lines=0, files=None):
    params = {
        'repos': repos,  # which repositories to search
        'i': 'yes' if ignore_case else 'nope',
        'ctx': context_lines,
    }
    if files:
        params['files'] = files
    params['q'] = q

    headers = {
        'Content-Type': 'application/json',
    }
    url = server_url.rstrip('/') + '/api/v1/search'
    response = requests.get(url, params=params, headers=headers)
    return response.json()['Results']


def get_dependency_listings(package_name):
    return _query(
        q=package_name,
        # NOTE(dhellmann): Including setup.cfg shows *lots* of results
        # for oslo.config because of the plugins for the config
        # generator. It would be nice to figure out how to filter
        # those.
        files='(.*requirements.txt|.*constraint.*.txt)',
    )


def show_dependency_listings(package_name, official_repos):
    to_show = set(
        r.partition('/')[-1]
        for r in official_repos
    )
    results = get_dependency_listings(package_name)
    for repo, repo_matches in sorted(results.items()):
        if repo not in to_show:
            continue
        for repo_match in repo_matches['Matches']:
            for file_match in repo_match['Matches']:
                if file_match['Line'].lstrip().startswith('#'):
                    # ignore comments
                    continue
                print('{repo:30}:{filename:30}:{linenum:3}: {line}'.format(
                    repo=repo,
                    filename=repo_match['Filename'],
                    linenum=file_match['LineNumber'],
                    line=file_match['Line'],
                    ))
