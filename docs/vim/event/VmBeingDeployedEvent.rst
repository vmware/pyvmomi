.. _vim.event.VmEvent: ../../vim/event/VmEvent.rst

.. _vim.event.VmEventArgument: ../../vim/event/VmEventArgument.rst


vim.event.VmBeingDeployedEvent
==============================
  This event records a virtual machine being deployed from a template.
:extends: vim.event.VmEvent_

Attributes:
    srcTemplate (`vim.event.VmEventArgument`_):

       The template object from which the virtual machine is being deployed.
