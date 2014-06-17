.. _str: https://docs.python.org/2/library/stdtypes.html

.. _vim.alarm.AlarmExpression: ../../vim/alarm/AlarmExpression.rst

.. _vim.alarm.StateAlarmExpression.StateOperator: ../../vim/alarm/StateAlarmExpression/StateOperator.rst


vim.alarm.StateAlarmExpression
==============================
  An alarm expression that uses the running state of either a virtual machine or a host as the condition that triggers the alarm. Base type.There are two alarm operands: yellow and red. At least one of them must be set. The value of the alarm expression is determined as follows:
   * If the red state is set but the yellow state is not: the expression is red when the state operand matches (isEqual operator) or does not match (isUnequal operator) the state of the managed entity. The expression is green otherwise.
   * If yellow is set but red is not: the expression is yellow when the state operand matches (isEqual) or does not match (isUnequal) the state of the managed entity. The expression is green otherwise.
   * If both yellow and red are set, the value of the expression is red when the red state operand matches (isEqual) or does not match (isUnequal) the state of the managed entity. Otherwise, the expression is yellow when the yellow state operand matches (isEqual) or does not match (isUnequal) the state of the managed entity. Otherwise, the expression is green.
   * 
:extends: vim.alarm.AlarmExpression_

Attributes:
    operator (`vim.alarm.StateAlarmExpression.StateOperator`_):

       The operation to be tested on the target state.
    type (`str`_):

       Name of the object type containing the property.
    statePath (`str`_):

       Path of the state property.The supported values:
        * for vim.VirtualMachine type:
        * runtime.powerState or summary.quickStats.guestHeartbeatStatus
        * for vim.HostSystem type: runtime.connectionState
        * 
    yellow (`str`_, optional):

       Whether or not to test for a yellow condition. If this property is not set, do not calculate yellow status.
    red (`str`_, optional):

       Whether or not to test for a red condition. If this property is not set, do not calculate red status.
