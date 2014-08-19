
vim.Task
========
  A task is used to monitor and potentially cancel long running operations.


:extends: vim.ExtensibleManagedObject_


Attributes
----------
    info (`vim.TaskInfo <vim/TaskInfo.rst>`_):
       Detailed information about this task.


Methods
-------


CancelTask():
   Cancels a running or queued task. A task may only be canceled if it is cancelable. Multiple cancel requests will be treated as a single cancelation request. Canceling a completed or already canceled task will throw an InvalidState exception.If a task is canceled, its runtime state will be set to error and its error state will be set to `RequestCanceled <vmodl/fault/RequestCanceled.rst>`_ .A cancel operation is asynchronous. The operation may return before the task is canceled.


  Privilege:
               Global.CancelTask



  Args:


  Returns:
    None
         

  Raises:

    `vim.fault.InvalidState <vim/fault/InvalidState.rst>`_: 
       If the task is already canceled or completed.

    `vmodl.fault.NotSupported <vmodl/fault/NotSupported.rst>`_: 
       If the task is not cancelable.


UpdateProgress(percentDone):
   Sets percentage done for this task and recalculates overall percentage done. If a percentDone value of less than zero or greater than 100 is specified, a value of zero or 100 respectively is used.
  since: `VI API 2.5 <vim/version.rst#vimversionversion2>`_


  Privilege:
               Task.Update



  Args:
    percentDone (`int <https://docs.python.org/2/library/stdtypes.html>`_):
       Percentage to set for this task




  Returns:
    None
         

  Raises:

    `vim.fault.InvalidState <vim/fault/InvalidState.rst>`_: 
       If task is not running

    `vim.fault.OutOfBounds <vim/fault/OutOfBounds.rst>`_: 
       VirtualCenter 2.x servers throw this fault if percentDone is less than 0 or greater than 100. Newer versions behave as described above, and never throw this fault.


SetTaskState(state, result, fault):
   Sets task state and optionally sets results or fault, as appropriate for state
  since: `VI API 2.5 <vim/version.rst#vimversionversion2>`_


  Privilege:
               Task.Update



  Args:
    state (`vim.TaskInfo.State <vim/TaskInfo/State.rst>`_):
       New state for task


    result (`object <https://docs.python.org/2/library/stdtypes.html>`_, optional):
       Result to set, valid only if task state is TaskInfo.State.success


    fault (`vmodl.MethodFault <vmodl/MethodFault.rst>`_, optional):
       Fault to set, valid only if task state is `error <vim/TaskInfo/State.rst#error>`_ . The fault must be a of a fault type that directly or indirectly extends `VimFault <vim/fault/VimFault.rst>`_ .




  Returns:
    None
         

  Raises:

    `vim.fault.InvalidState <vim/fault/InvalidState.rst>`_: 
       If attempting to change states after task is completed or in error, or attempting to set the result or fault incorrectly


SetTaskDescription(description):
   Updates task description to describe the current phase of the task.
  since: `vSphere API 4.0 <vim/version.rst#vimversionversion5>`_


  Privilege:
               Task.Update



  Args:
    description (`vmodl.LocalizableMessage <vmodl/LocalizableMessage.rst>`_):
       New description for task




  Returns:
    None
         


