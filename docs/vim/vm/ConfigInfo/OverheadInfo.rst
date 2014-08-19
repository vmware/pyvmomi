
vim.vm.ConfigInfo.OverheadInfo
==============================
  Information about virtualization overhead required to power on the virtual machine on the registered host.
:extends: vmodl.DynamicData_
:since: `vSphere API 5.0 <vim/version.rst#vimversionversion7>`_

Attributes:
    initialMemoryReservation (`long <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Memory overhead required for virtual machine to be powered on (in bytes).
    initialSwapReservation (`long <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Disk space required for virtual machine to be powered on (in bytes). This space is used by virtualization infrastructure to swap out virtual machine process memory. Location of the file is specified by sched.swap.vmxSwapDir virtual machinge advanced config option or in case it is not specified - current virtual machine home directory is being used.
