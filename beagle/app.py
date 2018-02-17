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

import logging
import sys

import pkg_resources

from cliff.app import App
from cliff.commandmanager import CommandManager

from beagle import openstack


class Beagle(App):

    log = logging.getLogger(__name__)

    def __init__(self):
        dist = pkg_resources.get_distribution('beagle')
        super(Beagle, self).__init__(
            description='Hound command line',
            version=dist.version,
            command_manager=CommandManager('beagle.cli'),
        )

    def build_option_parser(self, description, version,
                            argparse_kwargs=None):
        parser = super(Beagle, self).build_option_parser(
            description,
            version,
            argparse_kwargs,
        )
        parser.add_argument(
            '--server-url', '-s',
            dest='server_url',
            help='the server URL',
            default=openstack.DEFAULT_URL,
        )
        return parser

    def initialize_app(self, argv):
        pass


def main(argv=sys.argv[1:]):
    myapp = Beagle()
    return myapp.run(argv)


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
