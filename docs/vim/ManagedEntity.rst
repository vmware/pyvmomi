
vim.ManagedEntity
=================
  ManagedEntity is an abstract base type for all managed objects present in the inventory tree. The base type provides common functionality for traversing the tree structure, as well as health monitoring and other basic functions.Most Virtual Infrastructure managed object types extend this type.


:extends: vim.ExtensibleManagedObject_


Attributes
----------
    parent (`vim.ManagedEntity <vim/ManagedEntity.rst>`_):
      privilege: System.View
       Parent of this entity.This value is null for the root object and for `VirtualMachine <vim/VirtualMachine.rst>`_ objects that are part of a `VirtualApp <vim/VirtualApp.rst>`_ .
    customValue ([`vim.CustomFieldsManager.Value <vim/CustomFieldsManager/Value.rst>`_]):
      privilege: System.View
       Custom field values.
    overallStatus (`vim.ManagedEntity.Status <vim/ManagedEntity/Status.rst>`_):
       General health of this managed entity. The overall status of the managed entity is computed as the worst status among its alarms and the configuration issues detected on the entity. The status is reported as one of the following values:
        * red: The entity has alarms or configuration issues with a red status.
        * yellow: The entity does not have alarms or configuration issues with a red status, and has at least one with a yellow status.
        * green: The entity does not have alarms or configuration issues with a red or yellow status, and has at least one with a green status.
        * gray: All of the entity's alarms have a gray status and the configuration status of the entity is not being monitored.
        * In releases after vSphere API 5.0, vSphere Servers might not generate property collector update notifications for this property. To obtain the latest value of the property, you can use PropertyCollector methods RetrievePropertiesEx or WaitForUpdatesEx. If you use the PropertyCollector.WaitForUpdatesEx method, specify an empty string for the version parameter. Any other version value will not produce any property values as no updates are generated.
    configStatus (`vim.ManagedEntity.Status <vim/ManagedEntity/Status.rst>`_):
       The configStatus indicates whether or not the system has detected a configuration issue involving this entity. For example, it might have detected a duplicate IP address or MAC address, or a host in a cluster might be out of compliance. The meanings of the configStatus values are:
        * red: A problem has been detected involving the entity.
        * yellow: A problem is about to occur or a transient condition has occurred (For example, reconfigure fail-over policy).
        * green: No configuration issues have been detected.
        * gray: The configuration status of the entity is not being monitored.
        * A green status indicates only that a problem has not been detected; it is not a guarantee that the entity is problem-free.
        * The
        * `configIssue <vim/ManagedEntity.rst#configIssue>`_
        * property contains a list of the problems that have been detected. In releases after vSphere API 5.0, vSphere Servers might not generate property collector update notifications for this property. To obtain the latest value of the property, you can use PropertyCollector methods RetrievePropertiesEx or WaitForUpdatesEx. If you use the PropertyCollector.WaitForUpdatesEx method, specify an empty string for the version parameter. Any other version value will not produce any property values as no updates are generated.
    configIssue ([`vim.event.Event <vim/event/Event.rst>`_]):
       Current configuration issues that have been detected for this entity. Typically, these issues have already been logged as events. The entity stores these events as long as they are still current. The `configStatus <vim/ManagedEntity.rst#configStatus>`_ property provides an overall status based on these events.
    effectiveRole ([`int <https://docs.python.org/2/library/stdtypes.html>`_]):
      privilege: System.View
       Access rights the current session has to this entity.
    permission ([`vim.AuthorizationManager.Permission <vim/AuthorizationManager/Permission.rst>`_]):
       List of permissions defined for this entity.
    name (`str <https://docs.python.org/2/library/stdtypes.html>`_):
      privilege: System.View
       Name of this entity, unique relative to its parent.Any / (slash), \ (backslash), character used in this name element will be escaped. Similarly, any % (percent) character used in this name element will be escaped, unless it is used to start an escape sequence. A slash is escaped as %2F or %2f. A backslash is escaped as %5C or %5c, and a percent is escaped as %25.
    disabledMethod ([`str <https://docs.python.org/2/library/stdtypes.html>`_]):
       List of operations that are disabled, given the current runtime state of the entity. For example, a power-on operation always fails if a virtual machine is already powered on. This list can be used by clients to enable or disable operations in a graphical user interface.Note: This list is determined by the current runtime state of an entity, not by its permissions.This list may include the following operations for a HostSystem:
        * `EnterMaintenanceMode_Task <vim/HostSystem.rst#enterMaintenanceMode>`_
        * 
        * `ExitMaintenanceMode_Task <vim/HostSystem.rst#exitMaintenanceMode>`_
        * 
        * `RebootHost_Task <vim/HostSystem.rst#reboot>`_
        * 
        * `ShutdownHost_Task <vim/HostSystem.rst#shutdown>`_
        * 
        * `ReconnectHost_Task <vim/HostSystem.rst#reconnect>`_
        * 
        * `DisconnectHost_Task <vim/HostSystem.rst#disconnect>`_
        * 
        * 
        * This list may include the following operations for a VirtualMachine:
        * 
        * `AnswerVM <vim/VirtualMachine.rst#answer>`_
        * 
        * `Rename_Task <vim/ManagedEntity.rst#rename>`_
        * 
        * `CloneVM_Task <vim/VirtualMachine.rst#clone>`_
        * 
        * `PowerOffVM_Task <vim/VirtualMachine.rst#powerOff>`_
        * 
        * `PowerOnVM_Task <vim/VirtualMachine.rst#powerOn>`_
        * 
        * `SuspendVM_Task <vim/VirtualMachine.rst#suspend>`_
        * 
        * `ResetVM_Task <vim/VirtualMachine.rst#reset>`_
        * 
        * `ReconfigVM_Task <vim/VirtualMachine.rst#reconfigure>`_
        * 
        * `RelocateVM_Task <vim/VirtualMachine.rst#relocate>`_
        * 
        * `MigrateVM_Task <vim/VirtualMachine.rst#migrate>`_
        * 
        * `CustomizeVM_Task <vim/VirtualMachine.rst#customize>`_
        * 
        * `ShutdownGuest <vim/VirtualMachine.rst#shutdownGuest>`_
        * 
        * `StandbyGuest <vim/VirtualMachine.rst#standbyGuest>`_
        * 
        * `RebootGuest <vim/VirtualMachine.rst#rebootGuest>`_
        * 
        * `CreateSnapshot_Task <vim/VirtualMachine.rst#createSnapshot>`_
        * 
        * `RemoveAllSnapshots_Task <vim/VirtualMachine.rst#removeAllSnapshots>`_
        * 
        * `RevertToCurrentSnapshot_Task <vim/VirtualMachine.rst#revertToCurrentSnapshot>`_
        * 
        * `MarkAsTemplate <vim/VirtualMachine.rst#markAsTemplate>`_
        * 
        * `MarkAsVirtualMachine <vim/VirtualMachine.rst#markAsVirtualMachine>`_
        * 
        * `ResetGuestInformation <vim/VirtualMachine.rst#resetGuestInformation>`_
        * 
        * `MountToolsInstaller <vim/VirtualMachine.rst#mountToolsInstaller>`_
        * 
        * `UnmountToolsInstaller <vim/VirtualMachine.rst#unmountToolsInstaller>`_
        * 
        * `Destroy_Task <vim/ManagedEntity.rst#destroy>`_
        * 
        * `UpgradeVM_Task <vim/VirtualMachine.rst#upgradeVirtualHardware>`_
        * 
        * `ExportVm <vim/VirtualMachine.rst#exportVm>`_
        * 
        * 
        * This list may include the following operations for a ResourcePool:
        * 
        * `ImportVApp <vim/ResourcePool.rst#importVApp>`_
        * 
        * `CreateChildVM_Task <vim/ResourcePool.rst#createVm>`_
        * 
        * `UpdateConfig <vim/ResourcePool.rst#updateConfig>`_
        * 
        * `CreateVM_Task <vim/Folder.rst#createVm>`_
        * 
        * `Destroy_Task <vim/ManagedEntity.rst#destroy>`_
        * 
        * `Rename_Task <vim/ManagedEntity.rst#rename>`_
        * 
        * This list may include the following operations for a VirtualApp:
        * 
        * `Destroy_Task <vim/ManagedEntity.rst#destroy>`_
        * 
        * `CloneVApp_Task <vim/VirtualApp.rst#clone>`_
        * 
        * `unregisterVApp_Task <vim/VirtualApp.rst#unregister>`_
        * 
        * `ExportVApp <vim/VirtualApp.rst#exportVApp>`_
        * 
        * `PowerOnVApp_Task <vim/VirtualApp.rst#powerOn>`_
        * 
        * `PowerOffVApp_Task <vim/VirtualApp.rst#powerOff>`_
        * 
        * `UpdateVAppConfig <vim/VirtualApp.rst#updateVAppConfig>`_
        * 
        * 
        * In releases after vSphere API 5.0, vSphere Servers might not generate property collector update notifications for this property. To obtain the latest value of the property, you can use PropertyCollector methods RetrievePropertiesEx or WaitForUpdatesEx. If you use the PropertyCollector.WaitForUpdatesEx method, specify an empty string for the version parameter. Any other version value will not produce any property values as no updates are generated.
    recentTask ([`vim.Task <vim/Task.rst>`_]):
       The set of recent tasks operating on this managed entity. This is a subset of `recentTask <vim/TaskManager.rst#recentTask>`_ belong to this entity. A task in this list could be in one of the four states: pending, running, success or error.This property can be used to deduce intermediate power states for a virtual machine entity. For example, if the current powerState is "poweredOn" and there is a running task performing the "suspend" operation, then the virtual machine's intermediate state might be described as "suspending."Most tasks (such as power operations) obtain exclusive access to the virtual machine, so it is unusual for this list to contain more than one running task. One exception, however, is the task of cloning a virtual machine. In releases after vSphere API 5.0, vSphere Servers might not generate property collector update notifications for this property. To obtain the latest value of the property, you can use PropertyCollector methods RetrievePropertiesEx or WaitForUpdatesEx. If you use the PropertyCollector.WaitForUpdatesEx method, specify an empty string for the version parameter. Any other version value will not produce any property values as no updates are generated.
    declaredAlarmState ([`vim.alarm.AlarmState <vim/alarm/AlarmState.rst>`_]):
      privilege: System.View
       A set of alarm states for alarms that apply to this managed entity. The set includes alarms defined on this entity and alarms inherited from the parent entity, or from any ancestors in the inventory hierarchy.Alarms are inherited if they can be triggered by this entity or its descendants. This set does not include alarms that are defined on descendants of this entity.
    triggeredAlarmState ([`vim.alarm.AlarmState <vim/alarm/AlarmState.rst>`_]):
      privilege: System.View
       A set of alarm states for alarms triggered by this entity or by its descendants.Triggered alarms are propagated up the inventory hierarchy so that a user can readily tell when a descendant has triggered an alarm. In releases after vSphere API 5.0, vSphere Servers might not generate property collector update notifications for this property. To obtain the latest value of the property, you can use PropertyCollector methods RetrievePropertiesEx or WaitForUpdatesEx. If you use the PropertyCollector.WaitForUpdatesEx method, specify an empty string for the version parameter. Any other version value will not produce any property values as no updates are generated.
    alarmActionsEnabled (`bool <https://docs.python.org/2/library/stdtypes.html>`_):
      privilege: System.Read
       Whether alarm actions are enabled for this entity. True if enabled; false otherwise.
    tag ([`vim.Tag <vim/Tag.rst>`_]):
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
   Renames this managed entity.Any % (percent) character used in this name parameter must be escaped, unless it is used to start an escape sequence. Clients may also escape any other characters in this name parameter.See `name <vim/ManagedEntity.rst#name>`_ 


  Privilege:



  Args:
    newName (`str <https://docs.python.org/2/library/stdtypes.html>`_):
       See `name <vim/ManagedEntity.rst#name>`_ 




  Returns:
     `vim.Task <vim/Task.rst>`_:
         

  Raises:

    `vim.fault.DuplicateName <vim/fault/DuplicateName.rst>`_: 
       If another object in the same folder has the target name.See `name <vim/ManagedEntity.rst#name>`_ 

    `vim.fault.InvalidName <vim/fault/InvalidName.rst>`_: 
       If the new name is not a valid entity name.See `name <vim/ManagedEntity.rst#name>`_ 


Destroy():
   Destroys this object, deleting its contents and removing it from its parent folder (if any).NOTE: The appropriate privilege must be held on the parent of the destroyed entity as well as the entity itself.This method can throw one of several exceptions. The exact set of exceptions depends on the kind of entity that is being removed. See comments for each entity for more information on destroy behavior.


  Privilege:



  Args:


  Returns:
     `vim.Task <vim/Task.rst>`_:
         

  Raises:

    `vim.fault.VimFault <vim/fault/VimFault.rst>`_: 
       vim.fault.VimFault


