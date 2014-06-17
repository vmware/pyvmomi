.. _str: https://docs.python.org/2/library/stdtypes.html

.. _VI API 2.5: ../../vim/version.rst#vimversionversion2

.. _vim.event.HostDasEvent: ../../vim/event/HostDasEvent.rst


vim.event.HostPrimaryAgentNotShortNameEvent
===========================================
  This event records that the primary agent specified is not a short name. The name of the primary agent is usually stored as a short name. You should not normally see this error. Please check the network configurations of your hosts.
:extends: vim.event.HostDasEvent_
:since: `VI API 2.5`_
**deprecated**


Attributes:
    primaryAgent (`str`_):

