.. _str: https://docs.python.org/2/library/stdtypes.html

.. _vmodl.DynamicData: ../../../vmodl/DynamicData.rst

.. _vim.vm.GuestInfo.ToolsStatus: ../../../vim/vm/GuestInfo/ToolsStatus.rst


vim.vm.Summary.GuestSummary
===========================
  A subset of virtual machine guest information.
:extends: vmodl.DynamicData_

Attributes:
    guestId (`str`_, optional):

       Guest operating system identifier (short name), if known.
    guestFullName (`str`_, optional):

       Guest operating system name configured on the virtual machine.
    toolsStatus (`vim.vm.GuestInfo.ToolsStatus`_, optional):

       Current status of VMware Tools in the guest operating system, if known.
    toolsVersionStatus (`str`_, optional):

       Current version status of VMware Tools in the guest operating system, if known.
    toolsVersionStatus2 (`str`_, optional):

       Current version status of VMware Tools in the guest operating system, if known.
    toolsRunningStatus (`str`_, optional):

       Current running status of VMware Tools in the guest operating system, if known.
    hostName (`str`_, optional):

       Hostname of the guest operating system, if known.
    ipAddress (`str`_, optional):

       Primary IP address assigned to the guest operating system, if known.
