.. _str: https://docs.python.org/2/library/stdtypes.html

.. _vSphere API 4.1: ../../vim/version.rst#vimversionversion6

.. _vim.event.VmEvent: ../../vim/event/VmEvent.rst


vim.event.VmAcquiredTicketEvent
===============================
  This event records a user successfully acquiring a ticket
:extends: vim.event.VmEvent_
:since: `vSphere API 4.1`_

Attributes:
    ticketType (`str`_):

       The type of the ticketSee VirtualMachine.TicketType
