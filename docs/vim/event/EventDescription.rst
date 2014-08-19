
vim.event.EventDescription
==========================
  This data object provides static, locale-specific strings for event objects.
:extends: vmodl.DynamicData_

Attributes:
    category ([`vim.ElementDescription <vim/ElementDescription.rst>`_]):

        `Event Category enum <vim/event/EventDescription/EventCategory.rst>`_ 
    eventInfo ([`vim.event.EventDescription.EventDetail <vim/event/EventDescription/EventDetail.rst>`_]):

       The event class description details.
    enumeratedTypes ([`vim.EnumDescription <vim/EnumDescription.rst>`_], optional):

       Localized descriptions of all enumerated types that are used for member declarations in event classes.
