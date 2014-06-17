.. _option: ../../../vim/host/SystemSwapConfiguration.rst#option

.. _vSphere API 5.1: ../../../vim/version.rst#vimversionversion8

.. _InvalidArgument: ../../../vmodl/fault/InvalidArgument.rst

.. _UpdateSystemSwapConfiguration: ../../../vim/HostSystem.rst#updateSystemSwapConfiguration

.. _vim.host.SystemSwapConfiguration.SystemSwapOption: ../../../vim/host/SystemSwapConfiguration/SystemSwapOption.rst


vim.host.SystemSwapConfiguration.DisabledOption
===============================================
  Indicates that the system swap on the host is currently disabled. This value is used with the `UpdateSystemSwapConfiguration`_ managed method to disable system swap. Presence of this value in `option`_ excludes appearance of any other options. Specifying additional options will result in a `InvalidArgument`_ fault being thrown from the `UpdateSystemSwapConfiguration`_ method.
:extends: vim.host.SystemSwapConfiguration.SystemSwapOption_
:since: `vSphere API 5.1`_

Attributes:
