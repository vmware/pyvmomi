
vim.vm.device.VirtualPS2ControllerOption
========================================
  The VirtualPS2ControllerOption data object type contains the options for a virtual PS/2 controller for keyboards and mice. In addition to the options defined in the `VirtualControllerOption <vim/vm/device/VirtualControllerOption.rst>`_ data object type, these options include the number of keyboards and mice.
:extends: vim.vm.device.VirtualControllerOption_

Attributes:
    numKeyboards (`vim.option.IntOption <vim/option/IntOption.rst>`_):

       The minimum, maximum, and default number of keyboards you can have at any given time. This is further constrained by the number of available slots in the PS/2 controller. The minimum, maximum, and default are integers defined by three properties:
        * numKeyBoards.min
        * : the minimum.
        * numKeyBoards.max
        * : the maximum.
        * numKeyBoards.defaultValue
        * : the default number.
        * 
    numPointingDevices (`vim.option.IntOption <vim/option/IntOption.rst>`_):

       The minimum, maximum, and default number of mice you can have at any given time. The number of mice is also limited by the number of available slots in the PS/2 controller. The minimum, maximum, and default are integers defined by three properties:
        * numPointingDevices.min
        * : the minimum.
        * numPointingDevices.max
        * : the maximum.
        * numPointingDevices.defaultValue
        * : the default number.
        * 
