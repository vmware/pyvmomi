.. _InvalidArgument: ../../vmodl/fault/InvalidArgument.rst

.. _vSphere API 5.1: ../../vim/version.rst#vimversionversion8

.. _vmodl.DynamicData: ../../vmodl/DynamicData.rst

.. _UpdateSystemSwapConfiguration: ../../vim/HostSystem.rst#updateSystemSwapConfiguration

.. _HostSystemSwapConfigurationDisabledOption: ../../vim/host/SystemSwapConfiguration/DisabledOption.rst

.. _vim.host.SystemSwapConfiguration.SystemSwapOption: ../../vim/host/SystemSwapConfiguration/SystemSwapOption.rst


vim.host.SystemSwapConfiguration
================================
  Information and specification for control of the system swap configuration on the current host.
:extends: vmodl.DynamicData_
:since: `vSphere API 5.1`_

Attributes:
    option (`vim.host.SystemSwapConfiguration.SystemSwapOption`_, optional):

       The currently enabled options. When this property contains only one value and this value is `HostSystemSwapConfigurationDisabledOption`_ , this indicates that the system swap is disabled.If the `HostSystemSwapConfigurationDisabledOption`_ option is used toghether with some other option in call to `UpdateSystemSwapConfiguration`_ , a `InvalidArgument`_ is thrown.It is not allowed to have duplicate values in this array. If so a `InvalidArgument`_ is thrown.
