
vim.host.SystemSwapConfiguration.DisabledOption
===============================================
  Indicates that the system swap on the host is currently disabled. This value is used with the `UpdateSystemSwapConfiguration <vim/HostSystem.rst#updateSystemSwapConfiguration>`_ managed method to disable system swap. Presence of this value in `option <vim/host/SystemSwapConfiguration.rst#option>`_ excludes appearance of any other options. Specifying additional options will result in a `InvalidArgument <vmodl/fault/InvalidArgument.rst>`_ fault being thrown from the `UpdateSystemSwapConfiguration <vim/HostSystem.rst#updateSystemSwapConfiguration>`_ method.
:extends: vim.host.SystemSwapConfiguration.SystemSwapOption_
:since: `vSphere API 5.1 <vim/version.rst#vimversionversion8>`_

Attributes:
