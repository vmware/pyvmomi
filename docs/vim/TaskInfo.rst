.. _int: https://docs.python.org/2/library/stdtypes.html

.. _str: https://docs.python.org/2/library/stdtypes.html

.. _bool: https://docs.python.org/2/library/stdtypes.html

.. _object: https://docs.python.org/2/library/stdtypes.html

.. _vim.Task: ../vim/Task.rst

.. _datetime: https://docs.python.org/2/library/stdtypes.html

.. _vim.TaskReason: ../vim/TaskReason.rst

.. _vim.ManagedEntity: ../vim/ManagedEntity.rst

.. _vmodl.DynamicData: ../vmodl/DynamicData.rst

.. _vim.TaskInfo.State: ../vim/TaskInfo/State.rst

.. _vmodl.LocalizableMessage: ../vmodl/LocalizableMessage.rst

.. _vmodl.LocalizedMethodFault: ../vmodl/LocalizedMethodFault.rst


vim.TaskInfo
============
  This data object type contains all information about a task. A task represents an operation performed by VirtualCenter or ESX.
:extends: vmodl.DynamicData_

Attributes:
    key (`str`_):

       The unique key for the task.
    task (`vim.Task`_):

       The managed object that represents this task.
    description (`vmodl.LocalizableMessage`_, optional):

       The description field of the task describes the current phase of operation of the task. For a task that does a single monolithic activity, this will be fixed and unchanging. For tasks that have various substeps, this field will change as the task progresses from one phase to another.
    name (`str`_, optional):

       The name of the operation that created the task. This is not set for internal tasks.
    descriptionId (`str`_):

       An identifier for this operation. This includes publicly visible internal tasks and is a lookup in the TaskDescription methodInfo data object.
    entity (`vim.ManagedEntity`_, optional):

       Managed entity to which the operation applies.
    entityName (`str`_, optional):

       The name of the managed entity, locale-specific, retained for the history collector database.
    locked (`vim.ManagedEntity`_, optional):

       If the state of the task is "running", then this property is a list of managed entities that the operation has locked, with a shared lock.
    state (`vim.TaskInfo.State`_):

       Runtime status of the task.
    cancelled (`bool`_):

       Flag to indicate whether or not the client requested cancellation of the task.
    cancelable (`bool`_):

       Flag to indicate whether or not the cancel task operation is supported.
    error (`vmodl.LocalizedMethodFault`_, optional):

       If the task state is "error", then this property contains the fault code.
    result (`object`_, optional):

       If the task state is "success", then this property may be used to hold a return value.
    progress (`int`_, optional):

       If the task state is "running", then this property contains a progress measurement, expressed as percentage completed, from 0 to 100.If this property is not set, then the command does not report progress.
    reason (`vim.TaskReason`_):

       Kind of entity responsible for creating this task.
    queueTime (`datetime`_):

       Time stamp when the task was created.
    startTime (`datetime`_, optional):

       Time stamp when the task started running.
    completeTime (`datetime`_, optional):

       Time stamp when the task was completed (whether success or failure).
    eventChainId (`int`_):

       Event chain ID that leads to the corresponding events.
    changeTag (`str`_, optional):

       The user entered tag to identify the operations and their side effects
    parentTaskKey (`str`_, optional):

       Tasks can be cretaed by another task. This shows `key`_ of the task spun off this task. This is to track causality between tasks.
    rootTaskKey (`str`_, optional):

       Tasks can be cretaed by another task and such creation can go on for multiple levels. This is the `key`_ of the task that started the chain of tasks.
