.. _int: https://docs.python.org/2/library/stdtypes.html

.. _str: https://docs.python.org/2/library/stdtypes.html

.. _bool: https://docs.python.org/2/library/stdtypes.html

.. _name: ../vim/ManagedEntity.rst#name

.. _vim.Tag: ../vim/Tag.rst

.. _vim.Task: ../vim/Task.rst

.. _AnswerVM: ../vim/VirtualMachine.rst#answer

.. _ExportVm: ../vim/VirtualMachine.rst#exportVm

.. _ImportVApp: ../vim/ResourcePool.rst#importVApp

.. _recentTask: ../vim/TaskManager.rst#recentTask

.. _VirtualApp: ../vim/VirtualApp.rst

.. _ExportVApp: ../vim/VirtualApp.rst#exportVApp

.. _RebootGuest: ../vim/VirtualMachine.rst#rebootGuest

.. _configIssue: ../vim/ManagedEntity.rst#configIssue

.. _Rename_Task: ../vim/ManagedEntity.rst#rename

.. _StandbyGuest: ../vim/VirtualMachine.rst#standbyGuest

.. _ResetVM_Task: ../vim/VirtualMachine.rst#reset

.. _configStatus: ../vim/ManagedEntity.rst#configStatus

.. _CloneVM_Task: ../vim/VirtualMachine.rst#clone

.. _UpdateConfig: ../vim/ResourcePool.rst#updateConfig

.. _Destroy_Task: ../vim/ManagedEntity.rst#destroy

.. _CreateVM_Task: ../vim/Folder.rst#createVm

.. _ShutdownGuest: ../vim/VirtualMachine.rst#shutdownGuest

.. _SuspendVM_Task: ../vim/VirtualMachine.rst#suspend

.. _UpgradeVM_Task: ../vim/VirtualMachine.rst#upgradeVirtualHardware

.. _PowerOnVM_Task: ../vim/VirtualMachine.rst#powerOn

.. _VirtualMachine: ../vim/VirtualMachine.rst

.. _CloneVApp_Task: ../vim/VirtualApp.rst#clone

.. _MarkAsTemplate: ../vim/VirtualMachine.rst#markAsTemplate

.. _MigrateVM_Task: ../vim/VirtualMachine.rst#migrate

.. _RebootHost_Task: ../vim/HostSystem.rst#reboot

.. _RelocateVM_Task: ../vim/VirtualMachine.rst#relocate

.. _vSphere API 4.0: ../vim/version.rst#vimversionversion5

.. _ReconfigVM_Task: ../vim/VirtualMachine.rst#reconfigure

.. _PowerOffVM_Task: ../vim/VirtualMachine.rst#powerOff

.. _vim.event.Event: ../vim/event/Event.rst

.. _PowerOnVApp_Task: ../vim/VirtualApp.rst#powerOn

.. _CustomizeVM_Task: ../vim/VirtualMachine.rst#customize

.. _UpdateVAppConfig: ../vim/VirtualApp.rst#updateVAppConfig

.. _PowerOffVApp_Task: ../vim/VirtualApp.rst#powerOff

.. _ShutdownHost_Task: ../vim/HostSystem.rst#shutdown

.. _vim.ManagedEntity: ../vim/ManagedEntity.rst

.. _ReconnectHost_Task: ../vim/HostSystem.rst#reconnect

.. _vim.fault.VimFault: ../vim/fault/VimFault.rst

.. _CreateChildVM_Task: ../vim/ResourcePool.rst#createVm

.. _unregisterVApp_Task: ../vim/VirtualApp.rst#unregister

.. _MountToolsInstaller: ../vim/VirtualMachine.rst#mountToolsInstaller

.. _DisconnectHost_Task: ../vim/HostSystem.rst#disconnect

.. _CreateSnapshot_Task: ../vim/VirtualMachine.rst#createSnapshot

.. _vim.alarm.AlarmState: ../vim/alarm/AlarmState.rst

.. _MarkAsVirtualMachine: ../vim/VirtualMachine.rst#markAsVirtualMachine

.. _UnmountToolsInstaller: ../vim/VirtualMachine.rst#unmountToolsInstaller

.. _vim.fault.InvalidName: ../vim/fault/InvalidName.rst

.. _ResetGuestInformation: ../vim/VirtualMachine.rst#resetGuestInformation

.. _RemoveAllSnapshots_Task: ../vim/VirtualMachine.rst#removeAllSnapshots

.. _vim.fault.DuplicateName: ../vim/fault/DuplicateName.rst

.. _vim.ManagedEntity.Status: ../vim/ManagedEntity/Status.rst

.. _ExitMaintenanceMode_Task: ../vim/HostSystem.rst#exitMaintenanceMode

.. _EnterMaintenanceMode_Task: ../vim/HostSystem.rst#enterMaintenanceMode

.. _vim.ExtensibleManagedObject: ../vim/ExtensibleManagedObject.rst

.. _RevertToCurrentSnapshot_Task: ../vim/VirtualMachine.rst#revertToCurrentSnapshot

.. _vim.CustomFieldsManager.Value: ../vim/CustomFieldsManager/Value.rst

