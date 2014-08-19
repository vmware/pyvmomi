
vim.dvs.VmwareDistributedVirtualSwitch.VmwareHealthCheckFeatureCapability
=========================================================================
  The feature capabilities of health check supported by the vSphere Distributed Switch
:extends: vim.DistributedVirtualSwitch.HealthCheckFeatureCapability_
:since: `vSphere API 5.1 <vim/version.rst#vimversionversion8>`_

Attributes:
    vlanMtuSupported (`bool <https://docs.python.org/2/library/stdtypes.html>`_):

       Flag to indicate whether vlan/mtu health check is supported on the vSphere Distributed Switch.
    teamingSupported (`bool <https://docs.python.org/2/library/stdtypes.html>`_):

       Flag to indicate whether teaming health check is supported on the vSphere Distributed Switch.
