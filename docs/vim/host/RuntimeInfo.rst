
vim.host.RuntimeInfo
====================
  This data object type describes the runtime state of a host.
:extends: vmodl.DynamicData_

Attributes:
    connectionState (`vim.HostSystem.ConnectionState <vim/HostSystem/ConnectionState.rst>`_):

       The host connection state. See the description in the enums for the `ConnectionState <vim/HostSystem/ConnectionState.rst>`_ data object type.
    powerState (`vim.HostSystem.PowerState <vim/HostSystem/PowerState.rst>`_):

       The host power state. See the description in the enums for the `PowerState <vim/HostSystem/PowerState.rst>`_ data object type.
    standbyMode (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       The host's standby mode. For valid values see `HostStandbyMode <vim/HostSystem/StandbyMode.rst>`_ . The property is only populated by vCenter server. If queried directly from a ESX host, the property is is unset.
    inMaintenanceMode (`bool <https://docs.python.org/2/library/stdtypes.html>`_):

       The flag to indicate whether or not the host is in maintenance mode. This flag is set when the host has entered the maintenance mode. It is not set during the entering phase of maintenance mode.See `EnterMaintenanceMode_Task <vim/HostSystem.rst#enterMaintenanceMode>`_ See `ExitMaintenanceMode_Task <vim/HostSystem.rst#exitMaintenanceMode>`_ 
    bootTime (`datetime <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       The time when the host was booted.
    healthSystemRuntime (`vim.host.HealthStatusSystem.Runtime <vim/host/HealthStatusSystem/Runtime.rst>`_, optional):

       Available system health status
    dasHostState (`vim.cluster.DasFdmHostState <vim/cluster/DasFdmHostState.rst>`_, optional):

       The availability state of an active host in a vSphere HA enabled cluster. A host is inactive if it is in maintenance or standby mode, or it has been disconnected from vCenter Server. The active hosts in a cluster form a vSphere HA fault domain.The property is unset if vSphere HA is disabled, the host is in maintenance or standby mode, or the host is disconnected from vCenter Server.
    tpmPcrValues ([`vim.host.TpmDigestInfo <vim/host/TpmDigestInfo.rst>`_], optional):

       The array of PCR digest values stored in the TPM device since the last host boot time.
    vsanRuntimeInfo (`vim.vsan.host.VsanRuntimeInfo <vim/vsan/host/VsanRuntimeInfo.rst>`_, optional):

       Host Runtime information related to the VSAN service.See `VsanHostRuntimeInfo <vim/vsan/host/VsanRuntimeInfo.rst>`_ 
    networkRuntimeInfo (`vim.host.RuntimeInfo.NetworkRuntimeInfo <vim/host/RuntimeInfo/NetworkRuntimeInfo.rst>`_, optional):

       This property is for getting network related runtime info
    vFlashResourceRuntimeInfo (`vim.host.VFlashManager.VFlashResourceRunTimeInfo <vim/host/VFlashManager/VFlashResourceRunTimeInfo.rst>`_, optional):

       Runtime information of vFlash resource of the host.
    hostMaxVirtualDiskCapacity (`long <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       The maximum theoretical virtual disk capacity supported by this host
