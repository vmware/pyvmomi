
vim.vm.ConfigOptionDescriptor
=============================
  Contains the definition of a unique key that can be used to retrieve a configOption object.
:extends: vmodl.DynamicData_

Attributes:
    key (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       A unique key used to identify a configOption object in this `EnvironmentBrowser <vim/EnvironmentBrowser.rst>`_ .
    description (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       A description of the configOption object.
    host ([`vim.HostSystem <vim/HostSystem.rst>`_], optional):

       List of hosts to which this descriptor applies. List of hosts is not set when descriptor is returned from `queryDatacenterConfigOptionDescriptor <vim/Datacenter.rst#queryConfigOptionDescriptor>`_ .
    createSupported (`bool <https://docs.python.org/2/library/stdtypes.html>`_):

       Indicates whether the associated set of configuration options can be used for virtual machine creation on a given host or cluster.
    defaultConfigOption (`bool <https://docs.python.org/2/library/stdtypes.html>`_):

       Indicates whether the associated set of virtual machine configuration options is the default one for a given host or cluster. Latest version is marked as default unless other version is specified via `defaultHardwareVersionKey <vim/ComputeResource/ConfigInfo.rst#defaultHardwareVersionKey>`_ or `defaultHardwareVersionKey <vim/Datacenter/ConfigInfo.rst#defaultHardwareVersionKey>`_ . If this setting is TRUE, virtual machine creates will use the associated set of configuration options, unless a config version is explicitly specified in the `ConfigSpec <vim/vm/ConfigSpec.rst>`_ .
    runSupported (`bool <https://docs.python.org/2/library/stdtypes.html>`_):

       Indicates whether the associated set of configuration options can be used to power on a virtual machine on a given host or cluster.
    upgradeSupported (`bool <https://docs.python.org/2/library/stdtypes.html>`_):

       Indicates whether the associated set of configuration options can be used as a virtual hardware upgrade target.
