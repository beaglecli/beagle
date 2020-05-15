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

from cliff.formatters import base

from beagle import grep_formatter


DEFAULT_URL = 'http://codesearch.openstack.org'


class OSLinkFormatter(base.ListFormatter):
    "OpenStack cgit link formatter"

    def add_argument_group(self, parser):
        pass

    def emit_list(self, column_names, data, stdout, parsed_args):
        fmt = '{base_url}/{repo}'.format(
            base_url='https://opendev.org',
            repo='{Repository}/src/branch/master/{Filename}#n{Line} : '
                 '{Text}\n'
        )

        for row in data:
            row_d = {
                c: r
                for c, r in zip(column_names, row)
            }

            if parsed_args.context_lines:
                before = row_d['Before'].machine_readable()
                grep_formatter.write_lines_with_offset(
                    fmt,
                    row_d,
                    before,
                    -1 * len(before),
                    stdout,
                )

            stdout.write(fmt.format(**row_d))

            if parsed_args.context_lines:
                grep_formatter.write_lines_with_offset(
                    fmt,
                    row_d,
                    row_d['After'].machine_readable(),
                    1,
                    stdout,
                )
