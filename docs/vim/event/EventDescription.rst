.. _vmodl.DynamicData: ../../vmodl/DynamicData.rst

.. _vim.EnumDescription: ../../vim/EnumDescription.rst

.. _Event Category enum: ../../vim/event/EventDescription/EventCategory.rst

.. _vim.ElementDescription: ../../vim/ElementDescription.rst

.. _vim.event.EventDescription.EventDetail: ../../vim/event/EventDescription/EventDetail.rst


vim.event.EventDescription
==========================
  This data object provides static, locale-specific strings for event objects.
:extends: vmodl.DynamicData_

Attributes:
    category ([`vim.ElementDescription`_]):

        `Event Category enum`_ 
    eventInfo ([`vim.event.EventDescription.EventDetail`_]):

       The event class description details.
    enumeratedTypes ([`vim.EnumDescription`_], optional):

       Localized descriptions of all enumerated types that are used for member declarations in event classes.
