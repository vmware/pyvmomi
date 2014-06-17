.. _vim.event.VmEvent: ../../vim/event/VmEvent.rst

.. _vim.vm.ConfigSpec: ../../vim/vm/ConfigSpec.rst


vim.event.VmBeingCreatedEvent
=============================
  This event records a virtual machine being created.
:extends: vim.event.VmEvent_

Attributes:
    configSpec (`vim.vm.ConfigSpec`_, optional):

       The configuration specification that was used to create this virtual machine.
