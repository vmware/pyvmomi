.. _int: https://docs.python.org/2/library/stdtypes.html

.. _object: https://docs.python.org/2/library/stdtypes.html

.. _vim.Task: ../vim/Task.rst

.. _VI API 2.5: ../vim/version.rst#vimversionversion2

.. _vim.TaskInfo: ../vim/TaskInfo.rst

.. _RequestCanceled: ../vmodl/fault/RequestCanceled.rst

.. _vSphere API 4.0: ../vim/version.rst#vimversionversion5

.. _vmodl.MethodFault: ../vmodl/MethodFault.rst

.. _vim.TaskInfo.State: ../vim/TaskInfo/State.rst

.. _vim.fault.OutOfBounds: ../vim/fault/OutOfBounds.rst

.. _vim.fault.InvalidState: ../vim/fault/InvalidState.rst

.. _vmodl.LocalizableMessage: ../vmodl/LocalizableMessage.rst

.. _vmodl.fault.NotSupported: ../vmodl/fault/NotSupported.rst

.. _vim.ExtensibleManagedObject: ../vim/ExtensibleManagedObject.rst


vim.Task
========
  A task is used to monitor and potentially cancel long running operations.


:extends: vim.ExtensibleManagedObject_


Attributes
----------
    info (`vim.TaskInfo`_):
       Detailed information about this task.


Methods
-------


CancelTask():
   Cancels a running or queued task. A task may only be canceled if it is cancelable. Multiple cancel requests will be treated as a single cancelation request. Canceling a completed or already canceled task will throw an InvalidState exception.If a task is canceled, its runtime state will be set to error and its error state will be set to `RequestCanceled`_ .A cancel operation is asynchronous. The operation may return before the task is canceled.


  Privilege:
               Global.CancelTask



  Args:


  Returns:
    None
         

  Raises:

    `vim.fault.InvalidState`_: 
       If the task is already canceled or completed.

    `vmodl.fault.NotSupported`_: 
       If the task is not cancelable.


UpdateProgress(percentDone):
   Sets percentage done for this task and recalculates overall percentage done. If a percentDone value of less than zero or greater than 100 is specified, a value of zero or 100 respectively is used.
  since: `VI API 2.5`_


  Privilege:
               Task.Update



  Args:
    percentDone (`int`_):
       Percentage to set for this task




  Returns:
    None
         

  Raises:

    `vim.fault.InvalidState`_: 
       If task is not running

    `vim.fault.OutOfBounds`_: 
       VirtualCenter 2.x servers throw this fault if percentDone is less than 0 or greater than 100. Newer versions behave as described above, and never throw this fault.


SetTaskState(state, result, fault):
   Sets task state and optionally sets results or fault, as appropriate for state
  since: `VI API 2.5`_


  Privilege:
               Task.Update



  Args:
    state (`vim.TaskInfo.State`_):
       New state for task


    result (`object`_, optional):
       Result to set, valid only if task state is TaskInfo.State.success


    fault (`vmodl.MethodFault`_, optional):
       Fault to set, valid only if task state is `error`_ . The fault must be a of a fault type that directly or indirectly extends `VimFault`_ .




  Returns:
    None
         

  Raises:

    `vim.fault.InvalidState`_: 
       If attempting to change states after task is completed or in error, or attempting to set the result or fault incorrectly


SetTaskDescription(description):
   Updates task description to describe the current phase of the task.
  since: `vSphere API 4.0`_


  Privilege:
               Task.Update



  Args:
    description (`vmodl.LocalizableMessage`_):
       New description for task




  Returns:
    None
         


