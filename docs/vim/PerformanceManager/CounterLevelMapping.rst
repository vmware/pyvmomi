.. _int: https://docs.python.org/2/library/stdtypes.html

.. _vSphere API 4.1: ../../vim/version.rst#vimversionversion6

.. _vmodl.DynamicData: ../../vmodl/DynamicData.rst

.. _PerformanceManagerCounterLevelMapping: ../../vim/PerformanceManager/CounterLevelMapping.rst


vim.PerformanceManager.CounterLevelMapping
==========================================
   `PerformanceManagerCounterLevelMapping`_ class captures the counter and level mapping. Any counter has two aspects: aggregate value or the per-device value. For example, cpu.usage.average on a host is an aggregate counter and cpu.usage.average on pcpus in a host is a per-device counters. There is a need to be able to specify different levels for the two versions. Currently, all per-device stats are collected at level greater than or equal to 3.In order to be able to configure the level of collections for aggregate and per-device counters we have two optional level fields. `PerformanceManagerCounterLevelMapping`_ is used to update the levels for a counter.
:extends: vmodl.DynamicData_
:since: `vSphere API 4.1`_

Attributes:
    counterId (`int`_):

       The counter Id
    aggregateLevel (`int`_, optional):

       Level for the aggregate counter. If not set then the value is not changed when updateCounterLevelMapping is called.
    perDeviceLevel (`int`_, optional):

       Level for the per device counter. If not set then the value is not changed when updateCounterLevelMapping is called.
