.. _str: https://docs.python.org/2/library/stdtypes.html

.. _VI API 2.5: ../../vim/version.rst#vimversionversion2

.. _vmodl.DynamicData: ../../vmodl/DynamicData.rst


vim.Extension.EventTypeInfo
===========================
  This data object type describes event types defined by the extension.
:extends: vmodl.DynamicData_
:since: `VI API 2.5`_

Attributes:
    eventID (`str`_):

       The ID of the event type. Should follow java package naming conventions for uniqueness.
    eventTypeSchema (`str`_, optional):

       Optional XML descriptor for the EventType. The structure of this descriptor is:EventTypeeventTypeIDeventID/eventTypeIDdescriptionOptional description for event eventID/description!-- Optional arguments: --arguments!-- Zero or more of: --argumentnameargName/nametypeargtype/name/argument/arguments/EventTypewhereargtypecan be one of the following:
        * string
        * 
        * moid
        * 
        * long
        * 
        * int
        * 
        * bool
        * 
        * Note:
        * moid
        * is really just a string, with some additional semantic meaning attached - that it is the identifier of some object in the inventory, and can be looked up by a client that is so inclined.
