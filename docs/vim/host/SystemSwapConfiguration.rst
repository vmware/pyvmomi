
vim.host.SystemSwapConfiguration
================================
  Information and specification for control of the system swap configuration on the current host.
:extends: vmodl.DynamicData_
:since: `vSphere API 5.1 <vim/version.rst#vimversionversion8>`_

Attributes:
    option ([`vim.host.SystemSwapConfiguration.SystemSwapOption <vim/host/SystemSwapConfiguration/SystemSwapOption.rst>`_], optional):

       The currently enabled options. When this property contains only one value and this value is `HostSystemSwapConfigurationDisabledOption <vim/host/SystemSwapConfiguration/DisabledOption.rst>`_ , this indicates that the system swap is disabled.If the `HostSystemSwapConfigurationDisabledOption <vim/host/SystemSwapConfiguration/DisabledOption.rst>`_ option is used toghether with some other option in call to `UpdateSystemSwapConfiguration <vim/HostSystem.rst#updateSystemSwapConfiguration>`_ , a `InvalidArgument <vmodl/fault/InvalidArgument.rst>`_ is thrown.It is not allowed to have duplicate values in this array. If so a `InvalidArgument <vmodl/fault/InvalidArgument.rst>`_ is thrown.
