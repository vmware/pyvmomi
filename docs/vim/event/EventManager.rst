.. _int: https://docs.python.org/2/library/stdtypes.html

.. _str: https://docs.python.org/2/library/stdtypes.html

.. _Event: ../../vim/event/Event.rst

.. _chainId: ../../vim/event/Event.rst#chainId

.. _vim.Task: ../../vim/Task.rst

.. _VI API 2.5: ../../vim/version.rst#vimversionversion2

.. _createdTime: ../../vim/event/Event.rst#createdTime

.. _vim.TaskInfo: ../../vim/TaskInfo.rst

.. _vim.event.Event: ../../vim/event/Event.rst

.. _vSphere API 4.0: ../../vim/version.rst#vimversionversion5

.. _vim.ManagedEntity: ../../vim/ManagedEntity.rst

.. _EntityEventArgument: ../../vim/event/EntityEventArgument.rst

.. _vim.fault.InvalidState: ../../vim/fault/InvalidState.rst

.. _vim.fault.InvalidEvent: ../../vim/fault/InvalidEvent.rst

.. _vim.event.EventFilterSpec: ../../vim/event/EventFilterSpec.rst

.. _vim.event.EventDescription: ../../vim/event/EventDescription.rst

.. _vmodl.fault.InvalidArgument: ../../vmodl/fault/InvalidArgument.rst

.. _vim.event.EventHistoryCollector: ../../vim/event/EventHistoryCollector.rst

.. _vim.event.EventDescription.EventArgDesc: ../../vim/event/EventDescription/EventArgDesc.rst


vim.event.EventManager
======================
  This managed object type provides properties and methods for event management support. Event objects are used to record significant state changes of managed entities.




Attributes
----------
    description (`vim.event.EventDescription`_):
      privilege: System.View
       Static descriptive strings used in events.
    latestEvent (`vim.event.Event`_):
      privilege: System.View
       The latest event that happened on the VirtualCenter server.
    maxCollector (`int`_):
      privilege: System.View
       For each client, the maximum number of event collectors that can exist simultaneously.


Methods
-------


RetrieveArgumentDescription(eventTypeId):
   Retrieves the argument meta-data for a given Event type
  since: `vSphere API 4.0`_


  Privilege:
               System.View



  Args:
    eventTypeId (`str`_):




  Returns:
    `vim.event.EventDescription.EventArgDesc`_:
         


CreateCollectorForEvents(filter):
   Creates an event history collector, which is a specialized history collector that provides Event objects.Event collectors do not persist beyond the current client session.


  Privilege:
               System.View



  Args:
    filter (`vim.event.EventFilterSpec`_):
       The event query filter.




  Returns:
    `vim.event.EventHistoryCollector`_:
         The event collector based on the filter.

  Raises:

    `vim.fault.InvalidState`_: 
       if there are more than the maximum number of event collectors.

    `vmodl.fault.InvalidArgument`_: 
       if the filter is null or if any of its fields is invalid, such as an invalid reference to a managed object, alarm, or scheduled task, or an invalid event type or event chain id, etc.


LogUserEvent(entity, msg):
   Logs a user defined event against a particular managed entity.


  Privilege:



  Args:
    entity (`vim.ManagedEntity`_):
       The entity against which the event is logged. The entity must be the root folder, a DataCenter, a VirtualMachine, a HostSystem, or a ComputeResource.


    msg (`str`_):
       The message to be logged.




  Returns:
    None
         

  Raises:

    `vmodl.fault.InvalidArgument`_: 
       if the entity is of a wrong type or the "msg" string is empty.


QueryEvents(filter):
   Returns the events in specified filter. Returns empty array when there are not any events qualified.


  Privilege:
               System.View



  Args:
    filter (`vim.event.EventFilterSpec`_):
       The events qualified.




  Returns:
    `vim.event.Event`_:
         The events matching the filter.

  Raises:

    `vmodl.fault.InvalidArgument`_: 
       if the filter is null or if any of its fields is invalid, such as an invalid reference to a managed object, alarm, or scheduled task, or an invalid event type or event chain id, etc.


PostEvent(eventToPost, taskInfo):
   Posts the specified event, optionally associating it with a task.The event being posted should have the following info in it:
    * The ManagedEntity on which the event is being posted should be set in the appropriate
    * `EntityEventArgument`_
    * field of the base
    * `Event`_
    * class. It is OK to not set any entity, in which case the event is treated as an event about the system.
    * Some Event fields (
    * `key`_
    * ,
    * `chainId`_
    * ,
    * `createdTime`_
    * ) are mandatory because of the nature of the structure, but any caller-supplied values will be overwritten by the system.
    * 
    * If the event being posted is to be associated with an existing Task, the appropriate TaskInfo needs to be passed in. This task can either be one returned from a vSphere API operation or an extension task created by calling TaskManager#createTask.
  since: `VI API 2.5`_


  Privilege:
               Global.LogEvent



  Args:
    eventToPost (`vim.event.Event`_):
       Fully-specified event to post


    taskInfo (`vim.TaskInfo`_, optional):
       optional task associated with the event




  Returns:
    None
         

  Raises:

    `vim.fault.InvalidEvent`_: 
       no longer thrown by this API

    `vmodl.fault.InvalidArgument`_: 
       if
        * an invalid reference to a managed object is passed in to one of the
        * `EntityEventArgument`_
        * fields
        * an invalid severity value is passed in an
        * `EventEx`_
        * .
        * 


