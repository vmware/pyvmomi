.. _str: https://docs.python.org/2/library/stdtypes.html

.. _bool: https://docs.python.org/2/library/stdtypes.html

.. _ListNamespaces: ../../vim/vm/NamespaceManager.rst#listNamespaces

.. _vmodl.DynamicData: ../../vmodl/DynamicData.rst

.. _GuestInfoAppStateType: ../../vim/vm/GuestInfo/AppStateType.rst

.. _maxSizeEventsFromGuest: ../../vim/vm/NamespaceManager/CreateSpec.rst#maxSizeEventsFromGuest

.. _vim.vm.GuestInfo.NicInfo: ../../vim/vm/GuestInfo/NicInfo.rst

.. _vim.vm.GuestInfo.DiskInfo: ../../vim/vm/GuestInfo/DiskInfo.rst

.. _vim.vm.GuestInfo.StackInfo: ../../vim/vm/GuestInfo/StackInfo.rst

.. _vim.vm.GuestInfo.ScreenInfo: ../../vim/vm/GuestInfo/ScreenInfo.rst

.. _vim.vm.GuestInfo.ToolsStatus: ../../vim/vm/GuestInfo/ToolsStatus.rst

.. _VirtualMachineToolsRunningStatus: ../../vim/vm/GuestInfo/ToolsRunningStatus.rst

.. _VirtualMachineToolsVersionStatus: ../../vim/vm/GuestInfo/ToolsVersionStatus.rst

.. _VirtualMachineAppHeartbeatStatusType: ../../vim/VirtualMachine/AppHeartbeatStatusType.rst

.. _vim.vm.GuestInfo.NamespaceGenerationInfo: ../../vim/vm/GuestInfo/NamespaceGenerationInfo.rst


vim.vm.GuestInfo
================
  Information about the guest operating system.Most of this information is collected by VMware Tools. In general, be sure you have VMware Tools installed and that the virtual machine is running when you access this information.
:extends: vmodl.DynamicData_

Attributes:
    toolsStatus (`vim.vm.GuestInfo.ToolsStatus`_, optional):

       Current status of VMware Tools in the guest operating system, if known.
    toolsVersionStatus (`str`_, optional):

       Current version status of VMware Tools in the guest operating system, if known. The set of possible values is described in `VirtualMachineToolsVersionStatus`_ for vSphere API 5.0.
    toolsVersionStatus2 (`str`_, optional):

       Current version status of VMware Tools in the guest operating system, if known. The set of possible values is described in `VirtualMachineToolsVersionStatus`_ 
    toolsRunningStatus (`str`_, optional):

       Current running status of VMware Tools in the guest operating system, if known. The set of possible values is described in `VirtualMachineToolsRunningStatus`_ 
    toolsVersion (`str`_, optional):

       Current version of VMware Tools, if known.
    guestId (`str`_, optional):

       Guest operating system identifier (short name), if known.
    guestFamily (`str`_, optional):

       Guest operating system family, if known.
    guestFullName (`str`_, optional):

       Guest operating system full name, if known.
    hostName (`str`_, optional):

       Hostname of the guest operating system, if known.
    ipAddress (`str`_, optional):

       Primary IP address assigned to the guest operating system, if known.
    net ([`vim.vm.GuestInfo.NicInfo`_], optional):

       Guest information about network adapters, if known.
    ipStack ([`vim.vm.GuestInfo.StackInfo`_], optional):

       Guest information about IP networking stack, if known.
    disk ([`vim.vm.GuestInfo.DiskInfo`_], optional):

       Guest information about disks.You can obtain Linux guest disk information for the following file system types only: Ext2, Ext3, Ext4, ReiserFS, ZFS, NTFS, VFAT, UFS, PCFS, HFS, and MS-DOS.
    screen (`vim.vm.GuestInfo.ScreenInfo`_, optional):

       Guest screen resolution info, if known.
    guestState (`str`_):

       Operation mode of guest operating system. One of:
        * "running" - Guest is running normally.
        * "shuttingdown" - Guest has a pending shutdown command.
        * "resetting" - Guest has a pending reset command.
        * "standby" - Guest has a pending standby command.
        * "notRunning" - Guest is not running.
        * "unknown" - Guest information is not available.
        * 
    appHeartbeatStatus (`str`_, optional):

       Application heartbeat status. Please see `VirtualMachineAppHeartbeatStatusType`_ 
    appState (`str`_, optional):

       Application state. If vSphere HA is enabled and the vm is configured for Application Monitoring and this field's value is "appStateNeedReset" then HA will attempt immediately reset the vm. There are some system conditions which may delay the immediate reset. The immediate reset will be performed as soon as allowed by vSphere HA and ESX. If during these conditions the value is changed to appStateOk the reset will be cancelled.See `GuestInfoAppStateType`_ 
    guestOperationsReady (`bool`_, optional):

       Guest Operations availability. If true, the vitrual machine is ready to process guest operations.
    interactiveGuestOperationsReady (`bool`_, optional):

       Interactive Guest Operations availability. If true, the vitrual machine is ready to process guest operations as the user interacting with the guest desktop.
    generationInfo ([`vim.vm.GuestInfo.NamespaceGenerationInfo`_, privilege: VirtualMachine.Namespace.EventNotify], optional):

       A list of namespaces and their corresponding generation numbers. Only namespaces with non-zero `maxSizeEventsFromGuest`_ are guaranteed to be present here. Use `ListNamespaces`_ to retrieve list of namespaces.
