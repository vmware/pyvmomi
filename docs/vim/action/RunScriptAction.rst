
vim.action.RunScriptAction
==========================
  This data object type specifies a script that is triggered by an alarm. You can use any elements of the `ActionParameter <vim/action/Action/ActionParameter.rst>`_ enumerated list as part of your script to provide information available at runtime.
:extends: vim.action.Action_

Attributes:
    script (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       The fully-qualified path to a shell script that runs on the VirtualCenter server as a result of an alarm.
