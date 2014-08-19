
vim.event.VmDeployedEvent
=========================
  This event records the completion of a virtual machine deployment operation.
:extends: vim.event.VmEvent_

Attributes:
    srcTemplate (`vim.event.VmEventArgument <vim/event/VmEventArgument.rst>`_):

       The template object from which the virtual machine has been deployed.
