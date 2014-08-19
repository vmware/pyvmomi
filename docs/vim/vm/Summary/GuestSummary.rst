
vim.vm.Summary.GuestSummary
===========================
  A subset of virtual machine guest information.
:extends: vmodl.DynamicData_

Attributes:
    guestId (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Guest operating system identifier (short name), if known.
    guestFullName (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Guest operating system name configured on the virtual machine.
    toolsStatus (`vim.vm.GuestInfo.ToolsStatus <vim/vm/GuestInfo/ToolsStatus.rst>`_, optional):

       Current status of VMware Tools in the guest operating system, if known.
    toolsVersionStatus (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Current version status of VMware Tools in the guest operating system, if known.
    toolsVersionStatus2 (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Current version status of VMware Tools in the guest operating system, if known.
    toolsRunningStatus (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Current running status of VMware Tools in the guest operating system, if known.
    hostName (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Hostname of the guest operating system, if known.
    ipAddress (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Primary IP address assigned to the guest operating system, if known.
