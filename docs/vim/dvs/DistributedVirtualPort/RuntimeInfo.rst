
vim.dvs.DistributedVirtualPort.RuntimeInfo
==========================================
  The `DVPortStatus <vim/dvs/DistributedVirtualPort/RuntimeInfo.rst>`_ data object contains runtime information about a `DistributedVirtualPort <vim/dvs/DistributedVirtualPort.rst>`_ .
:extends: vmodl.DynamicData_
:since: `vSphere API 4.0 <vim/version.rst#vimversionversion5>`_

Attributes:
    linkUp (`bool <https://docs.python.org/2/library/stdtypes.html>`_):

       Indicates whether the port is in linkUp status.
    blocked (`bool <https://docs.python.org/2/library/stdtypes.html>`_):

       Indicates whether the port is blocked by switch implementation.
    vlanIds ([`vim.NumericRange <vim/NumericRange.rst>`_], optional):

       VLAN ID of the port.
    trunkingMode (`bool <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       True if the port VLAN tagging/stripping is disabled.
    mtu (`int <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Maximum transmission unit (MTU) of the port. You can set the MTU only at the switch level ( `VMwareDVSConfigSpec <vim/dvs/VmwareDistributedVirtualSwitch/ConfigSpec.rst>`_ ). If you attempt to change it at the portgroup or port level, the Server throws an exception.
    linkPeer (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Name of the connected entity.
    macAddress (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       The MAC address that is used at this port.
    statusDetail (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Additional information regarding the current status of the port.
    vmDirectPathGen2Active (`bool <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Indicates whether VMDirectPath Gen 2 is active on this port. If false, the reason(s) for inactivity will be provided in one or more of `vmDirectPathGen2InactiveReasonNetwork <vim/dvs/DistributedVirtualPort/RuntimeInfo.rst#vmDirectPathGen2InactiveReasonNetwork>`_ , `vmDirectPathGen2InactiveReasonOther <vim/dvs/DistributedVirtualPort/RuntimeInfo.rst#vmDirectPathGen2InactiveReasonOther>`_ , and `vmDirectPathGen2InactiveReasonExtended <vim/dvs/DistributedVirtualPort/RuntimeInfo.rst#vmDirectPathGen2InactiveReasonExtended>`_ .If the host software is not capable of VMDirectPath Gen 2, this property will be unset. See `HostCapability <vim/host/Capability.rst>`_ . `vmDirectPathGen2Supported <vim/host/Capability.rst#vmDirectPathGen2Supported>`_ .
    vmDirectPathGen2InactiveReasonNetwork ([`str <https://docs.python.org/2/library/stdtypes.html>`_], optional):

       If `vmDirectPathGen2Active <vim/dvs/DistributedVirtualPort/RuntimeInfo.rst#vmDirectPathGen2Active>`_ is false, this array will be populated with reasons for the inactivity that are related to network state or configuration. The reasons are chosen from the `DVPortStatusVmDirectPathGen2InactiveReasonNetwork <vim/dvs/DistributedVirtualPort/RuntimeInfo/VmDirectPathGen2InactiveReasonNetwork.rst>`_ values.Other reasons for inactivity will be provided in `vmDirectPathGen2InactiveReasonOther <vim/dvs/DistributedVirtualPort/RuntimeInfo.rst#vmDirectPathGen2InactiveReasonOther>`_ . If there is a reason for inactivity that cannot be described by the available constants, `vmDirectPathGen2InactiveReasonExtended <vim/dvs/DistributedVirtualPort/RuntimeInfo.rst#vmDirectPathGen2InactiveReasonExtended>`_ will be populated with an additional explanation provided by the platform.Note that this list of reasons is not guaranteed to be exhaustive.
    vmDirectPathGen2InactiveReasonOther ([`str <https://docs.python.org/2/library/stdtypes.html>`_], optional):

       If `vmDirectPathGen2Active <vim/dvs/DistributedVirtualPort/RuntimeInfo.rst#vmDirectPathGen2Active>`_ is false, this array will be populated with reasons for the inactivity that are not related to network state or configuration. The reasons are chosen from the `DVPortStatusVmDirectPathGen2InactiveReasonOther <vim/dvs/DistributedVirtualPort/RuntimeInfo/VmDirectPathGen2InactiveReasonOther.rst>`_ values.Network-related reasons for inactivity will be provided in `vmDirectPathGen2InactiveReasonNetwork <vim/dvs/DistributedVirtualPort/RuntimeInfo.rst#vmDirectPathGen2InactiveReasonNetwork>`_ . If there is a reason for inactivity that cannot be described by the available constants, `vmDirectPathGen2InactiveReasonExtended <vim/dvs/DistributedVirtualPort/RuntimeInfo.rst#vmDirectPathGen2InactiveReasonExtended>`_ will be populated with an additional explanation provided by the platform.Note that this list of reasons is not guaranteed to be exhaustive.See `vmDirectPathGen2Supported <vim/host/Capability.rst#vmDirectPathGen2Supported>`_ 
    vmDirectPathGen2InactiveReasonExtended (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       If `vmDirectPathGen2Active <vim/dvs/DistributedVirtualPort/RuntimeInfo.rst#vmDirectPathGen2Active>`_ is false, this property may contain an explanation provided by the platform, beyond the reasons (if any) listed in `vmDirectPathGen2InactiveReasonNetwork <vim/dvs/DistributedVirtualPort/RuntimeInfo.rst#vmDirectPathGen2InactiveReasonNetwork>`_ and/or `vmDirectPathGen2InactiveReasonOther <vim/dvs/DistributedVirtualPort/RuntimeInfo.rst#vmDirectPathGen2InactiveReasonOther>`_ .
