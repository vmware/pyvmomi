.. _vim.option.IntOption: ../../../vim/option/IntOption.rst

.. _vim.vm.device.VirtualControllerOption: ../../../vim/vm/device/VirtualControllerOption.rst


vim.vm.device.VirtualSIOControllerOption
========================================
  The VirtualSIOControllerOption data object type contains the options for a virtual Super IO Controller.
:extends: vim.vm.device.VirtualControllerOption_

Attributes:
    numFloppyDrives (`vim.option.IntOption`_):

       Three properties (numFloppyDrives.min, numFloppyDrives.max, and numFloppyDrives.defaultValue) define the minimum, maximum, and default number of floppy drives you can have at any given time in the Super IO Controller. This is further constrained by the number of available slots in the Super IO Controller.
    numSerialPorts (`vim.option.IntOption`_):

       Three properties (numSerialPorts.min, numSerialPorts.max, and numSerialPorts.defaultValue) define the minimum, maximum, and default number of serial ports you can have at any given time in the Super IO Controller. This is further constrained by the number of available slots in the Super IO Controller.
    numParallelPorts (`vim.option.IntOption`_):

       Three properties (numParallelPorts.min, numParallelPorts.max, and numParallelPorts.defaultValue) define the minimum, maximum, and default number of parallel ports you can have at any given time in the Super IO controller. This is further constrained by the number of available slots in the Super IO Controller.
