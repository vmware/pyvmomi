
vim.TaskFilterSpec
==================
  This data object type defines the specification for the task filter used to query tasks in the history collector database. The client creates a task history collector with a filter specification, then retrieves the tasks from the task history collector.
:extends: vmodl.DynamicData_

Attributes:
    entity (`vim.TaskFilterSpec.ByEntity <vim/TaskFilterSpec/ByEntity.rst>`_, optional):

       The filter specification for retrieving tasks by managed entity. If not provided, then the tasks attached to all managed entities are collected.
    time (`vim.TaskFilterSpec.ByTime <vim/TaskFilterSpec/ByTime.rst>`_, optional):

       The filter specification for retrieving tasks by time. If not provided, then the tasks with any time stamp are collected.
    userName (`vim.TaskFilterSpec.ByUsername <vim/TaskFilterSpec/ByUsername.rst>`_, optional):

       The filter specification for retrieving tasks by user name. If not provided, then the tasks belonging to any user are collected.
    state ([`vim.TaskInfo.State <vim/TaskInfo/State.rst>`_], optional):

       This property, if provided, limits the set of collected tasks by their states. Task states are enumerated in `State <vim/TaskInfo.rst#state>`_ . If not provided, tasks are collected regardless of their state.
    alarm (`vim.alarm.Alarm <vim/alarm/Alarm.rst>`_, optional):

       This property, if provided, limits the set of collected tasks to those associated with the specified alarm. If not provided, tasks are collected regardless of their association with alarms.
    scheduledTask (`vim.scheduler.ScheduledTask <vim/scheduler/ScheduledTask.rst>`_, optional):

       This property, if provided, limits the set of collected tasks to those associated with the specified scheduled task. If not provided, tasks are collected regardless of their association with any scheduled task.
    eventChainId ([`int <https://docs.python.org/2/library/stdtypes.html>`_], optional):

       The filter specification for retrieving tasks by chain ID. If it is set, tasks not with the given `eventChainId <vim/TaskInfo.rst#eventChainId>`_ will be filtered out. If the property is not set, tasks' chain ID is disregarded for filtering purposes.
    tag ([`str <https://docs.python.org/2/library/stdtypes.html>`_], optional):

       The filter specification for retrieving tasks by `tag <vim/TaskInfo.rst#changeTag>`_ . If it is set, tasks not with the given tag(s) will be filtered out. If the property is not set, tasks' tag is disregarded for filtering purposes. If it is set, and includes an empty string, tasks without a tag will be returned.
    parentTaskKey ([`str <https://docs.python.org/2/library/stdtypes.html>`_], optional):

       The filter specification for retrieving tasks by `parentTaskKey <vim/TaskInfo.rst#parentTaskKey>`_ . If it is set, tasks not with the given parentTaskKey(s) will be filtered out. If the property is not set, tasks' parentTaskKey is disregarded for filtering purposes.
    rootTaskKey ([`str <https://docs.python.org/2/library/stdtypes.html>`_], optional):

       The filter specification for retrieving tasks by `rootTaskKey <vim/TaskInfo.rst#rootTaskKey>`_ . If it is set, tasks not with the given rootTaskKey(s) will be filtered out. If the property is not set, tasks' rootTaskKey is disregarded for filtering purposes.
