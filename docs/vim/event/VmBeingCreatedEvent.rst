
vim.event.VmBeingCreatedEvent
=============================
  This event records a virtual machine being created.
:extends: vim.event.VmEvent_

Attributes:
    configSpec (`vim.vm.ConfigSpec <vim/vm/ConfigSpec.rst>`_, optional):

       The configuration specification that was used to create this virtual machine.
