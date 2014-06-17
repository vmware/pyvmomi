.. _str: https://docs.python.org/2/library/stdtypes.html

.. _vSphere API 5.1: ../../../vim/version.rst#vimversionversion8

.. _vim.dvs.HostMember.HealthCheckResult: ../../../vim/dvs/HostMember/HealthCheckResult.rst


vim.dvs.VmwareDistributedVirtualSwitch.TeamingHealthCheckResult
===============================================================
  This class defines teaming health check result of a host that joined the VMware vSphered Distributed Switch.
:extends: vim.dvs.HostMember.HealthCheckResult_
:since: `vSphere API 5.1`_

Attributes:
    teamingStatus (`str`_):

       Teaming check status. See TeamingMatchStatus for valid values.
