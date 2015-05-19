.. _int: https://docs.python.org/2/library/stdtypes.html

.. _vmodl.DynamicData: ../../../vmodl/DynamicData.rst


vim.host.Summary.QuickStats
===========================
  Basic host statistics.Included in the host statistics are fairness scores. Fairness scores are represented in units with relative values, meaning they are evaluated relative to the scores of other hosts. They should not be thought of as having any particular absolute value. Each fairness unit represents an increment of 0.001 in a fairness score. The further the fairness score diverges from 1, the less fair the allocation. Therefore, a fairness score of 990, representing 0.990, is more fair than a fairness score of 1015, which represents 1.015. This is because 1.015 is further from 1 than 0.990.
:extends: vmodl.DynamicData_

Attributes:
    overallCpuUsage (`int`_, optional):

       Aggregated CPU usage across all cores on the host in MHz. This is only available if the host is connected.
    overallMemoryUsage (`int`_, optional):

       Physical memory usage on the host in MB. This is only available if the host is connected.
    distributedCpuFairness (`int`_, optional):

       The fairness of distributed CPU resource allocation on the host.
    distributedMemoryFairness (`int`_, optional):

       The fairness of distributed memory resource allocation on the host.
    uptime (`int`_, optional):

       The system uptime of the host in seconds.
