
vim.event.EventFilterSpec.ByUsername
====================================
  This option specifies users used to filter event history.
:extends: vmodl.DynamicData_

Attributes:
    systemUser (`bool <https://docs.python.org/2/library/stdtypes.html>`_):

       filter by system user true for system user event
    userList ([`str <https://docs.python.org/2/library/stdtypes.html>`_], optional):

       all interested username list If this property is not set, then all regular user events are collected
