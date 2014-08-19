
vim.event.VmBeingDeployedEvent
==============================
  This event records a virtual machine being deployed from a template.
:extends: vim.event.VmEvent_

Attributes:
    srcTemplate (`vim.event.VmEventArgument <vim/event/VmEventArgument.rst>`_):

       The template object from which the virtual machine is being deployed.
