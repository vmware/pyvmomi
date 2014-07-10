.. _bool: https://docs.python.org/2/library/stdtypes.html

.. _vim.action.Action: ../../vim/action/Action.rst

.. _vim.alarm.AlarmAction: ../../vim/alarm/AlarmAction.rst

.. _vim.alarm.AlarmTriggeringAction.TransitionSpec: ../../vim/alarm/AlarmTriggeringAction/TransitionSpec.rst


vim.alarm.AlarmTriggeringAction
===============================
  This data object type describes one or more triggering transitions and an action to be done when an alarm is triggered.There are four triggering transitions; at least one of them must be provided. A gray state is considered the same as a green state, for the purpose of detecting transitions.
:extends: vim.alarm.AlarmAction_

Attributes:
    action (`vim.action.Action`_):

       The action to be done when the alarm is triggered.
    transitionSpecs (`vim.alarm.AlarmTriggeringAction.TransitionSpec`_, optional):

       Indicates on which transitions this action executes and repeats. This is optional only for backwards compatibility.
    green2yellow (`bool`_):

       Flag to specify that the alarm should trigger on a transition from green to yellow.
    yellow2red (`bool`_):

       Flag to specify that the alarm should trigger on a transition from yellow to red.
    red2yellow (`bool`_):

       Flag to specify that the alarm should trigger on a transition from red to yellow.
    yellow2green (`bool`_):

       Flag to specify that the alarm should trigger on a transition from yellow to green.
