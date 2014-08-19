
vim.alarm.AlarmTriggeringAction.TransitionSpec
==============================================
  Specification indicating which on transitions this action fires. The existence of a Spec indicates that this action fires on transitions from that Spec's startState to finalState.There are only four acceptable {startState, finalState} pairs: {green, yellow}, {yellow, red}, {red, yellow} and {yellow, green}. At least one of these pairs must be specified. Any deviation from the above will render the enclosing AlarmSpec invalid.
:extends: vmodl.DynamicData_
:since: `vSphere API 4.0 <vim/version.rst#vimversionversion5>`_

Attributes:
    startState (`vim.ManagedEntity.Status <vim/ManagedEntity/Status.rst>`_):

       The state from which the alarm must transition for the action to fire. Valid choices are red, yellow and green.
    finalState (`vim.ManagedEntity.Status <vim/ManagedEntity/Status.rst>`_):

       The state to which the alarm must transition for the action to fire. Valid choices are red, yellow, and green.
    repeats (`bool <https://docs.python.org/2/library/stdtypes.html>`_):

       Whether or not the action repeats, as per the actionFrequency defined in the enclosing Alarm.
