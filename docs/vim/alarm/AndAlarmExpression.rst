.. _vim.alarm.AlarmExpression: ../../vim/alarm/AlarmExpression.rst


vim.alarm.AndAlarmExpression
============================
  A data object type that links multiple alarm expressions with AND operators.
:extends: vim.alarm.AlarmExpression_

Attributes:
    expression (`vim.alarm.AlarmExpression`_):

       List of alarm expressions that define the overall status of the alarm.
        * The state of the alarm expression is gray if all subexpressions are gray. Otherwise, gray subexpressions are ignored.
        * The state is red if all subexpressions are red.
        * Otherwise, the state is yellow if all subexpressions are red or yellow.
        * Otherwise, the state of the alarm expression is green.
        * 
