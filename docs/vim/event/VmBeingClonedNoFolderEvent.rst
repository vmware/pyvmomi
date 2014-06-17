.. _str: https://docs.python.org/2/library/stdtypes.html

.. _vSphere API 4.1: ../../vim/version.rst#vimversionversion6

.. _vim.event.VmCloneEvent: ../../vim/event/VmCloneEvent.rst

.. _vim.event.HostEventArgument: ../../vim/event/HostEventArgument.rst


vim.event.VmBeingClonedNoFolderEvent
====================================
  This event records a virtual machine being cloned.
:extends: vim.event.VmCloneEvent_
:since: `vSphere API 4.1`_

Attributes:
    destName (`str`_):

       The name of the destination virtual machine.
    destHost (`vim.event.HostEventArgument`_):

       The destination host to which the virtual machine is being cloned.
