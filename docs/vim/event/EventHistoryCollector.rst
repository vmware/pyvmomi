
vim.event.EventHistoryCollector
===============================
  EventHistoryCollector provides a mechanism for retrieving historical data and updates when the server appends new events.


:extends: vim.HistoryCollector_


Attributes
----------
    latestPage ([`vim.event.Event <vim/event/Event.rst>`_]):
       The items in the 'viewable latest page'. As new events that match the collector's `EventFilterSpec <vim/event/EventFilterSpec.rst>`_ are created, they are added to this page, and the oldest events are removed from the collector to keep the size of the page to that allowed by HistoryCollector#setLatestPageSize.The "oldest event" is the one with the smallest key (event ID). The events in the returned page are unordered.


Methods
-------


ReadNextEvents(maxCount):
   Reads the 'scrollable view' from the current position. The scrollable position is moved to the next newer page after the read. No item is returned when the end of the collector is reached.


  Privilege:



  Args:
    maxCount (`int <https://docs.python.org/2/library/stdtypes.html>`_):
       The maximum number of items in the page.




  Returns:
    [`vim.event.Event <vim/event/Event.rst>`_]:
         

  Raises:

    `vmodl.fault.InvalidArgument <vmodl/fault/InvalidArgument.rst>`_: 
       if maxCount is out of range.


ReadPreviousEvents(maxCount):
   Reads the 'scrollable view' from the current position. The scrollable position is moved to the next older page after the read. No item is returned when the head of the collector is reached.


  Privilege:



  Args:
    maxCount (`int <https://docs.python.org/2/library/stdtypes.html>`_):
       The maximum number of items in the page.




  Returns:
    [`vim.event.Event <vim/event/Event.rst>`_]:
         

  Raises:

    `vmodl.fault.InvalidArgument <vmodl/fault/InvalidArgument.rst>`_: 
       if maxCount is out of range.


