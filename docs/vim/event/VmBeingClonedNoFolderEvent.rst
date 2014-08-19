
vim.event.VmBeingClonedNoFolderEvent
====================================
  This event records a virtual machine being cloned.
:extends: vim.event.VmCloneEvent_
:since: `vSphere API 4.1 <vim/version.rst#vimversionversion6>`_

Attributes:
    destName (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       The name of the destination virtual machine.
    destHost (`vim.event.HostEventArgument <vim/event/HostEventArgument.rst>`_):

       The destination host to which the virtual machine is being cloned.
