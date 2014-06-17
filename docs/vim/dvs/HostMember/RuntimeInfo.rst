.. _str: https://docs.python.org/2/library/stdtypes.html

.. _status: ../../../vim/dvs/HostMember.rst#status

.. _statusDetail: ../../../vim/dvs/HostMember.rst#statusDetail

.. _vim.HostSystem: ../../../vim/HostSystem.rst

.. _vSphere API 5.1: ../../../vim/version.rst#vimversionversion8

.. _vmodl.DynamicData: ../../../vmodl/DynamicData.rst

.. _HostComponentState: ../../../vim/dvs/HostMember/HostComponentState.rst

.. _HostMemberRuntimeInfo: ../../../vim/dvs/HostMember/RuntimeInfo.rst

.. _DistributedVirtualSwitchHostMember: ../../../vim/dvs/HostMember.rst

.. _vim.dvs.HostMember.HealthCheckResult: ../../../vim/dvs/HostMember/HealthCheckResult.rst


vim.dvs.HostMember.RuntimeInfo
==============================
  The `HostMemberRuntimeInfo`_ data object contains healthcheck and status information about a host member of a distributed virtual switch.
:extends: vmodl.DynamicData_
:since: `vSphere API 5.1`_

Attributes:
    host (`vim.HostSystem`_):

       The host.
    status (`str`_, optional):

       Host proxy switch status. See `HostComponentState`_ for valid values. This property replaces the deprecated `DistributedVirtualSwitchHostMember`_ . `status`_ .
    statusDetail (`str`_, optional):

       Additional information regarding the current membership status of the host. This property replaces the deprecated `DistributedVirtualSwitchHostMember`_ . `statusDetail`_ .
    healthCheckResult (`vim.dvs.HostMember.HealthCheckResult`_, optional):

       Health check result for the host that joined the distributed virtual switch.
