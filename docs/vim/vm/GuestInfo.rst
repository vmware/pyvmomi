
vim.vm.GuestInfo
================
  Information about the guest operating system.Most of this information is collected by VMware Tools. In general, be sure you have VMware Tools installed and that the virtual machine is running when you access this information.
:extends: vmodl.DynamicData_

Attributes:
    toolsStatus (`vim.vm.GuestInfo.ToolsStatus <vim/vm/GuestInfo/ToolsStatus.rst>`_, optional):

       Current status of VMware Tools in the guest operating system, if known.
    toolsVersionStatus (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Current version status of VMware Tools in the guest operating system, if known. The set of possible values is described in `VirtualMachineToolsVersionStatus <vim/vm/GuestInfo/ToolsVersionStatus.rst>`_ for vSphere API 5.0.
    toolsVersionStatus2 (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Current version status of VMware Tools in the guest operating system, if known. The set of possible values is described in `VirtualMachineToolsVersionStatus <vim/vm/GuestInfo/ToolsVersionStatus.rst>`_ 
    toolsRunningStatus (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Current running status of VMware Tools in the guest operating system, if known. The set of possible values is described in `VirtualMachineToolsRunningStatus <vim/vm/GuestInfo/ToolsRunningStatus.rst>`_ 
    toolsVersion (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Current version of VMware Tools, if known.
    guestId (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Guest operating system identifier (short name), if known.
    guestFamily (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Guest operating system family, if known.
    guestFullName (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Guest operating system full name, if known.
    hostName (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Hostname of the guest operating system, if known.
    ipAddress (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Primary IP address assigned to the guest operating system, if known.
    net ([`vim.vm.GuestInfo.NicInfo <vim/vm/GuestInfo/NicInfo.rst>`_], optional):

       Guest information about network adapters, if known.
    ipStack ([`vim.vm.GuestInfo.StackInfo <vim/vm/GuestInfo/StackInfo.rst>`_], optional):

       Guest information about IP networking stack, if known.
    disk ([`vim.vm.GuestInfo.DiskInfo <vim/vm/GuestInfo/DiskInfo.rst>`_], optional):

       Guest information about disks.You can obtain Linux guest disk information for the following file system types only: Ext2, Ext3, Ext4, ReiserFS, ZFS, NTFS, VFAT, UFS, PCFS, HFS, and MS-DOS.
    screen (`vim.vm.GuestInfo.ScreenInfo <vim/vm/GuestInfo/ScreenInfo.rst>`_, optional):

       Guest screen resolution info, if known.
    guestState (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       Operation mode of guest operating system. One of:
        * "running" - Guest is running normally.
        * "shuttingdown" - Guest has a pending shutdown command.
        * "resetting" - Guest has a pending reset command.
        * "standby" - Guest has a pending standby command.
        * "notrunning" - Guest is not running.
        * "unknown" - Guest information is not available.
        * 
    appHeartbeatStatus (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Application heartbeat status. Please see `VirtualMachineAppHeartbeatStatusType <vim/VirtualMachine/AppHeartbeatStatusType.rst>`_ 
    appState (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Application state. If vSphere HA is enabled and the vm is configured for Application Monitoring and this field's value is "appStateNeedReset" then HA will attempt immediately reset the vm. There are some system conditions which may delay the immediate reset. The immediate reset will be performed as soon as allowed by vSphere HA and ESX. If during these conditions the value is changed to appStateOk the reset will be cancelled.See `GuestInfoAppStateType <vim/vm/GuestInfo/AppStateType.rst>`_ 
    guestOperationsReady (`bool <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Guest Operations availability. If true, the vitrual machine is ready to process guest operations.
    interactiveGuestOperationsReady (`bool <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Interactive Guest Operations availability. If true, the vitrual machine is ready to process guest operations as the user interacting with the guest desktop.
    generationInfo ([`vim.vm.GuestInfo.NamespaceGenerationInfo <vim/vm/GuestInfo/NamespaceGenerationInfo.rst>`_, privilege: VirtualMachine.Namespace.EventNotify], optional):

       A list of namespaces and their corresponding generation numbers. Only namespaces with non-zero `maxSizeEventsFromGuest <vim/vm/NamespaceManager/CreateSpec.rst#maxSizeEventsFromGuest>`_ are guaranteed to be present here. Use `ListNamespaces <vim/vm/NamespaceManager.rst#listNamespaces>`_ to retrieve list of namespaces.
