.. _int: https://docs.python.org/2/library/stdtypes.html

.. _str: https://docs.python.org/2/library/stdtypes.html

.. _bool: https://docs.python.org/2/library/stdtypes.html

.. _UpgradePolicy: ../../vim/vm/ToolsConfigInfo/UpgradePolicy.rst

.. _vmodl.DynamicData: ../../vmodl/DynamicData.rst

.. _vim.vm.ToolsConfigInfo.ToolsLastInstallInfo: ../../vim/vm/ToolsConfigInfo/ToolsLastInstallInfo.rst


vim.vm.ToolsConfigInfo
======================
  ToolsConfigInfo is a data object type containing settings for the VMware Tools software running in the guest operating system.
:extends: vmodl.DynamicData_

Attributes:
    toolsVersion (`int`_, optional):

       Version of VMware Tools installed on the guest operating system.
    afterPowerOn (`bool`_, optional):

       Flag to specify whether or not scripts should run after the virtual machine powers on.
    afterResume (`bool`_, optional):

       Flag to specify whether or not scripts should run after the virtual machine resumes.
    beforeGuestStandby (`bool`_, optional):

       Flag to specify whether or not scripts should run before the virtual machine suspends.
    beforeGuestShutdown (`bool`_, optional):

       Flag to specify whether or not scripts should run before the virtual machine powers off.
    beforeGuestReboot (`bool`_, optional):

       Flag to specify whether or not scripts should run before the virtual machine reboots.
    toolsUpgradePolicy (`str`_, optional):

       Tools upgrade policy setting for the virtual machine.See `UpgradePolicy`_ 
    pendingCustomization (`str`_, optional):

       When set, this indicates that a customization operation is pending on the VM. The value represents the filename of the customization package on the host.
    syncTimeWithHost (`bool`_, optional):

       Indicates whether or not the tools program will sync time with the host time.
    lastInstallInfo (`vim.vm.ToolsConfigInfo.ToolsLastInstallInfo`_, optional):

       Information about the last tools upgrade attempt if applicable. This information is maintained by the server and is ignored if set by the client.
