.. _bool: https://docs.python.org/2/library/stdtypes.html

.. _vSphere API 5.1: ../../../vim/version.rst#vimversionversion8

.. _vim.NumericRange: ../../../vim/NumericRange.rst

.. _vlanSupportSwitchMtu: ../../../vim/dvs/VmwareDistributedVirtualSwitch/MtuHealthCheckResult.rst#vlanSupportSwitchMtu

.. _vlanNotSupportSwitchMtu: ../../../vim/dvs/VmwareDistributedVirtualSwitch/MtuHealthCheckResult.rst#vlanNotSupportSwitchMtu

.. _vim.dvs.HostMember.UplinkHealthCheckResult: ../../../vim/dvs/HostMember/UplinkHealthCheckResult.rst


vim.dvs.VmwareDistributedVirtualSwitch.MtuHealthCheckResult
===========================================================
  This class defines MTU health check result of an uplink port in the VMware vSphered Distributed Switch.
:extends: vim.dvs.HostMember.UplinkHealthCheckResult_
:since: `vSphere API 5.1`_

Attributes:
    mtuMismatch (`bool`_):

       True if the MTU configured in the vSphere Distributed Switch is different from the value configured in the Physical NIC, else false. If it is true, MTU health check is stopped. In this case, `vlanSupportSwitchMtu`_ and `vlanNotSupportSwitchMtu`_ will not have values.
    vlanSupportSwitchMtu ([`vim.NumericRange`_], optional):

       The vlan's MTU setting on physical switch allows vSphere Distributed Switch max MTU size packets passing. If the vlan is not a range, but a single Id, both start and end have the same value with the single vlan Id.
    vlanNotSupportSwitchMtu ([`vim.NumericRange`_], optional):

       The vlan's MTU setting on physical switch does not allow vSphere Distributed Switch max MTU size packets passing. If the vlan is not a range, but a single Id, both start and end have the same value with the single vlan Id.
