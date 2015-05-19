.. _long: https://docs.python.org/2/library/stdtypes.html

.. _VI API 2.5: ../../vim/version.rst#vimversionversion2

.. _vim.event.HostEvent: ../../vim/event/HostEvent.rst

.. _vim.event.VmEventArgument: ../../vim/event/VmEventArgument.rst

.. _vim.event.HostEventArgument: ../../vim/event/HostEventArgument.rst


vim.event.HostWwnConflictEvent
==============================
  This event records a conflict of host WWNs (World Wide Name).
:extends: vim.event.HostEvent_
:since: `VI API 2.5`_

Attributes:
    conflictedVms ([`vim.event.VmEventArgument`_], optional):

       The virtual machine whose WWN conflicts with the current host's WWN.
    conflictedHosts ([`vim.event.HostEventArgument`_], optional):

       The host whose physical WWN conflicts with the current host's WWN.
    wwn (`long`_):

       The WWN in conflict.
