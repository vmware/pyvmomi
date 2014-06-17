.. _str: https://docs.python.org/2/library/stdtypes.html

.. _long: https://docs.python.org/2/library/stdtypes.html

.. _bool: https://docs.python.org/2/library/stdtypes.html

.. _datetime: https://docs.python.org/2/library/stdtypes.html

.. _PowerState: ../../vim/HostSystem/PowerState.rst

.. _ConnectionState: ../../vim/HostSystem/ConnectionState.rst

.. _HostStandbyMode: ../../vim/HostSystem/StandbyMode.rst

.. _vmodl.DynamicData: ../../vmodl/DynamicData.rst

.. _VsanHostRuntimeInfo: ../../vim/vsan/host/VsanRuntimeInfo.rst

.. _vim.host.TpmDigestInfo: ../../vim/host/TpmDigestInfo.rst

.. _ExitMaintenanceMode_Task: ../../vim/HostSystem.rst#exitMaintenanceMode

.. _vim.HostSystem.PowerState: ../../vim/HostSystem/PowerState.rst

.. _EnterMaintenanceMode_Task: ../../vim/HostSystem.rst#enterMaintenanceMode

.. _vim.cluster.DasFdmHostState: ../../vim/cluster/DasFdmHostState.rst

.. _vim.vsan.host.VsanRuntimeInfo: ../../vim/vsan/host/VsanRuntimeInfo.rst

.. _vim.HostSystem.ConnectionState: ../../vim/HostSystem/ConnectionState.rst

.. _vim.host.HealthStatusSystem.Runtime: ../../vim/host/HealthStatusSystem/Runtime.rst

.. _vim.host.RuntimeInfo.NetworkRuntimeInfo: ../../vim/host/RuntimeInfo/NetworkRuntimeInfo.rst

.. _vim.host.VFlashManager.VFlashResourceRunTimeInfo: ../../vim/host/VFlashManager/VFlashResourceRunTimeInfo.rst


vim.host.RuntimeInfo
====================
  This data object type describes the runtime state of a host.
:extends: vmodl.DynamicData_

Attributes:
    connectionState (`vim.HostSystem.ConnectionState`_):

       The host connection state. See the description in the enums for the `ConnectionState`_ data object type.
    powerState (`vim.HostSystem.PowerState`_):

       The host power state. See the description in the enums for the `PowerState`_ data object type.
    standbyMode (`str`_, optional):

       The host's standby mode. For valid values see `HostStandbyMode`_ . The property is only populated by vCenter server. If queried directly from a ESX host, the property is is unset.
    inMaintenanceMode (`bool`_):

       The flag to indicate whether or not the host is in maintenance mode. This flag is set when the host has entered the maintenance mode. It is not set during the entering phase of maintenance mode.See `EnterMaintenanceMode_Task`_ See `ExitMaintenanceMode_Task`_ 
    bootTime (`datetime`_, optional):

       The time when the host was booted.
    healthSystemRuntime (`vim.host.HealthStatusSystem.Runtime`_, optional):

       Available system health status
    dasHostState (`vim.cluster.DasFdmHostState`_, optional):

       The availability state of an active host in a vSphere HA enabled cluster. A host is inactive if it is in maintenance or standby mode, or it has been disconnected from vCenter Server. The active hosts in a cluster form a vSphere HA fault domain.The property is unset if vSphere HA is disabled, the host is in maintenance or standby mode, or the host is disconnected from vCenter Server.
    tpmPcrValues (`vim.host.TpmDigestInfo`_, optional):

       The array of PCR digest values stored in the TPM device since the last host boot time.
    vsanRuntimeInfo (`vim.vsan.host.VsanRuntimeInfo`_, optional):

       Host Runtime information related to the VSAN service.See `VsanHostRuntimeInfo`_ 
    networkRuntimeInfo (`vim.host.RuntimeInfo.NetworkRuntimeInfo`_, optional):

       This property is for getting network related runtime info
    vFlashResourceRuntimeInfo (`vim.host.VFlashManager.VFlashResourceRunTimeInfo`_, optional):

       Runtime information of vFlash resource of the host.
    hostMaxVirtualDiskCapacity (`long`_, optional):

       The maximum theoretical virtual disk capacity supported by this host
