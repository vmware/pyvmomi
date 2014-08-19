
vim.host.NatService.Config
==========================
  This data object type describes the network address translation (NAT) service configuration representing both the configured properties on a NAT Service and identification information.
:extends: vmodl.DynamicData_
:since: `VI API 2.5 <vim/version.rst#vimversionversion2>`_

Attributes:
    changeOperation (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Indicates the change operation to apply on this configuration specification.See `HostConfigChangeOperation <vim/host/ConfigChange/Operation.rst>`_ 
    key (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       The instance ID of the NAT service.
    spec (`vim.host.NatService.Specification <vim/host/NatService/Specification.rst>`_):

       The specification of the NAT service.
