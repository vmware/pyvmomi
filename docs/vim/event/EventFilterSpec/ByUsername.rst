.. _str: https://docs.python.org/2/library/stdtypes.html

.. _bool: https://docs.python.org/2/library/stdtypes.html

.. _vmodl.DynamicData: ../../../vmodl/DynamicData.rst


vim.event.EventFilterSpec.ByUsername
====================================
  This option specifies users used to filter event history.
:extends: vmodl.DynamicData_

Attributes:
    systemUser (`bool`_):

       filter by system user true for system user event
    userList (`str`_, optional):

       all interested username list If this property is not set, then all regular user events are collected
