===========
Users guide
===========

Examples
========

To find requirements or constraints specifications for ``cliff``:

.. code-block:: console

   $ beagle search --file '(.*requirement.*|.*constraint.*|setup.cfg|tox.ini)' 'cliff[><=]'

   +-----------------------+------------------------------------------------------------+------+------------------------------------+
   | Repository            | Filename                                                   | Line | Text                               |
   +-----------------------+------------------------------------------------------------+------+------------------------------------+
   | group-based-policy    | test-requirements.txt                                      |   20 | cliff>=2.3.0 # Apache-2.0          |
   | kolla-kubernetes      | requirements.txt                                           |    6 | cliff>=2.8.0 # Apache-2.0          |
   | networking-bigswitch  | test-requirements.txt                                      |    8 | cliff>=1.7.0  # Apache-2.0         |
   | networking-brocade    | test-requirements.txt                                      |    6 | cliff>=1.14.0  # Apache-2.0        |
   | networking-mlnx       | test-requirements.txt                                      |    6 | cliff>=1.15.0 # Apache-2.0         |
   | networking-plumgrid   | test-requirements.txt                                      |    3 | cliff>=2.2.0 # Apache-2.0          |
   | osops-tools-contrib   | ansible_requirements.txt                                   |    5 | cliff==2.2.0                       |
   | paunch                | requirements.txt                                           |    7 | cliff>=2.6.0  # Apache-2.0         |
   | rally                 | upper-constraints.txt                                      |   68 | cliff===2.11.0                     |
   | requirements          | global-requirements.txt                                    |   21 | cliff>=2.8.0,!=2.9.0  # Apache-2.0 |
   | requirements          | openstack_requirements/tests/files/gr-base.txt             |    9 | cliff>=1.4                         |
   | requirements          | openstack_requirements/tests/files/upper-constraints.txt   |  192 | cliff===2.4.0                      |
   | requirements          | upper-constraints.txt                                      |  216 | cliff===2.11.0                     |
   | rpm-packaging         | requirements.txt                                           |   21 | cliff>=2.8.0,!=2.9.0  # Apache-2.0 |
   +-----------------------+------------------------------------------------------------+------+------------------------------------+

To show the 5 lines before and after the location of the class
definition for ``ConfigOpts`` in ``oslo.config`` using the ``grep``
output formatter.

.. code-block:: console

   $ beagle search -f grep --context-lines 5 --repo oslo.config 'class ConfigOpts'
   oslo.config:oslo_config/cfg.py:135:--------------------
   oslo.config:oslo_config/cfg.py:136:
   oslo.config:oslo_config/cfg.py:137:The config manager has two CLI options defined by default, --config-file
   oslo.config:oslo_config/cfg.py:138:and --config-dir::
   oslo.config:oslo_config/cfg.py:139:
   oslo.config:oslo_config/cfg.py:140:class ConfigOpts(object):
   oslo.config:oslo_config/cfg.py:141:
   oslo.config:oslo_config/cfg.py:142:        def __call__(self, ...):
   oslo.config:oslo_config/cfg.py:143:
   oslo.config:oslo_config/cfg.py:144:            opts = [
   oslo.config:oslo_config/cfg.py:145:                MultiStrOpt('config-file',
   oslo.config:oslo_config/cfg.py:2332:    def print_usage(self, file=None):
   oslo.config:oslo_config/cfg.py:2333:        self.initialize_parser_arguments()
   oslo.config:oslo_config/cfg.py:2334:        super(_CachedArgumentParser, self).print_usage(file)
   oslo.config:oslo_config/cfg.py:2335:
   oslo.config:oslo_config/cfg.py:2336:
   oslo.config:oslo_config/cfg.py:2337:class ConfigOpts(collections.Mapping):
   oslo.config:oslo_config/cfg.py:2338:
   oslo.config:oslo_config/cfg.py:2339:    """Config options which may be set on the command line or in config files.
   oslo.config:oslo_config/cfg.py:2340:
   oslo.config:oslo_config/cfg.py:2341:    ConfigOpts is a configuration option manager with APIs for registering
   oslo.config:oslo_config/cfg.py:2342:    option schemas, grouping options, parsing option values and retrieving

To produce links to the source on the OpenStack git server, use the
``link`` formatter:

.. code-block:: console

   $ beagle --debug search -f link --repo oslo.config 'clasOpts'figO
   http://git.openstack.org/cgit/openstack/oslo.config/tree/oslo_config/cfg.py#n140 : class ConfigOpts(object):
   http://git.openstack.org/cgit/openstack/oslo.config/tree/oslo_config/cfg.py#n2337 : class ConfigOpts(collections.Mapping):

OpenStack Client Integration
============================

When the ``python-openstackclient`` package and ``beagle`` are both
installed, it is possible to search the OpenStack source code directly
from the ``openstack`` command line tool.

.. code-block:: console

   $ openstack code search --file '(.*requirement.*|.*constraint.*|setup.cfg|tox.ini)' 'cliff[><=]'

   +-----------------------+------------------------------------------------------------+------+------------------------------------+
   | Repository            | Filename                                                   | Line | Text                               |
   +-----------------------+------------------------------------------------------------+------+------------------------------------+
   | group-based-policy    | test-requirements.txt                                      |   20 | cliff>=2.3.0 # Apache-2.0          |
   | kolla-kubernetes      | requirements.txt                                           |    6 | cliff>=2.8.0 # Apache-2.0          |
   | networking-bigswitch  | test-requirements.txt                                      |    8 | cliff>=1.7.0  # Apache-2.0         |
   | networking-brocade    | test-requirements.txt                                      |    6 | cliff>=1.14.0  # Apache-2.0        |
   | networking-mlnx       | test-requirements.txt                                      |    6 | cliff>=1.15.0 # Apache-2.0         |
   | networking-plumgrid   | test-requirements.txt                                      |    3 | cliff>=2.2.0 # Apache-2.0          |
   | osops-tools-contrib   | ansible_requirements.txt                                   |    5 | cliff==2.2.0                       |
   | paunch                | requirements.txt                                           |    7 | cliff>=2.6.0  # Apache-2.0         |
   | rally                 | upper-constraints.txt                                      |   68 | cliff===2.11.0                     |
   | requirements          | global-requirements.txt                                    |   21 | cliff>=2.8.0,!=2.9.0  # Apache-2.0 |
   | requirements          | openstack_requirements/tests/files/gr-base.txt             |    9 | cliff>=1.4                         |
   | requirements          | openstack_requirements/tests/files/upper-constraints.txt   |  192 | cliff===2.4.0                      |
   | requirements          | upper-constraints.txt                                      |  216 | cliff===2.11.0                     |
   | rpm-packaging         | requirements.txt                                           |   21 | cliff>=2.8.0,!=2.9.0  # Apache-2.0 |
   +-----------------------+------------------------------------------------------------+------+------------------------------------+
