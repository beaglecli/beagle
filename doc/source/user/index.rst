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

   $ beagle search -f grep --context-lines 5 --repo openstack/oslo.config 'class ConfigOpts'
   openstack/oslo.config:doc/source/reference/configuration-files.rst:5:The config manager has two CLI options defined by default, ``--config-file``
   openstack/oslo.config:doc/source/reference/configuration-files.rst:6:and ``--config-dir``:
   openstack/oslo.config:doc/source/reference/configuration-files.rst:7:
   openstack/oslo.config:doc/source/reference/configuration-files.rst:8:.. code-block:: python
   openstack/oslo.config:doc/source/reference/configuration-files.rst:9:
   openstack/oslo.config:doc/source/reference/configuration-files.rst:10:class ConfigOpts(object):
   openstack/oslo.config:doc/source/reference/configuration-files.rst:11:
   openstack/oslo.config:doc/source/reference/configuration-files.rst:12:        def __call__(self, ...):
   openstack/oslo.config:doc/source/reference/configuration-files.rst:13:
   openstack/oslo.config:doc/source/reference/configuration-files.rst:14:            opts = [
   openstack/oslo.config:doc/source/reference/configuration-files.rst:15:                MultiStrOpt('config-file',
   openstack/oslo.config:oslo_config/cfg.py:1920:    def print_usage(self, file=None):
   openstack/oslo.config:oslo_config/cfg.py:1921:        self.initialize_parser_arguments()
   openstack/oslo.config:oslo_config/cfg.py:1922:        super(_CachedArgumentParser, self).print_usage(file)
   openstack/oslo.config:oslo_config/cfg.py:1923:
   openstack/oslo.config:oslo_config/cfg.py:1924:
   openstack/oslo.config:oslo_config/cfg.py:1925:class ConfigOpts(abc.Mapping):
   openstack/oslo.config:oslo_config/cfg.py:1926:
   openstack/oslo.config:oslo_config/cfg.py:1927:    """Config options which may be set on the command line or in config files.
   openstack/oslo.config:oslo_config/cfg.py:1928:
   openstack/oslo.config:oslo_config/cfg.py:1929:    ConfigOpts is a configuration option manager with APIs for registering
   openstack/oslo.config:oslo_config/cfg.py:1930:    option schemas, grouping options, parsing option values and retrieving


To produce links to the source on the OpenStack git server, use the
``link`` formatter:

.. code-block:: console

   $ beagle --debug search -f link --repo openstack/oslo.config 'class ConfigOpts'
   https://opendev.org/openstack/oslo.config/src/branch/master/doc/source/reference/configuration-files.rst#n10 : class ConfigOpts(object):
   https://opendev.org/openstack/oslo.config/src/branch/master/oslo_config/cfg.py#n1925 : class ConfigOpts(abc.Mapping):

To filter repositories in search results, use the ``--repo-pattern`` option.

Example to show which openstack oslo project call the ``ssl.wrap_socket``
function:

.. code-block:: console

   $ beagle search --ignore-comments -f link --repo-pattern "openstack/oslo.*" 'ssl.wrap_socket'
   https://opendev.org/openstack/oslo.service/src/branch/master/oslo_service/sslutils.py#n104 : return ssl.wrap_socket(sock, **ssl_kwargs)  # nosec
   https://opendev.org/openstack/oslo.service/src/branch/master/oslo_service/tests/test_sslutils.py#n81 : @mock.patch("ssl.wrap_socket")

Same research only in the whole openstack projects
(will ignore starlingx, etc):

.. code-block:: console

   $ beagle search --ignore-comments -f link --repo-pattern "openstack/*" 'ssl.wrap_socket'
   https://opendev.org/openstack/glance/src/branch/master/glance/common/client.py#n124 : ssl.wrap_socket(), which forces SSL to check server certificate against
   https://opendev.org/openstack/glance/src/branch/master/glance/common/client.py#n133 : self.sock = ssl.wrap_socket(sock, self.key_file, self.cert_file,
   https://opendev.org/openstack/glance/src/branch/master/glance/common/client.py#n136 : self.sock = ssl.wrap_socket(sock, self.key_file, self.cert_file,
   https://opendev.org/openstack/heat/src/branch/master/heat/common/wsgi.py#n239 : ssl.wrap_socket if conf specifies cert_file
   https://opendev.org/openstack/heat/src/branch/master/heat/common/wsgi.py#n414 : self.sock = ssl.wrap_socket(self._sock,

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
