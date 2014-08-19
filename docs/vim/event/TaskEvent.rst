
vim.event.TaskEvent
===================
  This event records the creation of a Task. Note that the embedded TaskInfo object is asnapshotof the Task state at the time of its creation, so its state will always be "queued". To find the current status of the task, query for the current state of the Task using the eventChainId in the embedded TaskInfo object.
:extends: vim.event.Event_

Attributes:
    info (`vim.TaskInfo <vim/TaskInfo.rst>`_):

       The information about the task.
