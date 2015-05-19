.. _bool: https://docs.python.org/2/library/stdtypes.html

.. _vSphere API 5.1: ../../../vim/version.rst#vimversionversion8

.. _vim.DistributedVirtualSwitch.HealthCheckFeatureCapability: ../../../vim/DistributedVirtualSwitch/HealthCheckFeatureCapability.rst


vim.dvs.VmwareDistributedVirtualSwitch.VmwareHealthCheckFeatureCapability
=========================================================================
  The feature capabilities of health check supported by the vSphere Distributed Switch
:extends: vim.DistributedVirtualSwitch.HealthCheckFeatureCapability_
:since: `vSphere API 5.1`_

Attributes:
    vlanMtuSupported (`bool`_):

       Flag to indicate whether vlan/mtu health check is supported on the vSphere Distributed Switch.
    teamingSupported (`bool`_):

       Flag to indicate whether teaming health check is supported on the vSphere Distributed Switch.
