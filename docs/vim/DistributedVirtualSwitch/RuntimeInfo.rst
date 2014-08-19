
vim.DistributedVirtualSwitch.RuntimeInfo
========================================
  The `DVSRuntimeInfo <vim/DistributedVirtualSwitch/RuntimeInfo.rst>`_ data object defines runtime information for a vSphere Distributed Switch.
:extends: vmodl.DynamicData_
:since: `vSphere API 5.1 <vim/version.rst#vimversionversion8>`_

Attributes:
    hostMemberRuntime ([`vim.dvs.HostMember.RuntimeInfo <vim/dvs/HostMember/RuntimeInfo.rst>`_], optional):

       Runtime information of the hosts that joined the switch.
