
vim.alarm.OrAlarmExpression
===========================
  A data object type that links multiple alarm expressions with OR operators.
:extends: vim.alarm.AlarmExpression_

Attributes:
    expression ([`vim.alarm.AlarmExpression <vim/alarm/AlarmExpression.rst>`_]):

       List of alarm expressions that define the overall status of the alarm.
        * The state of the alarm expression is gray if all subexpressions are gray. Otherwise, gray subexpressions are ignored.
        * The state is red if any subexpression is red.
        * Otherwise, the state is yellow if any subexpression is yellow.
        * Otherwise, the state of the alarm expression is green.
        * 
