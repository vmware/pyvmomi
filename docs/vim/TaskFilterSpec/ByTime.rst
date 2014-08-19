
vim.TaskFilterSpec.ByTime
=========================
  This data object type specifies a time range used to filter task history.
:extends: vmodl.DynamicData_

Attributes:
    timeType (`vim.TaskFilterSpec.TimeOption <vim/TaskFilterSpec/TimeOption.rst>`_):

       The time stamp to filter: queued, started, or completed time.
    beginTime (`datetime <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       The beginning of the time range. If this property is not specified, then tasks are collected from the earliest time in the database.When this property is specified, the time type field must also be specified.
    endTime (`datetime <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       The end of the time range. If this property is not specified, then tasks are collected up to the latest time in the database.When this property is specified, the time type field must also be specified.
