
vim.alarm.MetricAlarmExpression
===============================
  An alarm expression that uses a metric as the condition that triggers an alarm. Base type.There are two alarm operands: yellow and red. At least one of them must be set. The value of the alarm expression is determined as follows:
   * If the host is not connected, the host metric expression is gray.
   * If the vm is not connected, the vm metric expression is gray.
   * If red is set but yellow is not, the expression is red when the metric is over (isAbove operator) or under (isBelow operator) the red value. Otherwise, the expression is green.
   * If yellow is set but red is not, the expression is yellow when the metric is over (isAbove) or under (isBelow) the yellow value. Otherwise, the expression is green.
   * If both yellow and red are set, the value of the expression is red when the metric is over (isAbove) or under (isBelow) the red value. Otherwise, the expression is yellow when the metric is over (isAbove) or under (isBelow) the yellow value. Otherwise, the expression is green.
   * 
:extends: vim.alarm.AlarmExpression_

Attributes:
    operator (`vim.alarm.MetricAlarmExpression.MetricOperator <vim/alarm/MetricAlarmExpression/MetricOperator.rst>`_):

       The operation to be tested on the metric.
    type (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       Name of the object type containing the property.
    metric (`vim.PerformanceManager.MetricId <vim/PerformanceManager/MetricId.rst>`_):

       The instance of the metric.
    yellow (`int <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Whether or not to test for a yellow condition. If not set, do not calculate yellow status. If set, it contains the threshold value that triggers yellow status.
    yellowInterval (`int <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Time interval in seconds for which the yellow condition must be true before the yellow status is triggered. If unset, the yellow status is triggered immediately when the yellow condition becomes true.
    red (`int <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Whether or not to test for a red condition. If not set, do not calculate red status. If set, it contains the threshold value that triggers red status.
    redInterval (`int <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Time interval in seconds for which the red condition must be true before the red status is triggered. If unset, the red status is triggered immediately when the red condition becomes true.
