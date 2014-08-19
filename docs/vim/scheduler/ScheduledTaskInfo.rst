
vim.scheduler.ScheduledTaskInfo
===============================
  The scheduled task details.
:extends: vim.scheduler.ScheduledTaskSpec_

Attributes:
    scheduledTask (`vim.scheduler.ScheduledTask <vim/scheduler/ScheduledTask.rst>`_):

       Scheduled task object.
    entity (`vim.ManagedEntity <vim/ManagedEntity.rst>`_):

       The entity on which related events will be logged. If the task is scheduled on a ManagedEntity, this field will also reflect the same ManagedEntity. If task is scheduled on a ManagedObject, this field will have information about the entity on which the events will be logged on behalf of the ManagedObject. ManagedObject itself will be denoted by `taskObject <vim/scheduler/ScheduledTaskInfo.rst#taskObject>`_ 
    lastModifiedTime (`datetime <https://docs.python.org/2/library/stdtypes.html>`_):

       The time the scheduled task is created or modified.
    lastModifiedUser (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       Last user that modified the scheduled task.
    nextRunTime (`datetime <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       The next time the scheduled task will run.
    prevRunTime (`datetime <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       The last time the scheduled task ran.
    state (`vim.TaskInfo.State <vim/TaskInfo/State.rst>`_):

       Scheduled task state.
    error (`vmodl.LocalizedMethodFault <vmodl/LocalizedMethodFault.rst>`_, optional):

       The fault code when the scheduled task state is "error".
    result (`object <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       The operation result when the scheduled task state is "success".
    progress (`int <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       The task progress when the scheduled task state is "running".
    activeTask (`vim.Task <vim/Task.rst>`_, optional):

       The running task instance when the scheduled task state is "running".
    taskObject (`vmodl.ManagedObject <vim.ExtensibleManagedObject.rst>`_):

       The object on which the scheduled task is defined. This field will have information about either the ManagedEntity or the ManagedObject on which the scheduled task is defined.
