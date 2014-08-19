
vim.dvs.DistributedVirtualPort.ConfigSpec
=========================================
  Specification to reconfigure a `DistributedVirtualPort <vim/dvs/DistributedVirtualPort.rst>`_ .
:extends: vmodl.DynamicData_
:since: `vSphere API 4.0 <vim/version.rst#vimversionversion5>`_

Attributes:
    operation (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       The operation to remove or modify the existing ports. The valid values are:
        * `edit <vim/ConfigSpecOperation.rst#edit>`_
        * `remove <vim/ConfigSpecOperation.rst#remove>`_
    key (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Key of the port to be reconfigured.
    name (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       The name of the port.
    scope ([`vim.ManagedEntity <vim/ManagedEntity.rst>`_], optional):

       The eligible entities that can connect to the port, for detail see `scope <vim/dvs/DistributedVirtualPort/ConfigInfo.rst#scope>`_ .
    description (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       The description string of the port.
    setting (`vim.dvs.DistributedVirtualPort.Setting <vim/dvs/DistributedVirtualPort/Setting.rst>`_, optional):

       The network setting of the port.
    configVersion (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       The version string of the configuration.
