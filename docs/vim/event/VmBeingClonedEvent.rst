.. _str: https://docs.python.org/2/library/stdtypes.html

.. _vim.event.VmCloneEvent: ../../vim/event/VmCloneEvent.rst

.. _vim.event.HostEventArgument: ../../vim/event/HostEventArgument.rst

.. _vim.event.FolderEventArgument: ../../vim/event/FolderEventArgument.rst


vim.event.VmBeingClonedEvent
============================
  This event records a virtual machine being cloned.
:extends: vim.event.VmCloneEvent_

Attributes:
    destFolder (`vim.event.FolderEventArgument`_):

       The destination folder to which the virtual machine is being cloned.
    destName (`str`_):

       The name of the destination virtual machine.
    destHost (`vim.event.HostEventArgument`_):

       The destination host to which the virtual machine is being cloned.
