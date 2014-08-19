
vim.dvs.DistributedVirtualPort.ConfigInfo
=========================================
  Management related configuration of a DistributedVirtualPort.
:extends: vmodl.DynamicData_
:since: `vSphere API 4.0 <vim/version.rst#vimversionversion5>`_

Attributes:
    name (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       The name of the port.
    scope ([`vim.ManagedEntity <vim/ManagedEntity.rst>`_], optional):

       The eligible entities that can connect to the port. If unset, there is no restriction on which entity can connect to the port. If set, only the entities in the specified list or their child entities are allowed to connect to the port. If scopes are defined at both port and portgroup level, they are taken as an "AND" relationship. If such a relationship doesn't make sense, the reconfigure operation will raise an exception.
    description (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       A description string of the port.
    setting (`vim.dvs.DistributedVirtualPort.Setting <vim/dvs/DistributedVirtualPort/Setting.rst>`_, optional):

       The network configuration of the port.
    configVersion (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       The version string of the configuration.
