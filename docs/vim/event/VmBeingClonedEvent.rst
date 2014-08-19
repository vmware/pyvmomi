
vim.event.VmBeingClonedEvent
============================
  This event records a virtual machine being cloned.
:extends: vim.event.VmCloneEvent_

Attributes:
    destFolder (`vim.event.FolderEventArgument <vim/event/FolderEventArgument.rst>`_):

       The destination folder to which the virtual machine is being cloned.
    destName (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       The name of the destination virtual machine.
    destHost (`vim.event.HostEventArgument <vim/event/HostEventArgument.rst>`_):

       The destination host to which the virtual machine is being cloned.
