vim.PerformanceManager.CounterInfo.StatsType
============================================
  Indicates the type of statistical measurement that a counters value represents. Valid types areabsolute,delta, orrate.
  :contained by: `vim.PerformanceManager.CounterInfo <vim/PerformanceManager/CounterInfo.rst>`_

  :type: `vim.PerformanceManager.CounterInfo.StatsType <vim/PerformanceManager/CounterInfo/StatsType.rst>`_

  :name: rate

values:
--------

rate
   Represents a value that has been normalized over the `samplingPeriod <vim/HistoricalInterval.rst#samplingPeriod>`_ , enabling values for the same counter type to be compared, regardless of interval. For example, the number of reads per second.

delta
   Represents an amount of change for the counter during the `samplingPeriod <vim/HistoricalInterval.rst#samplingPeriod>`_ as compared to the previous `interval <vim/HistoricalInterval.rst>`_ . The first sampling interval

absolute
   Represents an actual value, level, or state of the counter. For example, theuptimecounter (systemgroup) represents the actual number of seconds since startup. Thecapacitycounter represents the actual configured size of the specified datastore. In other words, number of samples, samplingPeriod, and intervals have no bearing on anabsolutecounters value.
