
vim.event.CustomFieldValueChangedEvent
======================================
  This event records a change to a custom field value for a particular entity.
:extends: vim.event.CustomFieldEvent_

Attributes:
    entity (`vim.event.ManagedEntityEventArgument <vim/event/ManagedEntityEventArgument.rst>`_):

       The entity on which the field value was changed.
    fieldKey (`int <https://docs.python.org/2/library/stdtypes.html>`_):

       The custom field whose value was changed for the entity.
    name (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       The name of the custom field at the time the value was changed.
    value (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       The new value that was set.
