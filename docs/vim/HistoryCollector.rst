
vim.HistoryCollector
====================
  This managed object type enables clients to retrieve historical data and receive updates when the server appends new data to a collection. This is a base type for item-specific types related to event or task history. Historical data is inherently append-only, although a server administrator may periodically purge old data.Typically, a client creates a history collector by using a filter on a potentially large set, such as all the events in a datacenter. The collector provides access to the items that match the filter, which could also be a relatively large set.The items in a collector are always ordered by date and time of creation. Item properties normally include this time stamp.The client may set the "viewable latest page" for the collector, which is the contiguous subset of the items that are of immediate interest. These items are available as the "latestPage" property, which the client may retrieve and monitor by using the `PropertyCollector <vmodl/query/PropertyCollector.rst>`_ managed object.Clients can change the page size of the "latestPage" by using `setLatestPageSize() <vim/HistoryCollector.rst#setLatestPageSize>`_ .The client may use the following features of the history collector.
   * `RewindCollector <vim/HistoryCollector.rst#rewind>`_
   * - Moves the "scrollable view" to the oldest item (the default setting).
   * readNext - Retrieves all the items in the collector, from the oldest item to the newest item. Retrieves either
   * `tasks <vim/TaskHistoryCollector.rst#readNext>`_
   * or
   * `events <vim/event/EventHistoryCollector.rst#readNext>`_
   * depending on the operation.
   * readPrev - Retrieves all items (excluding the "viewable latest page") in the collector, from the newest item to the oldest item. Retrieves either
   * `tasks <vim/TaskHistoryCollector.rst#readPrev>`_
   * or
   * `events <vim/event/EventHistoryCollector.rst#readPrev>`_
   * depending on the operation.
   * `ResetCollector <vim/HistoryCollector.rst#reset>`_
   * - Moves the "scrollable view" to the item immediately preceding the "viewable latest page".
   * 




Attributes
----------
    filter (`object <https://docs.python.org/2/library/stdtypes.html>`_):
       The filter used to create this collector.The type of the returned filter is determined by the managed object for which the collector is created.


Methods
-------


SetCollectorPageSize(maxCount):
   Sets the "viewable latest page" size to contain at most the number of items specified by the maxCount parameter).


  Privilege:



  Args:
    maxCount (`int <https://docs.python.org/2/library/stdtypes.html>`_):
       The maximum number of items in the page.




  Returns:
    None
         

  Raises:

    `vmodl.fault.InvalidArgument <vmodl/fault/InvalidArgument.rst>`_: 
       if maxCount is out of range.


RewindCollector():
   Moves the "scrollable view" to the oldest item. If you use `ReadNextTasks <vim/TaskHistoryCollector.rst#readNext>`_ or `ReadNextEvents <vim/event/EventHistoryCollector.rst#readNext>`_ , all items are retrieved from the oldest item to the newest item. This is the default setting when the collector is created.


  Privilege:



  Args:


  Returns:
    None
         


ResetCollector():
   Moves the "scrollable view" to the item immediately preceding the "viewable latest page". If you use "readPrev", `ReadPreviousTasks <vim/TaskHistoryCollector.rst#readPrev>`_ or `ReadPreviousEvents <vim/event/EventHistoryCollector.rst#readPrev>`_ , all items are retrieved from the newest item to the oldest item.


  Privilege:



  Args:


  Returns:
    None
         


DestroyCollector():
   Destroys this collector.


  Privilege:



  Args:


  Returns:
    None
         