.. _vim.AuthorizationManager.Permission: ../vim/AuthorizationManager/Permission.rst


vim.ManagedEntity
=================
  ManagedEntity is an abstract base type for all managed objects present in the inventory tree. The base type provides common functionality for traversing the tree structure, as well as health monitoring and other basic functions.Most Virtual Infrastructure managed object types extend this type.


:extends: vim.ExtensibleManagedObject_


Attributes
----------
    parent (`vim.ManagedEntity`_):
      privilege: System.View
       Parent of this entity.This value is null for the root object and for `VirtualMachine`_ objects that are part of a `VirtualApp`_ .
    customValue (`vim.CustomFieldsManager.Value`_):
      privilege: System.View
       Custom field values.
    overallStatus (`vim.ManagedEntity.Status`_):
       General health of this managed entity. The overall status of the managed entity is computed as the worst status among its alarms and the configuration issues detected on the entity. The status is reported as one of the following values:
        * red: The entity has alarms or configuration issues with a red status.
        * yellow: The entity does not have alarms or configuration issues with a red status, and has at least one with a yellow status.
        * green: The entity does not have alarms or configuration issues with a red or yellow status, and has at least one with a green status.
        * gray: All of the entity's alarms have a gray status and the configuration status of the entity is not being monitored.
        * In releases after vSphere API 5.0, vSphere Servers might not generate property collector update notifications for this property. To obtain the latest value of the property, you can use PropertyCollector methods RetrievePropertiesEx or WaitForUpdatesEx. If you use the PropertyCollector.WaitForUpdatesEx method, specify an empty string for the version parameter. Any other version value will not produce any property values as no updates are generated.
    configStatus (`vim.ManagedEntity.Status`_):
       The configStatus indicates whether or not the system has detected a configuration issue involving this entity. For example, it might have detected a duplicate IP address or MAC address, or a host in a cluster might be out of compliance. The meanings of the configStatus values are:
        * red: A problem has been detected involving the entity.
        * yellow: A problem is about to occur or a transient condition has occurred (For example, reconfigure fail-over policy).
        * green: No configuration issues have been detected.
        * gray: The configuration status of the entity is not being monitored.
        * A green status indicates only that a problem has not been detected; it is not a guarantee that the entity is problem-free.
        * The
        * `configIssue`_
        * property contains a list of the problems that have been detected. In releases after vSphere API 5.0, vSphere Servers might not generate property collector update notifications for this property. To obtain the latest value of the property, you can use PropertyCollector methods RetrievePropertiesEx or WaitForUpdatesEx. If you use the PropertyCollector.WaitForUpdatesEx method, specify an empty string for the version parameter. Any other version value will not produce any property values as no updates are generated.
    configIssue (`vim.event.Event`_):
       Current configuration issues that have been detected for this entity. Typically, these issues have already been logged as events. The entity stores these events as long as they are still current. The `configStatus`_ property provides an overall status based on these events.
    effectiveRole (`int`_):
      privilege: System.View
       Access rights the current session has to this entity.
    permission (`vim.AuthorizationManager.Permission`_):
       List of permissions defined for this entity.
    name (`str`_):
      privilege: System.View
       Name of this entity, unique relative to its parent.Any / (slash), \ (backslash), character used in this name element will be escaped. Similarly, any % (percent) character used in this name element will be escaped, unless it is used to start an escape sequence. A slash is escaped as %2F or %2f. A backslash is escaped as %5C or %5c, and a percent is escaped as %25.
    disabledMethod (`str`_):
       List of operations that are disabled, given the current runtime state of the entity. For example, a power-on operation always fails if a virtual machine is already powered on. This list can be used by clients to enable or disable operations in a graphical user interface.Note: This list is determined by the current runtime state of an entity, not by its permissions.This list may include the following operations for a HostSystem:
        * `EnterMaintenanceMode_Task`_
        * 
        * `ExitMaintenanceMode_Task`_
        * 
        * `RebootHost_Task`_
        * 
        * `ShutdownHost_Task`_
        * 
        * `ReconnectHost_Task`_
        * 
        * `DisconnectHost_Task`_
        * 
        * 
        * This list may include the following operations for a VirtualMachine:
        * 
        * `AnswerVM`_
        * 
        * `Rename_Task`_
        * 
        * `CloneVM_Task`_
        * 
        * `PowerOffVM_Task`_
        * 
        * `PowerOnVM_Task`_
        * 
        * `SuspendVM_Task`_
        * 
        * `ResetVM_Task`_
        * 
        * `ReconfigVM_Task`_
        * 
        * `RelocateVM_Task`_
        * 
        * `MigrateVM_Task`_
        * 
        * `CustomizeVM_Task`_
        * 
        * `ShutdownGuest`_
        * 
        * `StandbyGuest`_
        * 
        * `RebootGuest`_
        * 
        * `CreateSnapshot_Task`_
        * 
        * `RemoveAllSnapshots_Task`_
        * 
        * `RevertToCurrentSnapshot_Task`_
        * 
        * `MarkAsTemplate`_
        * 
        * `MarkAsVirtualMachine`_
        * 
        * `ResetGuestInformation`_
        * 
        * `MountToolsInstaller`_
        * 
        * `UnmountToolsInstaller`_
        * 
        * `Destroy_Task`_
        * 
        * `UpgradeVM_Task`_
        * 
        * `ExportVm`_
        * 
        * 
        * This list may include the following operations for a ResourcePool:
        * 
        * `ImportVApp`_
        * 
        * `CreateChildVM_Task`_
        * 
        * `UpdateConfig`_
        * 
        * `CreateVM_Task`_
        * 
        * `Destroy_Task`_
        * 
        * `Rename_Task`_
        * 
        * This list may include the following operations for a VirtualApp:
        * 
        * `Destroy_Task`_
        * 
        * `CloneVApp_Task`_
        * 
        * `unregisterVApp_Task`_
        * 
        * `ExportVApp`_
        * 
        * `PowerOnVApp_Task`_
        * 
        * `PowerOffVApp_Task`_
        * 
        * `UpdateVAppConfig`_
        * 
        * 
        * In releases after vSphere API 5.0, vSphere Servers might not generate property collector update notifications for this property. To obtain the latest value of the property, you can use PropertyCollector methods RetrievePropertiesEx or WaitForUpdatesEx. If you use the PropertyCollector.WaitForUpdatesEx method, specify an empty string for the version parameter. Any other version value will not produce any property values as no updates are generated.
    recentTask (`vim.Task`_):
       The set of recent tasks operating on this managed entity. This is a subset of `recentTask`_ belong to this entity. A task in this list could be in one of the four states: pending, running, success or error.This property can be used to deduce intermediate power states for a virtual machine entity. For example, if the current powerState is "poweredOn" and there is a running task performing the "suspend" operation, then the virtual machine's intermediate state might be described as "suspending."Most tasks (such as power operations) obtain exclusive access to the virtual machine, so it is unusual for this list to contain more than one running task. One exception, however, is the task of cloning a virtual machine. In releases after vSphere API 5.0, vSphere Servers might not generate property collector update notifications for this property. To obtain the latest value of the property, you can use PropertyCollector methods RetrievePropertiesEx or WaitForUpdatesEx. If you use the PropertyCollector.WaitForUpdatesEx method, specify an empty string for the version parameter. Any other version value will not produce any property values as no updates are generated.
    declaredAlarmState (`vim.alarm.AlarmState`_):
      privilege: System.View
       A set of alarm states for alarms that apply to this managed entity. The set includes alarms defined on this entity and alarms inherited from the parent entity, or from any ancestors in the inventory hierarchy.Alarms are inherited if they can be triggered by this entity or its descendants. This set does not include alarms that are defined on descendants of this entity.
    triggeredAlarmState (`vim.alarm.AlarmState`_):
      privilege: System.View
       A set of alarm states for alarms triggered by this entity or by its descendants.Triggered alarms are propagated up the inventory hierarchy so that a user can readily tell when a descendant has triggered an alarm. In releases after vSphere API 5.0, vSphere Servers might not generate property collector update notifications for this property. To obtain the latest value of the property, you can use PropertyCollector methods RetrievePropertiesEx or WaitForUpdatesEx. If you use the PropertyCollector.WaitForUpdatesEx method, specify an empty string for the version parameter. Any other version value will not produce any property values as no updates are generated.
    alarmActionsEnabled (`bool`_):
      privilege: System.Read
       Whether alarm actions are enabled for this entity. True if enabled; false otherwise.
    tag (`vim.Tag`_):
      privilege: System.View
       The set of tags associated with this managed entity. Experimental. Subject to change.


