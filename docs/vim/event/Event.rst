
vim.event.Event
===============
  This event is the base data object type from which all events inherit. All event objects are data structures that describe events. While event data objects are data structures that describe events, event data type documentation may describe what the event records, rather than the data structure, itself.
:extends: vmodl.DynamicData_

Attributes:
    key (`int <https://docs.python.org/2/library/stdtypes.html>`_):

       The event ID.
    chainId (`int <https://docs.python.org/2/library/stdtypes.html>`_):

       The parent or group ID.
    createdTime (`datetime <https://docs.python.org/2/library/stdtypes.html>`_):

       The time the event was created.
    userName (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       The user who caused the event.
    datacenter (`vim.event.DatacenterEventArgument <vim/event/DatacenterEventArgument.rst>`_, optional):

       The Datacenter object of the event.
    computeResource (`vim.event.ComputeResourceEventArgument <vim/event/ComputeResourceEventArgument.rst>`_, optional):

       The ComputeResource object of the event.
    host (`vim.event.HostEventArgument <vim/event/HostEventArgument.rst>`_, optional):

       The Host object of the event.
    vm (`vim.event.VmEventArgument <vim/event/VmEventArgument.rst>`_, optional):

       The VirtualMachine object of the event.
    ds (`vim.event.DatastoreEventArgument <vim/event/DatastoreEventArgument.rst>`_, optional):

       The Datastore object of the event.
    net (`vim.event.NetworkEventArgument <vim/event/NetworkEventArgument.rst>`_, optional):

       The Network object of the event.
    dvs (`vim.event.DvsEventArgument <vim/event/DvsEventArgument.rst>`_, optional):

       The DistributedVirtualSwitch object of the event.
    fullFormattedMessage (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       A formatted text message describing the event. The message may be localized.
    changeTag (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       The user entered tag to identify the operations and their side effects
