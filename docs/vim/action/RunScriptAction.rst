.. _str: https://docs.python.org/2/library/stdtypes.html

.. _ActionParameter: ../../vim/action/Action/ActionParameter.rst

.. _vim.action.Action: ../../vim/action/Action.rst


vim.action.RunScriptAction
==========================
  This data object type specifies a script that is triggered by an alarm. You can use any elements of the `ActionParameter`_ enumerated list as part of your script to provide information available at runtime.
:extends: vim.action.Action_

Attributes:
    script (`str`_):

       The fully-qualified path to a shell script that runs on the VirtualCenter server as a result of an alarm.
