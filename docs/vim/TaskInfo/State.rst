vim.TaskInfo.State
==================
  List of possible states of a task.
  :contained by: `vim.TaskInfo <vim/TaskInfo.rst>`_

  :type: `vim.TaskInfo.State <vim/TaskInfo/State.rst>`_

  :name: error

values:
--------

running
   When the busy thread is freed from its current task by finishing the task, it picks a queued task to run. Then the queued tasks are marked as running.

queued
   When there are too many tasks for threads to handle.

success
   When a running task has completed.

error
   When a running task has encountered an error.
