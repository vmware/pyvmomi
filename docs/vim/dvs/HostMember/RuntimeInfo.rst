
vim.dvs.HostMember.RuntimeInfo
==============================
  The `HostMemberRuntimeInfo <vim/dvs/HostMember/RuntimeInfo.rst>`_ data object contains healthcheck and status information about a host member of a distributed virtual switch.
:extends: vmodl.DynamicData_
:since: `vSphere API 5.1 <vim/version.rst#vimversionversion8>`_

Attributes:
    host (`vim.HostSystem <vim/HostSystem.rst>`_):

       The host.
    status (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Host proxy switch status. See `HostComponentState <vim/dvs/HostMember/HostComponentState.rst>`_ for valid values. This property replaces the deprecated `DistributedVirtualSwitchHostMember <vim/dvs/HostMember.rst>`_ . `status <vim/dvs/HostMember.rst#status>`_ .
    statusDetail (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Additional information regarding the current membership status of the host. This property replaces the deprecated `DistributedVirtualSwitchHostMember <vim/dvs/HostMember.rst>`_ . `statusDetail <vim/dvs/HostMember.rst#statusDetail>`_ .
    healthCheckResult ([`vim.dvs.HostMember.HealthCheckResult <vim/dvs/HostMember/HealthCheckResult.rst>`_], optional):

       Health check result for the host that joined the distributed virtual switch.
