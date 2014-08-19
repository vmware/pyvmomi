
vim.host.DhcpService.Config
===========================
  This data object type describes the configuration of a DHCP service instance representing both the configured properties on the instance and identification information.
:extends: vmodl.DynamicData_
:since: `VI API 2.5 <vim/version.rst#vimversionversion2>`_

Attributes:
    changeOperation (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Indicates the change operation to apply on this configuration specification.See `HostConfigChangeOperation <vim/host/ConfigChange/Operation.rst>`_ 
    key (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       The instance ID of the DHCP service.
    spec (`vim.host.DhcpService.Specification <vim/host/DhcpService/Specification.rst>`_):

       Specification of the DHCP service.
