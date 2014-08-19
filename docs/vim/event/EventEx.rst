
vim.event.EventEx
=================
  EventEx is a dynamically typed Event class, whose type is indicated by its eventTypeId property.A collection of eventTypeIds is registered by Extensions, which can now pass in optional type information for each eventTypeId which indicates the applicable argument names and types, among other properties.EventEx allows event arguments of any type, though today, the system only supports "string" and "moid" (a string which can be interpreted as an object ID in the system) as argument types. In the future, the system may optionally strongly check the types of the arguments in the event against the declared type information, based on how the event type is declared.EventEx also allows arbitrary "event object"s - the object which the event refers to. You can put in any object identifier as the objectId, but objectType should be filled in only if the object is actually present in the VC Server's ManagedEntity inventory.
:extends: vim.event.Event_
:since: `vSphere API 4.0 <vim/version.rst#vimversionversion5>`_

Attributes:
    eventTypeId (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       The type of the event.
    severity (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       The severity level of the message: null=>info.See `EventEventSeverity <vim/event/Event/EventSeverity.rst>`_ 
    message (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       An arbitrary message string, not localized.
    arguments ([`vmodl.KeyAnyValue <vmodl/KeyAnyValue.rst>`_], optional):

       The event arguments associated with the event
    objectId (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       The ID of the object (VM, Host, Folder..) which the event pertains to. Federated or local inventory path.
    objectType (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       the type of the object, if known to the VirtualCenter inventory
    objectName (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       The name of the object
    fault (`vmodl.LocalizedMethodFault <vmodl/LocalizedMethodFault.rst>`_, optional):

       The fault that triggered the event, if any
