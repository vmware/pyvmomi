.. _str: https://docs.python.org/2/library/stdtypes.html

.. _bool: https://docs.python.org/2/library/stdtypes.html

.. _ConfigSpec: ../../vim/vm/ConfigSpec.rst

.. _vim.HostSystem: ../../vim/HostSystem.rst

.. _vmodl.DynamicData: ../../vmodl/DynamicData.rst

.. _EnvironmentBrowser: ../../vim/EnvironmentBrowser.rst

.. _defaultHardwareVersionKey: ../../vim/Datacenter/ConfigInfo.rst#defaultHardwareVersionKey

.. _queryDatacenterConfigOptionDescriptor: ../../vim/Datacenter.rst#queryConfigOptionDescriptor


vim.vm.ConfigOptionDescriptor
=============================
  Contains the definition of a unique key that can be used to retrieve a configOption object.
:extends: vmodl.DynamicData_

Attributes:
    key (`str`_):

       A unique key used to identify a configOption object in this `EnvironmentBrowser`_ .
    description (`str`_, optional):

       A description of the configOption object.
    host (`vim.HostSystem`_, optional):

       List of hosts to which this descriptor applies. List of hosts is not set when descriptor is returned from `queryDatacenterConfigOptionDescriptor`_ .
    createSupported (`bool`_):

       Indicates whether the associated set of configuration options can be used for virtual machine creation on a given host or cluster.
    defaultConfigOption (`bool`_):

       Indicates whether the associated set of virtual machine configuration options is the default one for a given host or cluster. Latest version is marked as default unless other version is specified via `defaultHardwareVersionKey`_ or `defaultHardwareVersionKey`_ . If this setting is TRUE, virtual machine creates will use the associated set of configuration options, unless a config version is explicitly specified in the `ConfigSpec`_ .
    runSupported (`bool`_):

       Indicates whether the associated set of configuration options can be used to power on a virtual machine on a given host or cluster.
    upgradeSupported (`bool`_):

       Indicates whether the associated set of configuration options can be used as a virtual hardware upgrade target.
