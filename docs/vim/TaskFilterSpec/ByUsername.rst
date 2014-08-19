
vim.TaskFilterSpec.ByUsername
=============================
  This data object type enables you to filter task history according to the users who performed the tasks.
:extends: vmodl.DynamicData_

Attributes:
    systemUser (`bool <https://docs.python.org/2/library/stdtypes.html>`_):

       Whether or not to filter by system user. If set to true, filters for system user event.
    userList ([`str <https://docs.python.org/2/library/stdtypes.html>`_], optional):

       Specifies the username list to use in the filter. If not set, then all regular user tasks are collected.
