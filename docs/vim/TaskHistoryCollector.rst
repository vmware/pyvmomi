
vim.TaskHistoryCollector
========================
  TaskHistoryCollector provides a mechanism for retrieving historical data and updates when the server appends new tasks.


:extends: vim.HistoryCollector_


Attributes
----------
    latestPage ([`vim.TaskInfo <vim/TaskInfo.rst>`_]):
       The items in the 'viewable latest page'. As new tasks that match the collector's `TaskFilterSpec <vim/TaskFilterSpec.rst>`_ are created, they are added to this page, and the oldest tasks are removed from the collector to keep the size of the page to that allowed by `SetCollectorPageSize <vim/HistoryCollector.rst#setLatestPageSize>`_ .The "oldest task" is the one with the oldest creation time. The tasks in the returned page are unordered.


Methods
-------


ReadNextTasks(maxCount):
   Reads the 'scrollable view' from the current position. The scrollable position is moved to the next newer page after the read. No item is returned when the end of the collector is reached.


  Privilege:



  Args:
    maxCount (`int <https://docs.python.org/2/library/stdtypes.html>`_):
       The maximum number of items in the page.




  Returns:
    [`vim.TaskInfo <vim/TaskInfo.rst>`_]:
         

  Raises:

    `vmodl.fault.InvalidArgument <vmodl/fault/InvalidArgument.rst>`_: 
       if maxCount is out of range.


ReadPreviousTasks(maxCount):
   Reads the 'scrollable view' from the current position. The scrollable position is then moved to the next older page after the read. No item is returned when the head of the collector is reached.


  Privilege:



  Args:
    maxCount (`int <https://docs.python.org/2/library/stdtypes.html>`_):
       The maximum number of items in the page.




  Returns:
    [`vim.TaskInfo <vim/TaskInfo.rst>`_]:
         

  Raises:

    `vmodl.fault.InvalidArgument <vmodl/fault/InvalidArgument.rst>`_: 
       if maxCount is out of range.


