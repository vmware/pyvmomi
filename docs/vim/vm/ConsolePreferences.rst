
vim.vm.ConsolePreferences
=========================
  Preferences for the legacy console application that affect the way it behaves during power operations on the virtual machine.
:extends: vmodl.DynamicData_

Attributes:
    powerOnWhenOpened (`bool <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Power on the virtual machine when it is opened in the console.
    enterFullScreenOnPowerOn (`bool <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Enter full screen mode when this virtual machine is powered on.
    closeOnPowerOffOrSuspend (`bool <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Close the console application when the virtual machine is powered off or suspended.
