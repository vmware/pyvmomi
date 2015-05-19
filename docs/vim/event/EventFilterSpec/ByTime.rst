.. _datetime: https://docs.python.org/2/library/stdtypes.html

.. _vmodl.DynamicData: ../../../vmodl/DynamicData.rst


vim.event.EventFilterSpec.ByTime
================================
  This option specifies a time range used to filter event history.
:extends: vmodl.DynamicData_

Attributes:
    beginTime (`datetime`_, optional):

       The beginning of the time range. If this property is not set, then events are collected from the earliest time in the database.
    endTime (`datetime`_, optional):

       The end of the time range. If this property is not specified, then events are collected up to the latest time in the database.
