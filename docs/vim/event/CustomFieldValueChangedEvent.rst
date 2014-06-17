.. _int: https://docs.python.org/2/library/stdtypes.html

.. _str: https://docs.python.org/2/library/stdtypes.html

.. _vim.event.CustomFieldEvent: ../../vim/event/CustomFieldEvent.rst

.. _vim.event.ManagedEntityEventArgument: ../../vim/event/ManagedEntityEventArgument.rst


vim.event.CustomFieldValueChangedEvent
======================================
  This event records a change to a custom field value for a particular entity.
:extends: vim.event.CustomFieldEvent_

Attributes:
    entity (`vim.event.ManagedEntityEventArgument`_):

       The entity on which the field value was changed.
    fieldKey (`int`_):

       The custom field whose value was changed for the entity.
    name (`str`_):

       The name of the custom field at the time the value was changed.
    value (`str`_):

       The new value that was set.