Methods
-------


Reload():
   Reload the entity state. Clients only need to call this method if they changed some external state that affects the service without using the Web service interface to perform the change. For example, hand-editing a virtual machine configuration file affects the configuration of the associated virtual machine but the service managing the virtual machine might not monitor the file for changes. In this case, after such an edit, a client would call "reload" on the associated virtual machine to ensure the service and its clients have current data for the virtual machine.


  Privilege:
               System.Read



  Args:


  Returns:
    None
         


Rename(newName):
   Renames this managed entity.Any % (percent) character used in this name parameter must be escaped, unless it is used to start an escape sequence. Clients may also escape any other characters in this name parameter.See `name`_ 


  Privilege:



  Args:
    newName (`str`_):
       See `name`_ 




  Returns:
     `vim.Task`_:
         

  Raises:

    `vim.fault.DuplicateName`_: 
       If another object in the same folder has the target name.See `name`_ 

    `vim.fault.InvalidName`_: 
       If the new name is not a valid entity name.See `name`_ 


Destroy():
   Destroys this object, deleting its contents and removing it from its parent folder (if any).NOTE: The appropriate privilege must be held on the parent of the destroyed entity as well as the entity itself.This method can throw one of several exceptions. The exact set of exceptions depends on the kind of entity that is being removed. See comments for each entity for more information on destroy behavior.


  Privilege:



  Args:


  Returns:
     `vim.Task`_:
         

  Raises:

    `vim.fault.VimFault`_: 
       vim.fault.VimFault


