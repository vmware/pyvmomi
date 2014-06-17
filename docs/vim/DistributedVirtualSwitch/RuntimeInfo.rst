.. _DVSRuntimeInfo: ../../vim/DistributedVirtualSwitch/RuntimeInfo.rst

.. _vSphere API 5.1: ../../vim/version.rst#vimversionversion8

.. _vmodl.DynamicData: ../../vmodl/DynamicData.rst

.. _vim.dvs.HostMember.RuntimeInfo: ../../vim/dvs/HostMember/RuntimeInfo.rst


vim.DistributedVirtualSwitch.RuntimeInfo
========================================
  The `DVSRuntimeInfo`_ data object defines runtime information for a vSphere Distributed Switch.
:extends: vmodl.DynamicData_
:since: `vSphere API 5.1`_

Attributes:
    hostMemberRuntime (`vim.dvs.HostMember.RuntimeInfo`_, optional):

       Runtime information of the hosts that joined the switch.
