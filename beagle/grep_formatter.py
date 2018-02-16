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

"""Format output like grep

"""

from cliff.formatters import base


def write_lines_with_offset(fmt, row_d, lines, offset_start, stdout):
    for offset, text in enumerate(lines, offset_start):
        d = {}
        d.update(row_d)
        d['Text'] = text
        d['Line'] += offset
        stdout.write(fmt.format(**d))


class GrepFormatter(base.ListFormatter):

    def add_argument_group(self, parser):
        pass

    def emit_list(self, column_names, data, stdout, parsed_args):
        fmt = ':'.join(
            '{' + c + '}'
            for c in column_names
            if c not in ('Before', 'After')
        ) + '\n'

        for row in data:
            row_d = {
                c: r
                for c, r in zip(column_names, row)
            }

            if parsed_args.context_lines:
                before = row_d['Before'].machine_readable()
                write_lines_with_offset(
                    fmt,
                    row_d,
                    before,
                    -1 * len(before),
                    stdout,
                )

            stdout.write(fmt.format(**row_d))

            if parsed_args.context_lines:
                write_lines_with_offset(
                    fmt,
                    row_d,
                    row_d['After'].machine_readable(),
                    1,
                    stdout,
                )
