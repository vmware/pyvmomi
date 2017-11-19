.. _long: https://docs.python.org/2/library/stdtypes.html

.. _bool: https://docs.python.org/2/library/stdtypes.html

.. _VI API 2.5: ../../vim/version.rst#vimversionversion2

.. _bootRetryDelay: ../../vim/vm/BootOptions.rst#bootRetryDelay

.. _bootRetryEnabled: ../../vim/vm/BootOptions.rst#bootRetryEnabled

.. _vmodl.DynamicData: ../../vmodl/DynamicData.rst

.. _VirtualMachineBootOptions: ../../vim/vm/BootOptions.rst

.. _vim.vm.BootOptions.BootableDevice: ../../vim/vm/BootOptions/BootableDevice.rst


vim.vm.BootOptions
==================
  The `VirtualMachineBootOptions`_ data object defines the boot-time behavior of a virtual machine.You can use the delay options to specify a time interval during which you can enter the virtual machine BIOS setup. These options provide a solution for the situation that occurs when the console attaches to the virtual machine after the boot sequence has passed the BIOS setup entry point.
:extends: vmodl.DynamicData_
:since: `VI API 2.5`_

Attributes:
    bootDelay (`long`_, optional):

       Delay in milliseconds before starting the boot sequence. The boot delay specifies a time interval between virtual machine power on or restart and the beginning of the boot sequence.
    enterBIOSSetup (`bool`_, optional):

       If set to true, the virtual machine automatically enters BIOS setup the next time it boots. The virtual machine resets this flag tofalseso that subsequent boots proceed normally.
    bootRetryEnabled (`bool`_, optional):

       If set to true, a virtual machine that fails to boot will try again after the `bootRetryDelay`_ time period has expired. Whenfalse, the virtual machine waits indefinitely for you to initiate boot retry.
    bootRetryDelay (`long`_, optional):

       Delay in milliseconds before a boot retry. The boot retry delay specifies a time interval between virtual machine boot failure and the subsequent attempt to boot again. The virtual machine uses this value only if `bootRetryEnabled`_ is true.
    bootOrder ([`vim.vm.BootOptions.BootableDevice`_], optional):

       Boot order. Listed devices are used for booting. After list is exhausted, default BIOS boot device algorithm is used for booting. Note that order of the entries in the list is important: device listed first is used for boot first, if that one fails second entry is used, and so on. Platform may have some internal limit on the number of devices it supports. If bootable device is not reached before platform's limit is hit, boot will fail. At least single entry is supported by all products supporting boot order settings.
