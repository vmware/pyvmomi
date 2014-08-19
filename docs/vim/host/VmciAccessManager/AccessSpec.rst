
vim.host.VmciAccessManager.AccessSpec
=====================================
  The AccessSpec data object declares an update to the service access granted to a VM. The given list of services will either be granted in addition to existing services, replace the existing service or be revoked depending on the mode specified. In case of a revoke, an empty or non-existing service list indicates that all granted services should be revoked.
:extends: vmodl.DynamicData_
:since: `vSphere API 5.0 <vim/version.rst#vimversionversion7>`_

Attributes:
    vm (`vim.VirtualMachine <vim/VirtualMachine.rst>`_):

    services ([`str <https://docs.python.org/2/library/stdtypes.html>`_], optional):

    mode (`str <https://docs.python.org/2/library/stdtypes.html>`_):

