.. _str: https://docs.python.org/2/library/stdtypes.html

.. _vSphere API 4.0: ../../../vim/version.rst#vimversionversion5

.. _vmodl.DynamicData: ../../../vmodl/DynamicData.rst

.. _EventAlarmExpression: ../../../vim/alarm/EventAlarmExpression.rst

.. _vim.ElementDescription: ../../../vim/ElementDescription.rst


vim.event.EventDescription.EventArgDesc
=======================================
  Describes an available event argument name for an Event type, which can be used in `EventAlarmExpression`_ .
:extends: vmodl.DynamicData_
:since: `vSphere API 4.0`_

Attributes:
    name (`str`_):

       The name of the argument
    type (`str`_):

       The type of the argument.
    description (`vim.ElementDescription`_, optional):

       The localized description of the event argument. The key holds the localization prefix for the argument, which is decided by the Event type that it is actually declared in, which may be a base type of this event type.
