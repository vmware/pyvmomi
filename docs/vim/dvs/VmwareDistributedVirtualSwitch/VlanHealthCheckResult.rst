.. _vSphere API 5.1: ../../../vim/version.rst#vimversionversion8

.. _vim.NumericRange: ../../../vim/NumericRange.rst

.. _vim.dvs.HostMember.UplinkHealthCheckResult: ../../../vim/dvs/HostMember/UplinkHealthCheckResult.rst


vim.dvs.VmwareDistributedVirtualSwitch.VlanHealthCheckResult
============================================================
  This class defines Vlan health check result of an uplink port in the VMware vSphered Distributed Switch.
:extends: vim.dvs.HostMember.UplinkHealthCheckResult_
:since: `vSphere API 5.1`_

Attributes:
    trunkedVlan (`vim.NumericRange`_, optional):

       The vlans which are trunked by the physical switch connected to the uplink port. If the vlan is not a range, but a single Id, both start and end have the same value with the single vlan Id.
    untrunkedVlan (`vim.NumericRange`_, optional):

       The vlans which are not trunked by the physical switch connected to the uplink port. If the vlan is not a range, but a single Id, both start and end have the same value with the single vlan Id.
