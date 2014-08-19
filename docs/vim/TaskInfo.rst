
vim.TaskInfo
============
  This data object type contains all information about a task. A task represents an operation performed by VirtualCenter or ESX.
:extends: vmodl.DynamicData_

Attributes:
    key (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       The unique key for the task.
    task (`vim.Task <vim/Task.rst>`_):

       The managed object that represents this task.
    description (`vmodl.LocalizableMessage <vmodl/LocalizableMessage.rst>`_, optional):

       The description field of the task describes the current phase of operation of the task. For a task that does a single monolithic activity, this will be fixed and unchanging. For tasks that have various substeps, this field will change as the task progresses from one phase to another.
    name (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       The name of the operation that created the task. This is not set for internal tasks.
    descriptionId (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       An identifier for this operation. This includes publicly visible internal tasks and is a lookup in the TaskDescription methodInfo data object.
    entity (`vim.ManagedEntity <vim/ManagedEntity.rst>`_, optional):

       Managed entity to which the operation applies.
    entityName (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       The name of the managed entity, locale-specific, retained for the history collector database.
    locked ([`vim.ManagedEntity <vim/ManagedEntity.rst>`_], optional):

       If the state of the task is "running", then this property is a list of managed entities that the operation has locked, with a shared lock.
    state (`vim.TaskInfo.State <vim/TaskInfo/State.rst>`_):

       Runtime status of the task.
    cancelled (`bool <https://docs.python.org/2/library/stdtypes.html>`_):

       Flag to indicate whether or not the client requested cancellation of the task.
    cancelable (`bool <https://docs.python.org/2/library/stdtypes.html>`_):

       Flag to indicate whether or not the cancel task operation is supported.
    error (`vmodl.LocalizedMethodFault <vmodl/LocalizedMethodFault.rst>`_, optional):

       If the task state is "error", then this property contains the fault code.
    result (`object <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       If the task state is "success", then this property may be used to hold a return value.
    progress (`int <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       If the task state is "running", then this property contains a progress measurement, expressed as percentage completed, from 0 to 100.If this property is not set, then the command does not report progress.
    reason (`vim.TaskReason <vim/TaskReason.rst>`_):

       Kind of entity responsible for creating this task.
    queueTime (`datetime <https://docs.python.org/2/library/stdtypes.html>`_):

       Time stamp when the task was created.
    startTime (`datetime <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Time stamp when the task started running.
    completeTime (`datetime <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Time stamp when the task was completed (whether success or failure).
    eventChainId (`int <https://docs.python.org/2/library/stdtypes.html>`_):

       Event chain ID that leads to the corresponding events.
    changeTag (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       The user entered tag to identify the operations and their side effects
    parentTaskKey (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Tasks can be cretaed by another task. This shows `key <vim/TaskInfo.rst#key>`_ of the task spun off this task. This is to track causality between tasks.
    rootTaskKey (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Tasks can be cretaed by another task and such creation can go on for multiple levels. This is the `key <vim/TaskInfo.rst#key>`_ of the task that started the chain of tasks.
