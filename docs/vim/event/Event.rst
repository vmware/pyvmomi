.. _int: https://docs.python.org/2/library/stdtypes.html

.. _str: https://docs.python.org/2/library/stdtypes.html

.. _datetime: https://docs.python.org/2/library/stdtypes.html

.. _vmodl.DynamicData: ../../vmodl/DynamicData.rst

.. _vim.event.VmEventArgument: ../../vim/event/VmEventArgument.rst

.. _vim.event.DvsEventArgument: ../../vim/event/DvsEventArgument.rst

.. _vim.event.HostEventArgument: ../../vim/event/HostEventArgument.rst

.. _vim.event.NetworkEventArgument: ../../vim/event/NetworkEventArgument.rst

.. _vim.event.DatastoreEventArgument: ../../vim/event/DatastoreEventArgument.rst

.. _vim.event.DatacenterEventArgument: ../../vim/event/DatacenterEventArgument.rst

.. _vim.event.ComputeResourceEventArgument: ../../vim/event/ComputeResourceEventArgument.rst


vim.event.Event
===============
  This event is the base data object type from which all events inherit. All event objects are data structures that describe events. While event data objects are data structures that describe events, event data type documentation may describe what the event records, rather than the data structure, itself.
:extends: vmodl.DynamicData_

Attributes:
    key (`int`_):

       The event ID.
    chainId (`int`_):

       The parent or group ID.
    createdTime (`datetime`_):

       The time the event was created.
    userName (`str`_):

       The user who caused the event.
    datacenter (`vim.event.DatacenterEventArgument`_, optional):

       The Datacenter object of the event.
    computeResource (`vim.event.ComputeResourceEventArgument`_, optional):

       The ComputeResource object of the event.
    host (`vim.event.HostEventArgument`_, optional):

       The Host object of the event.
    vm (`vim.event.VmEventArgument`_, optional):

       The VirtualMachine object of the event.
    ds (`vim.event.DatastoreEventArgument`_, optional):

       The Datastore object of the event.
    net (`vim.event.NetworkEventArgument`_, optional):

       The Network object of the event.
    dvs (`vim.event.DvsEventArgument`_, optional):

       The DistributedVirtualSwitch object of the event.
    fullFormattedMessage (`str`_, optional):

       A formatted text message describing the event. The message may be localized.
    changeTag (`str`_, optional):

       The user entered tag to identify the operations and their side effects
