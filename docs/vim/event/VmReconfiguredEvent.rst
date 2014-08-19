
vim.event.VmReconfiguredEvent
=============================
  This event records a reconfiguration of the virtual machine.
:extends: vim.event.VmEvent_

Attributes:
    configSpec (`vim.vm.ConfigSpec <vim/vm/ConfigSpec.rst>`_):

       The configuration specification that was used for the reconfiguration.
