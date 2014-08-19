vim.PerformanceManager.CounterInfo.RollupType
=============================================
  Indicates how multiple samples of a specific counter type are transformed into a single statistical value.
  :contained by: `vim.PerformanceManager.CounterInfo <vim/PerformanceManager/CounterInfo.rst>`_

  :type: `vim.PerformanceManager.CounterInfo.RollupType <vim/PerformanceManager/CounterInfo/RollupType.rst>`_

  :name: none

values:
--------

none
   The counter is never rolled up.

average
   The actual value collected or the average of all values collected during the summary period.

maximum
   The maximum value of the performance counter value over the summarization period.

minimum
   The minimum value of the performance counter value over the summarization period.

summation
   The sum of all the values of the performance counter over the summarization period.

latest
   The most recent value of the performance counter over the summarization period.
