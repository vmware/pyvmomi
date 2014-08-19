
vim.vm.ToolsConfigInfo
======================
  ToolsConfigInfo is a data object type containing settings for the VMware Tools software running in the guest operating system.
:extends: vmodl.DynamicData_

Attributes:
    toolsVersion (`int <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Version of VMware Tools installed on the guest operating system.
    afterPowerOn (`bool <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Flag to specify whether or not scripts should run after the virtual machine powers on.
    afterResume (`bool <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Flag to specify whether or not scripts should run after the virtual machine resumes.
    beforeGuestStandby (`bool <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Flag to specify whether or not scripts should run before the virtual machine suspends.
    beforeGuestShutdown (`bool <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Flag to specify whether or not scripts should run before the virtual machine powers off.
    beforeGuestReboot (`bool <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Flag to specify whether or not scripts should run before the virtual machine reboots.
    toolsUpgradePolicy (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Tools upgrade policy setting for the virtual machine.See `UpgradePolicy <vim/vm/ToolsConfigInfo/UpgradePolicy.rst>`_ 
    pendingCustomization (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       When set, this indicates that a customization operation is pending on the VM. The value represents the filename of the customization package on the host.
    syncTimeWithHost (`bool <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Indicates whether or not the tools program will sync time with the host time.
    lastInstallInfo (`vim.vm.ToolsConfigInfo.ToolsLastInstallInfo <vim/vm/ToolsConfigInfo/ToolsLastInstallInfo.rst>`_, optional):

       Information about the last tools upgrade attempt if applicable. This information is maintained by the server and is ignored if set by the client.
