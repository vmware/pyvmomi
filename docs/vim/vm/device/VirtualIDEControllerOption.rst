
vim.vm.device.VirtualIDEControllerOption
========================================
  The VirtualIDEControllerOption data object type contains the options for a virtual IDE controller.
:extends: vim.vm.device.VirtualControllerOption_

Attributes:
    numIDEDisks (`vim.option.IntOption <vim/option/IntOption.rst>`_):

       The minimum, maximum, and default number of IDE VirtualDisk instances you can have, at any given time, in the IDE controller. The number is further constrained by the number of available slots in the virtual IDE controller.
    numIDECdroms (`vim.option.IntOption <vim/option/IntOption.rst>`_):

       The minimum, maximum, and default number of IDE VirtualCdrom instances you can have, at any given time, in the IDE controller. The number is further constrained by the number of available slots in the virtual IDE controller.
