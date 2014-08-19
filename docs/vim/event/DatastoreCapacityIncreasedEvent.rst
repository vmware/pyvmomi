
vim.event.DatastoreCapacityIncreasedEvent
=========================================
  This event records when increase in a datastore's capacity is observed. It may happen due to different reasons, like extending or expanding a datastore.
:extends: vim.event.DatastoreEvent_
:since: `vSphere API 4.0 <vim/version.rst#vimversionversion5>`_

Attributes:
    oldCapacity (`long <https://docs.python.org/2/library/stdtypes.html>`_):

       The old datastore capacity.
    newCapacity (`long <https://docs.python.org/2/library/stdtypes.html>`_):

       The new datastore capacity.
