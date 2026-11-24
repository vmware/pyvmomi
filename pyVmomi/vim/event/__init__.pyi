# Copyright (c) 2006-2026 Broadcom. All Rights Reserved.
# The term "Broadcom" refers to Broadcom Inc. and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

import datetime as _datetime
import typing as _typing
import pyVmomi.VmomiSupport
import pyVmomi.vim
import pyVmomi.vmodl
import pyVmomi.vim.alarm
import pyVmomi.vim.dvs
import pyVmomi.vim.host
import pyVmomi.vim.profile
import pyVmomi.vim.scheduler
import pyVmomi.vim.vm
import pyVmomi.vim.profile.host



class Event(pyVmomi.vmodl.DynamicData):
   """
   This event is the base data object type from which all events inherit.
   
   All event
   objects are data structures that describe events. While event data objects are data
   structures that describe events, event data type documentation may describe what the
   event records, rather than the data structure, itself.
   
   Attributes:
       key: The event ID.
       chainId: The parent or group ID.
       createdTime: The time the event was created.
       userName: The user who caused the event.
       datacenter: The Datacenter object of the event.
       computeResource: The ComputeResource object of the event.
       host: The Host object of the event.
       vm: The VirtualMachine object of the event.
       ds: The Datastore object of the event.
       net: The Network object of the event.
       dvs: The DistributedVirtualSwitch object of the event.
       tgw: The TransitGateway object of the event.
           
           Since: vSphere API Release 9.1.0.0
       fullFormattedMessage: A formatted text message describing the event.
           
           The message may be localized.
       changeTag: The user entered tag to identify the operations and their side effects
       auditId: Specifies the name of the audit event.
           
           The value must never be empty.
           If unset, the event is not related to auditable activity.
           
           Since: vSphere API Release 9.1.0.0
   """
   class EventSeverity(pyVmomi.VmomiSupport.Enum):
      """
      Severity level constants.
      
      Attributes:
          error: Something that must be corrected
          warning: Should be corrected, but the system can continue operating normally
          info: An informational message
          user: A user-related message
      """
      error: _typing.ClassVar['Event.EventSeverity'] = 'error'
      warning: _typing.ClassVar['Event.EventSeverity'] = 'warning'
      info: _typing.ClassVar['Event.EventSeverity'] = 'info'
      user: _typing.ClassVar['Event.EventSeverity'] = 'user'

   key: int
   chainId: int
   createdTime: _datetime.datetime
   userName: str
   datacenter: _typing.Optional[DatacenterEventArgument] = None
   computeResource: _typing.Optional[ComputeResourceEventArgument] = None
   host: _typing.Optional[HostEventArgument] = None
   vm: _typing.Optional[VmEventArgument] = None
   ds: _typing.Optional[DatastoreEventArgument] = None
   net: _typing.Optional[NetworkEventArgument] = None
   dvs: _typing.Optional[DvsEventArgument] = None
   tgw: _typing.Optional[TgwEventArgument] = None
   fullFormattedMessage: _typing.Optional[str] = None
   changeTag: _typing.Optional[str] = None
   auditId: _typing.Optional[str] = None

class HostEvent(Event):
   """These are host-related events."""
   pass


class AccountCreatedEvent(HostEvent):
   """This event records that an account was created on a host."""
   spec: pyVmomi.vim.host.LocalAccountManager.AccountSpecification
   group: bool

class AccountRemovedEvent(HostEvent):
   """This event records that an account was removed from a host."""
   account: str
   group: bool


class AccountUpdatedEvent(HostEvent):
   """
   This event records that an account was updated on a host.
   
   Attributes:
       prevDescription: The previous account description
   """
   spec: pyVmomi.vim.host.LocalAccountManager.AccountSpecification
   group: bool
   prevDescription: _typing.Optional[str] = None

class AdminPasswordNotChangedEvent(HostEvent):
   """Default password for the Admin user on the host has not been changed."""
   pass

class AlarmEvent(Event):
   """
   This event is an alarm events.
   
   Attributes:
       alarm: The associated alarm object.
   """
   alarm: AlarmEventArgument

class AlarmAcknowledgedEvent(AlarmEvent):
   """
   This event records the acknowledgement of an Alarm
   
   Attributes:
       source: The entity that triggered the alarm.
       entity: The entity with which the alarm is registered.
   """
   source: ManagedEntityEventArgument
   entity: ManagedEntityEventArgument

class AlarmActionTriggeredEvent(AlarmEvent):
   """
   This event records that an alarm was triggered.
   
   Attributes:
       source: The entity that triggered the alarm.
       entity: The entity with which the alarm is registered.
   """
   source: ManagedEntityEventArgument
   entity: ManagedEntityEventArgument

class AlarmClearedEvent(AlarmEvent):
   """
   This event records the manual clearing of an Alarm
   
   Attributes:
       source: The entity that triggered the alarm.
       entity: The entity with which the alarm is registered.
       from: The original alarm status from which it was cleared
   """
   source: ManagedEntityEventArgument
   entity: ManagedEntityEventArgument
   # Reserved python keyword: commenting out.
   # from: str

class AlarmCreatedEvent(AlarmEvent):
   """
   This event records the creation of an alarm.
   
   Attributes:
       entity: The entity with which the alarm is registered.
   """
   entity: ManagedEntityEventArgument

class AlarmEmailCompletedEvent(AlarmEvent):
   """
   This event records the completion of an alarm email notification.
   
   Attributes:
       entity: The entity with which the alarm is registered.
       to: The destination email address.
   """
   entity: ManagedEntityEventArgument
   to: str


class AlarmEmailFailedEvent(AlarmEvent):
   """
   This event records a failure to complete an alarm email notification.
   
   Attributes:
       entity: The entity with which the alarm is registered.
       to: The destination email address.
       reason: The reason for the failure.
   """
   entity: ManagedEntityEventArgument
   to: str
   reason: pyVmomi.vmodl.MethodFault


class EventArgument(pyVmomi.vmodl.DynamicData):
   """
   This is the base type for event argument types.
   
   Event argument objects, which inherit from a common subtype,
   are used to manage supplementary properties of different kinds
   of event objects.
   """
   pass

class EntityEventArgument(EventArgument):
   """
   The event argument is a managed entity object.
   
   Subclasses of this type distinguish the different managed entities
   referenced in event objects.
   
   Attributes:
       name: Name of the entity, including its full path from the root of the inventory.
   """
   name: str


class AlarmEventArgument(EntityEventArgument):
   """
   The event argument is an Alarm object.
   
   Attributes:
       alarm: The Alarm object.
   """
   alarm: pyVmomi.vim.alarm.Alarm


class AlarmReconfiguredEvent(AlarmEvent):
   """
   This event records the reconfiguration of an alarm.
   
   Attributes:
       entity: The entity with which the alarm is registered.
       configChanges: The configuration values changed during the reconfiguration.
   """
   entity: ManagedEntityEventArgument
   configChanges: _typing.Optional[ChangesInfoEventArgument] = None

class AlarmRemovedEvent(AlarmEvent):
   """
   This event records the removal of an alarm.
   
   Attributes:
       entity: The entity with which the alarm is registered.
   """
   entity: ManagedEntityEventArgument

class AlarmScriptCompleteEvent(AlarmEvent):
   """
   This event records the completion of an alarm-triggered script.
   
   Attributes:
       entity: The entity with which the alarm is registered.
       script: The script triggered by the alarm.
   """
   entity: ManagedEntityEventArgument
   script: str


class AlarmScriptFailedEvent(AlarmEvent):
   """
   This event records a failure to complete an alarm-triggered script.
   
   Attributes:
       entity: The entity with which the alarm is registered.
       script: The script triggered by the alarm.
       reason: The reason for the failure.
   """
   entity: ManagedEntityEventArgument
   script: str
   reason: pyVmomi.vmodl.MethodFault

class AlarmSnmpCompletedEvent(AlarmEvent):
   """
   This event records the completion of an alarm SNMP notification.
   
   Attributes:
       entity: The entity with which the alarm is registered.
   """
   entity: ManagedEntityEventArgument


class AlarmSnmpFailedEvent(AlarmEvent):
   """
   This event records a failure to complete an alarm SNMP notification.
   
   Attributes:
       entity: The entity with which the alarm is registered.
       reason: The reason for the failure.
   """
   entity: ManagedEntityEventArgument
   reason: pyVmomi.vmodl.MethodFault

class AlarmStatusChangedEvent(AlarmEvent):
   """
   This event records a status change for an alarm.
   
   Attributes:
       source: The entity for which the alarm status has been changed.
       entity: The entity with which the alarm is registered.
       from: The original alarm status.
       to: The new alarm status.
   """
   source: ManagedEntityEventArgument
   entity: ManagedEntityEventArgument
   # Reserved python keyword: commenting out.
   # from: str
   to: str

class LicenseEvent(Event):
   """This is a base licensing event to group all license events."""
   pass

class AllVirtualMachinesLicensedEvent(LicenseEvent):
   """
   This event records that the previously unlicensed virtual machines on
   the specified host are now licensed.
   
   After this event is entered into
   the event log, we expect to see that the `vim.event.Event.UnlicensedVirtualMachinesEvent` `vim.ManagedEntity.configIssue` is removed from the host.
   """
   pass

class SessionEvent(Event):
   """These are session events."""
   pass

class AlreadyAuthenticatedSessionEvent(SessionEvent):
   """This event records a failed user logon due to the user already being logged on."""
   pass

class AuthorizationEvent(Event):
   """These events indicate authorization events."""
   pass

class BadUsernameSessionEvent(SessionEvent):
   """
   This event records a failed user logon.
   
   Failed logons are due to no match existing
   between the provided user name and password combination and the combinations
   stored for authentication.
   
   Attributes:
       ipAddress: The IP address of the peer that initiated the connection.
           
           This may
           be the client that originated the session, or it may be an intervening
           proxy if the binding uses a protocol that supports proxies, such as HTTP.
   """
   ipAddress: str

class CanceledHostOperationEvent(HostEvent):
   """
   An operation performed on the host was canceled.
   
   Typically,
   a previous event in the sequence of events contains more
   information about the cause of this cancellation.
   """
   pass


class ChangesInfoEventArgument(pyVmomi.vmodl.DynamicData):
   """
   The event argument contains changes.
   
   Attributes:
       modified: Modified properties.
       added: Added properties.
       deleted: Deleted properties.
   """
   modified: _typing.Optional[str] = None
   added: _typing.Optional[str] = None
   deleted: _typing.Optional[str] = None

class ClusterEvent(Event):
   """These are cluster events."""
   pass

class ClusterComplianceCheckedEvent(ClusterEvent):
   """
   This event records that a compliance check was triggered
   on the cluster.
   """
   profile: ProfileEventArgument

class ClusterCreatedEvent(ClusterEvent):
   """
   This event records when a cluster is created.
   
   Attributes:
       parent: The folder where the cluster is created.
   """
   parent: FolderEventArgument

class ClusterDestroyedEvent(ClusterEvent):
   """This event records when a cluster is destroyed."""
   pass

class ClusterOvercommittedEvent(ClusterEvent):
   """
   This event records when a cluster's host capacity cannot satisfy resource
   configuration constraints.
   """
   pass


class ClusterReconfiguredEvent(ClusterEvent):
   """
   This event records when a cluster is reconfigured.
   
   Attributes:
       configChanges: The configuration values changed during the reconfiguration.
   """
   configChanges: _typing.Optional[ChangesInfoEventArgument] = None

class ClusterStatusChangedEvent(ClusterEvent):
   """
   This event records when a cluster's overall status changed.
   
   Attributes:
       oldStatus: The old (`pyVmomi.vim.ManagedEntity.overallStatus`).
       newStatus: The new (`pyVmomi.vim.ManagedEntity.overallStatus`).
   """
   oldStatus: str
   newStatus: str


class ComputeResourceEventArgument(EntityEventArgument):
   """
   The event argument is a ComputeResource object.
   
   Attributes:
       computeResource: The ComputeResource object.
   """
   computeResource: pyVmomi.vim.ComputeResource

class CustomFieldEvent(Event):
   """These are custom field events."""
   pass

class CustomFieldDefEvent(CustomFieldEvent):
   """
   This event records a custom field definition event.
   
   Attributes:
       fieldKey: The unique identifier of the custom field definition.
       name: The name of the custom field.
   """
   fieldKey: int
   name: str

class CustomFieldDefAddedEvent(CustomFieldDefEvent):
   """This event records the addition of a custom field definition."""
   pass

class CustomFieldDefRemovedEvent(CustomFieldDefEvent):
   """This event records the removal of a custom field definition."""
   pass

class CustomFieldDefRenamedEvent(CustomFieldDefEvent):
   """This event records the renaming of a custom field definition."""
   newName: str


class CustomFieldValueChangedEvent(CustomFieldEvent):
   """
   This event records a change to a custom field value for a particular entity.
   
   Attributes:
       entity: The entity on which the field value was changed.
       fieldKey: The custom field whose value was changed for the entity.
       name: The name of the custom field at the time the value was changed.
       value: The new value that was set.
       prevState: The previous service state.
   """
   entity: ManagedEntityEventArgument
   fieldKey: int
   name: str
   value: str
   prevState: _typing.Optional[str] = None

class VmEvent(Event):
   """
   These are virtual machine events.
   
   Attributes:
       template: Indicates whether or not the virtual machine is marked as a template.
   """
   template: bool


class CustomizationEvent(VmEvent):
   """
   Base for customization events.
   
   Attributes:
       logLocation: The location of the in-guest customization log which will contain
           details of the customization operation.
   """
   logLocation: _typing.Optional[str] = None


class CustomizationFailed(CustomizationEvent):
   """
   The customization sequence in the guest failed.
   
   Attributes:
       reason: Reason why the customization failed @see CustomizationFailed.ReasonCode .
   """
   class ReasonCode(pyVmomi.VmomiSupport.Enum):
      """
      Attributes:
          userDefinedScriptDisabled: The user defined script is disabled during customization
          customizationDisabled: The guest customization is disabled by VMware Tools
              
              Since: vSphere API Release 7.0.1.0
          rawDataIsNotSupported: The cloud-init version is too old to support cloud-init raw data
              
              Since: vSphere API Release 7.0.3.0
          wrongMetadataFormat: The cloud-init meta data is not valid format
              
              Since: vSphere API Release 7.0.3.0
      """
      userDefinedScriptDisabled: _typing.ClassVar['CustomizationFailed.ReasonCode'] = 'userDefinedScriptDisabled'
      customizationDisabled: _typing.ClassVar['CustomizationFailed.ReasonCode'] = 'customizationDisabled'
      rawDataIsNotSupported: _typing.ClassVar['CustomizationFailed.ReasonCode'] = 'rawDataIsNotSupported'
      wrongMetadataFormat: _typing.ClassVar['CustomizationFailed.ReasonCode'] = 'wrongMetadataFormat'

   reason: _typing.Optional[str] = None

class CustomizationLinuxIdentityFailed(CustomizationFailed):
   """Failed to set Linux identity."""
   pass

class CustomizationNetworkSetupFailed(CustomizationFailed):
   """Network setup failed in the guest during customization."""
   pass

class CustomizationStartedEvent(CustomizationEvent):
   """The customization sequence has started in the VM guest."""
   pass

class CustomizationSucceeded(CustomizationEvent):
   """The customization sequence completed successfully in the guest."""
   pass

class CustomizationSysprepFailed(CustomizationFailed):
   """
   Sysprep failed to run in the guest during customization.
   
   This will most like
   have been caused by the fact that the wrong sysprep was used for the guest,
   so we include the version information in the event.
   
   Attributes:
       sysprepVersion: The version string for the sysprep files that were included in the
           customization package.
       systemVersion: The version string for the system
   """
   sysprepVersion: str
   systemVersion: str

class CustomizationUnknownFailure(CustomizationFailed):
   """The customization sequence failed unexpectedly in the guest."""
   pass

class DVPortgroupEvent(Event):
   """DVPortgroup related events."""
   pass

class DVPortgroupCreatedEvent(DVPortgroupEvent):
   """Two distributed virtual portgroup was created."""
   pass

class DVPortgroupDestroyedEvent(DVPortgroupEvent):
   """Two distributed virtual portgroup was destroyed."""
   pass


class DVPortgroupReconfiguredEvent(DVPortgroupEvent):
   """
   Two distributed virtual portgroup was reconfigured.
   
   Attributes:
       configSpec: The reconfiguration spec.
       configChanges: The configuration values changed during the reconfiguration.
   """
   configSpec: pyVmomi.vim.dvs.DistributedVirtualPortgroup.ConfigSpec
   configChanges: _typing.Optional[ChangesInfoEventArgument] = None

class DVPortgroupRenamedEvent(DVPortgroupEvent):
   """
   Two distributed virtual portgroup was renamed.
   
   Attributes:
       oldName: The old portgroup name.
       newName: The new portgroup name.
   """
   oldName: str
   newName: str

class DasAdmissionControlDisabledEvent(ClusterEvent):
   """
   This event records when admission control checks have been disabled in a HA
   cluster.
   """
   pass

class DasAdmissionControlEnabledEvent(ClusterEvent):
   """This event records when admission control checks have been enabled in a HA cluster."""
   pass

class DasAgentFoundEvent(ClusterEvent):
   """
   Deprecated: As of vSphere API 5.0, the event is no longer relevant.This event records that VirtualCenter has re-established contact with a
   primary host in this HA cluster.
   """
   pass

class DasAgentUnavailableEvent(ClusterEvent):
   """
   Deprecated: As of vSphere API 5.0, the event is no longer relevant.This event records that VirtualCenter cannot contact any primary host
   in this HA cluster.
   
   HA designates some hosts as primary hosts in the HA
   cluster. When adding a new host to an existing cluster, HA needs to
   contact one of the primary hosts to finish the configuration. VirtualCenter
   has lost contact with all primary nodes in the connected state. Attempts
   to configure HA on a host in this cluster will fail until a
   DasAgentFoundEvent is logged or unless this is the first node to be
   configured. For example, if all the other hosts are disconnected first.
   """
   pass

class DasClusterIsolatedEvent(ClusterEvent):
   """
   This event records that all hosts have been isolated from the network in a
   HA cluster.
   """
   pass

class DasDisabledEvent(ClusterEvent):
   """This event records when a cluster has been disabled for HA."""
   pass

class DasEnabledEvent(ClusterEvent):
   """This event records when a cluster has been enabled for HA."""
   pass

class DasHostFailedEvent(ClusterEvent):
   """
   This event records when a host failure has been detected by HA.
   
   Attributes:
       failedHost: The host that failed.
   """
   failedHost: HostEventArgument

class DasHostIsolatedEvent(ClusterEvent):
   """
   This event records that a host has been isolated from the network in a
   HA cluster.
   
   Since an isolated host cannot be distinguished from a failed
   host except by the isolated host itself, this event is logged when the
   isolated host regains network connectivity.
   
   Attributes:
       isolatedHost: The host that was isolated.
   """
   isolatedHost: HostEventArgument

class DatacenterEvent(Event):
   """These are datacenter events."""
   pass

class DatacenterCreatedEvent(DatacenterEvent):
   """
   Attributes:
       parent: The folder where the datacenter is created.
   """
   parent: FolderEventArgument


class DatacenterEventArgument(EntityEventArgument):
   """
   The event argument is a Datacenter object.
   
   Attributes:
       datacenter: The Datacenter object.
   """
   datacenter: pyVmomi.vim.Datacenter

class DatacenterRenamedEvent(DatacenterEvent):
   """
   Attributes:
       oldName: The old datacenter name.
       newName: The new datacenter name.
   """
   oldName: str
   newName: str


class DatastoreEvent(Event):
   """
   These are datastore events.
   
   Attributes:
       datastore: The associated datastore.
   """
   datastore: _typing.Optional[DatastoreEventArgument] = None


class DatastoreCapacityIncreasedEvent(DatastoreEvent):
   """
   This event records when increase in a datastore's capacity is observed.
   
   It may happen due to different reasons, like extending or expanding a
   datastore.
   
   Attributes:
       oldCapacity: The old datastore capacity.
       newCapacity: The new datastore capacity.
   """
   oldCapacity: pyVmomi.VmomiSupport.long
   newCapacity: pyVmomi.VmomiSupport.long

class DatastoreDestroyedEvent(DatastoreEvent):
   """This event records when a datastore is removed from VirtualCenter."""
   pass

class DatastoreDiscoveredEvent(HostEvent):
   """
   This event records when a host is added to VirtualCenter
   and datastores are discovered.
   
   Attributes:
       datastore: The associated datastore.
   """
   datastore: DatastoreEventArgument

class DatastoreDuplicatedEvent(DatastoreEvent):
   """
   This event records when a duplicate datastore name is found.
   
   This event is used in VirtualCenter 1.x and is included for
   backward compatibility.
   """
   pass


class DatastoreEventArgument(EntityEventArgument):
   """
   The event argument is a Datastore object.
   
   Attributes:
       datastore: The Datastore object.
   """
   datastore: pyVmomi.vim.Datastore


class DatastoreFileEvent(DatastoreEvent):
   """
   Base class for events related to datastore file and directory
   operations.
   
   Property datastore inherited from DatastoreEvent refers
   to the destination datastore in case there is more than datastore
   involved in the operation.
   
   Attributes:
       targetFile: Datastore path of the target file or directory.
       sourceOfOperation: Identifier of the initiator of the file operation.
       succeeded: Indicator whether the datastore file operation succeeded.
   """
   targetFile: str
   sourceOfOperation: _typing.Optional[str] = None
   succeeded: _typing.Optional[bool] = None

class DatastoreFileCopiedEvent(DatastoreFileEvent):
   """
   This event records copy of a file or directory.
   
   Attributes:
       sourceDatastore: Source datastore.
       sourceFile: Datastore path of the source file or directory.
   """
   sourceDatastore: DatastoreEventArgument
   sourceFile: str

class DatastoreFileDeletedEvent(DatastoreFileEvent):
   """This event records deletion of a file or directory."""
   pass

class DatastoreFileMovedEvent(DatastoreFileEvent):
   """
   This event records move of a file or directory.
   
   Attributes:
       sourceDatastore: Source datastore.
       sourceFile: Datastore path of the source file or directory.
   """
   sourceDatastore: DatastoreEventArgument
   sourceFile: str

class DatastoreIORMReconfiguredEvent(DatastoreEvent):
   """
   This event records that the configuration of storage I/O
   resource management for a datastore has changed.
   """
   pass

class DatastorePrincipalConfigured(HostEvent):
   """This event records that a datastore principal was configured on a host."""
   datastorePrincipal: str

class DatastoreRemovedOnHostEvent(HostEvent):
   """
   This event records when a datastore is removed from a host
   but not from VirtualCenter.
   
   Attributes:
       datastore: The associated datastore.
   """
   datastore: DatastoreEventArgument

class DatastoreRenamedEvent(DatastoreEvent):
   """
   This event records the renaming of a datastore.
   
   Attributes:
       oldName: The old datastore name.
       newName: The new datastore name.
   """
   oldName: str
   newName: str

class DatastoreRenamedOnHostEvent(HostEvent):
   """
   This event records when a datastore is added to VirtualCenter
   and is renamed by VirtualCenter because this datastore already
   exists in VirtualCenter with a different name, or because the
   name conflicts with another datastore in VirtualCenter.
   
   Attributes:
       oldName: The old datastore name.
       newName: The new datastore name.
   """
   oldName: str
   newName: str

class DrsDisabledEvent(ClusterEvent):
   """This event records when DRS is disabled on a cluster."""
   pass

class DrsEnabledEvent(ClusterEvent):
   """
   This event records when DRS is enabled on a cluster.
   
   Attributes:
       behavior: The DRS automation level in (`pyVmomi.vim.cluster.DrsConfigInfo.DrsBehavior`)
   """
   behavior: str

class EnteredStandbyModeEvent(HostEvent):
   """
   This event records that the host has successfully entered
   standby mode.
   
   A host in this mode has no running virtual machines and no
   provisioning operations are occurring.
   """
   pass

class DrsEnteredStandbyModeEvent(EnteredStandbyModeEvent):
   """
   This event records that the host has successfully entered standby mode initiated by
   Distributed Power Management.
   
   A host in this mode has no running virtual
   machines and no provisioning operations are occurring.
   """
   pass

class EnteringStandbyModeEvent(HostEvent):
   """
   This event records that a host has begun the process of entering
   standby mode.
   
   All virtual machine operations
   are blocked, except the following:
   - MigrateVM
   - PowerOffVM
   - SuspendVM
   - ShutdownGuest
   - StandbyGuest
   """
   pass

class DrsEnteringStandbyModeEvent(EnteringStandbyModeEvent):
   """
   This event records that a host has begun the process of
   entering standby mode initiated by Distributed Power Management.
   """
   pass

class ExitStandbyModeFailedEvent(HostEvent):
   """This event records that the host failed to exit standby mode."""
   pass

class DrsExitStandbyModeFailedEvent(ExitStandbyModeFailedEvent):
   """
   This event records that Distributed Power Management tried to bring a host out
   from standby mode, but the host failed to exit standby mode.
   """
   pass

class ExitedStandbyModeEvent(HostEvent):
   """
   This event records that the host is no longer in
   standby mode.
   """
   pass

class DrsExitedStandbyModeEvent(ExitedStandbyModeEvent):
   """
   This event records that Distributed Power Management brings this host
   out from standby mode.
   """
   pass

class ExitingStandbyModeEvent(HostEvent):
   """
   This event records that a host has begun the process of
   exiting standby mode.
   """
   pass

class DrsExitingStandbyModeEvent(ExitingStandbyModeEvent):
   """
   This event records that a host has begun the process of
   exiting standby mode initiated by Distributed Power Management.
   """
   pass

class DrsInvocationFailedEvent(ClusterEvent):
   """This event records DRS invocation failure."""
   pass

class DrsRecoveredFromFailureEvent(ClusterEvent):
   """
   This event records that DRS has recovered from failure.
   
   It is triggered by a successful DRS invocation after repeated failure.
   """
   pass


class DrsResourceConfigureFailedEvent(HostEvent):
   """
   This event records when resource configuration
   specification synchronization fails on a host.
   
   Attributes:
       reason: The reason for the failure.
   """
   reason: pyVmomi.vmodl.MethodFault

class DrsResourceConfigureSyncedEvent(HostEvent):
   """
   This event records when resource configuration
   specification returns to synchronized from previous failure.
   """
   pass

class DrsRuleComplianceEvent(VmEvent):
   """Deprecated: As of vSphere API 9.1, DRS no longer fires this event.This event records when a virtual machine comes into compliance with DRS rules."""
   pass

class DrsRuleViolationEvent(VmEvent):
   """This event records when a virtual machine violates a DRS VM-Host rule."""
   pass

class DrsSoftRuleViolationEvent(VmEvent):
   """This event records when a virtual machine violates a soft VM-Host rule."""
   pass


class VmMigratedEvent(VmEvent):
   """
   This event records a virtual machine migration.
   
   Attributes:
       sourceHost: The source host.
           
           (Because this is after a successful migration,
           the destination host is recorded in the inherited \"host\" property.)
       sourceDatacenter: The source datacenter
       sourceDatastore: The source primary datastore
   """
   sourceHost: HostEventArgument
   sourceDatacenter: _typing.Optional[DatacenterEventArgument] = None
   sourceDatastore: _typing.Optional[DatastoreEventArgument] = None

class DrsVmMigratedEvent(VmMigratedEvent):
   """This event records a virtual machine migration that was recommended by DRS."""
   pass

class VmPoweredOnEvent(VmEvent):
   """This event records when a virtual machine finished powering on."""
   pass

class DrsVmPoweredOnEvent(VmPoweredOnEvent):
   """This event records when a virtual machine is powered on by DRS."""
   pass

class DuplicateIpDetectedEvent(HostEvent):
   """
   This event records that a duplicate IP address has been observed in
   conflict with the vmotion or IP storage interface configured on the
   host.
   
   Attributes:
       duplicateIP: The Duplicate IP address detected.
       macAddress: The MAC associated with duplicate IP.
   """
   duplicateIP: str
   macAddress: str

class DvpgImportEvent(DVPortgroupEvent):
   """
   This event is generated when an import operation is
   performed on a distributed virtual portgroup
   
   Attributes:
       importType: The type of restore operation.
           
           See `pyVmomi.vim.dvs.EntityBackup.ImportType` for valid values
   """
   importType: str

class DvpgRestoreEvent(DVPortgroupEvent):
   """
   This event is generated when a restore operation is
   performed on a distributed virtual portgroup
   """
   pass


class DvsEvent(Event):
   """These are dvs-related events."""
   class PortBlockState(pyVmomi.VmomiSupport.Enum):
      """
      The port blocked/unblocked state.
      
      Attributes:
          unset: The dvs port is in unset state
          blocked: The dvs port is in blocked state
          unblocked: The dvs port is in unblocked state
          unknown: The dvs port is in unknown state
      """
      unset: _typing.ClassVar['DvsEvent.PortBlockState'] = 'unset'
      blocked: _typing.ClassVar['DvsEvent.PortBlockState'] = 'blocked'
      unblocked: _typing.ClassVar['DvsEvent.PortBlockState'] = 'unblocked'
      unknown: _typing.ClassVar['DvsEvent.PortBlockState'] = 'unknown'

class DvsCreatedEvent(DvsEvent):
   """
   A distributed virtual switch was created.
   
   Attributes:
       parent: The folder where the DistributedVirtualSwitch is created.
   """
   parent: FolderEventArgument

class DvsDestroyedEvent(DvsEvent):
   """A distributed virtual switch was destroyed."""
   pass


class DvsEventArgument(EntityEventArgument):
   """
   The event argument is a distributed virtual switch object.
   
   Attributes:
       dvs: The distributed virtual switch object.
   """
   dvs: pyVmomi.vim.DistributedVirtualSwitch


class DvsHealthStatusChangeEvent(HostEvent):
   """
   Health check status of an switch is changed.
   
   Attributes:
       switchUuid: UUID of the DVS the host is connected to.
       healthResult: Health check status.
   """
   switchUuid: str
   healthResult: _typing.Optional[pyVmomi.vim.dvs.HostMember.HealthCheckResult] = None

class DvsHostBackInSyncEvent(DvsEvent):
   """
   The DVS configuration on the host was synchronized with that of
   the Virtual Center Server and the configuration is the same on
   the host and Virtual Center Server.
   
   Attributes:
       hostBackInSync: The host that was synchronized.
   """
   hostBackInSync: HostEventArgument

class DvsHostJoinedEvent(DvsEvent):
   """
   A host joined the distributed virtual switch.
   
   Attributes:
       hostJoined: The host that joined DVS.
   """
   hostJoined: HostEventArgument

class DvsHostLeftEvent(DvsEvent):
   """
   A host left the distributed virtual switch.
   
   Attributes:
       hostLeft: The host that left DVS.
   """
   hostLeft: HostEventArgument


class DvsHostStatusUpdated(DvsEvent):
   """
   A host has it's status or statusDetail updated.
   
   Attributes:
       hostMember: The host.
       oldStatus: Host's old status.
       newStatus: Host's new status.
       oldStatusDetail: Comments regarding host's old status.
       newStatusDetail: Comments regarding host's new status.
   """
   hostMember: HostEventArgument
   oldStatus: _typing.Optional[str] = None
   newStatus: _typing.Optional[str] = None
   oldStatusDetail: _typing.Optional[str] = None
   newStatusDetail: _typing.Optional[str] = None

class DvsHostWentOutOfSyncEvent(DvsEvent):
   """
   The DVS configuration on the host diverged from that of
   the Virtual Center Server.
   
   Attributes:
       hostOutOfSync: The host that went out of sync.
   """
   hostOutOfSync: DvsOutOfSyncHostArgument

class DvsImportEvent(DvsEvent):
   """
   This event is generated when a import operation is
   performed on a distributed virtual switch
   
   Attributes:
       importType: The type of restore operation.
           
           See `pyVmomi.vim.dvs.EntityBackup.ImportType` for valid values
   """
   importType: str

class DvsMergedEvent(DvsEvent):
   """
   Two distributed virtual switches was merged.
   
   Attributes:
       sourceDvs: The source DVS.
       destinationDvs: The destination DVS.
   """
   sourceDvs: DvsEventArgument
   destinationDvs: DvsEventArgument


class DvsOutOfSyncHostArgument(pyVmomi.vmodl.DynamicData):
   """
   The host on which the DVS configuration is different from that
   of Virtual Center server.
   
   Attributes:
       outOfSyncHost: The host.
       configParamters: The DVS configuration parameters that are different between
           Virtual Center server and the host.
   """
   outOfSyncHost: HostEventArgument
   configParamters: list[str] = []


class DvsPortBlockedEvent(DvsEvent):
   """
   A port is blocked in the distributed virtual switch.
   
   Attributes:
       portKey: The port key.
       statusDetail: Reason for port's current status
       runtimeInfo: The port runtime information.
       prevBlockState: Previous state of the DvsPort.
           
           See `pyVmomi.vim.event.DvsEvent.PortBlockState`
   """
   portKey: str
   statusDetail: _typing.Optional[str] = None
   runtimeInfo: _typing.Optional[pyVmomi.vim.dvs.DistributedVirtualPort.RuntimeInfo] = None
   prevBlockState: _typing.Optional[str] = None


class DvsPortConnectedEvent(DvsEvent):
   """
   A port is connected in the distributed virtual switch.
   
   Attributes:
       portKey: The port key.
       connectee: The port's connectee.
   """
   portKey: str
   connectee: _typing.Optional[pyVmomi.vim.dvs.PortConnectee] = None

class DvsPortCreatedEvent(DvsEvent):
   """
   New ports are created in the distributed virtual switch.
   
   Attributes:
       portKey: The key of the ports that are created.
   """
   portKey: list[str] = []

class DvsPortDeletedEvent(DvsEvent):
   """
   Existing ports are deleted in the distributed virtual switch.
   
   Attributes:
       portKey: The key of the ports that are deleted.
   """
   portKey: list[str] = []


class DvsPortDisconnectedEvent(DvsEvent):
   """
   A port is disconnected in the distributed virtual switch.
   
   Attributes:
       portKey: The port key.
       connectee: The port's formal connectee.
   """
   portKey: str
   connectee: _typing.Optional[pyVmomi.vim.dvs.PortConnectee] = None


class DvsPortEnteredPassthruEvent(DvsEvent):
   """
   A port has entered passthrough mode on the distributed virtual switch.
   
   Attributes:
       portKey: The port key.
       runtimeInfo: The port runtime information.
   """
   portKey: str
   runtimeInfo: _typing.Optional[pyVmomi.vim.dvs.DistributedVirtualPort.RuntimeInfo] = None


class DvsPortExitedPassthruEvent(DvsEvent):
   """
   A port has exited passthrough mode on the distributed virtual switch.
   
   Attributes:
       portKey: The port key.
       runtimeInfo: The port runtime information.
   """
   portKey: str
   runtimeInfo: _typing.Optional[pyVmomi.vim.dvs.DistributedVirtualPort.RuntimeInfo] = None

class DvsPortJoinPortgroupEvent(DvsEvent):
   """
   A port was moved into the distributed virtual portgroup.
   
   Attributes:
       portKey: The port key.
       portgroupKey: The portgroup key.
       portgroupName: The portgroup name.
   """
   portKey: str
   portgroupKey: str
   portgroupName: str

class DvsPortLeavePortgroupEvent(DvsEvent):
   """
   A port was moved out of the distributed virtual portgroup.
   
   Attributes:
       portKey: The port key.
       portgroupKey: The portgroup key.
       portgroupName: The portgroup name.
   """
   portKey: str
   portgroupKey: str
   portgroupName: str


class DvsPortLinkDownEvent(DvsEvent):
   """
   A port of which link status is changed to down in the distributed
   virtual switch.
   
   Attributes:
       portKey: The port key.
       runtimeInfo: The port runtime information.
   """
   portKey: str
   runtimeInfo: _typing.Optional[pyVmomi.vim.dvs.DistributedVirtualPort.RuntimeInfo] = None


class DvsPortLinkUpEvent(DvsEvent):
   """
   A port of which link status is changed to up in the distributed
   virtual switch.
   
   Attributes:
       portKey: The port key.
       runtimeInfo: The port runtime information.
   """
   portKey: str
   runtimeInfo: _typing.Optional[pyVmomi.vim.dvs.DistributedVirtualPort.RuntimeInfo] = None


class DvsPortReconfiguredEvent(DvsEvent):
   """
   Existing ports are reconfigured in the distributed virtual switch.
   
   Attributes:
       portKey: The key of the ports that are reconfigured.
       configChanges: The configuration values changed during the reconfiguration.
   """
   portKey: list[str] = []
   configChanges: list[ChangesInfoEventArgument] = []


class DvsPortRuntimeChangeEvent(DvsEvent):
   """
   A port of which runtime information is changed in the vNetwork Distributed
   Switch.
   
   Attributes:
       portKey: The port key.
       runtimeInfo: The new port runtime information.
   """
   portKey: str
   runtimeInfo: pyVmomi.vim.dvs.DistributedVirtualPort.RuntimeInfo


class DvsPortUnblockedEvent(DvsEvent):
   """
   A port is unblocked in the distributed virtual switch.
   
   Attributes:
       portKey: The port key.
       runtimeInfo: The port runtime information.
       prevBlockState: Previous state of the DvsPort.
           
           See `pyVmomi.vim.event.DvsEvent.PortBlockState`
   """
   portKey: str
   runtimeInfo: _typing.Optional[pyVmomi.vim.dvs.DistributedVirtualPort.RuntimeInfo] = None
   prevBlockState: _typing.Optional[str] = None

class DvsPortVendorSpecificStateChangeEvent(DvsEvent):
   """
   A port of which vendor specific state is changed in the vNetwork Distributed
   Switch.
   
   Attributes:
       portKey: The port key.
   """
   portKey: str


class DvsReconfiguredEvent(DvsEvent):
   """
   A distributed virtual switch was reconfigured.
   
   Attributes:
       configSpec: The reconfiguration spec.
       configChanges: The configuration values changed during the reconfiguration.
   """
   configSpec: pyVmomi.vim.DistributedVirtualSwitch.ConfigSpec
   configChanges: _typing.Optional[ChangesInfoEventArgument] = None

class DvsRenamedEvent(DvsEvent):
   """
   A distributed virtual switch was renamed.
   
   Attributes:
       oldName: The old DistributedVirtualSwitch name.
       newName: The new DistributedVirtualSwitch name.
   """
   oldName: str
   newName: str

class DvsRestoreEvent(DvsEvent):
   """
   This event is generated when a restore operation is
   performed on a distributed virtual switch
   """
   pass


class DvsUpgradeAvailableEvent(DvsEvent):
   """
   An upgrade for the distributed virtual switch is available.
   
   Attributes:
       productInfo: The product info of the upgrade.
   """
   productInfo: pyVmomi.vim.dvs.ProductSpec


class DvsUpgradeInProgressEvent(DvsEvent):
   """
   An upgrade for the distributed virtual switch is in progress.
   
   Attributes:
       productInfo: The product info of the upgrade.
   """
   productInfo: pyVmomi.vim.dvs.ProductSpec


class DvsUpgradeRejectedEvent(DvsEvent):
   """
   An upgrade for the distributed virtual switch is rejected.
   
   Attributes:
       productInfo: The product info of the upgrade.
   """
   productInfo: pyVmomi.vim.dvs.ProductSpec


class DvsUpgradedEvent(DvsEvent):
   """
   The distributed virtual switch was upgraded.
   
   Attributes:
       productInfo: The product info of the upgrade.
   """
   productInfo: pyVmomi.vim.dvs.ProductSpec

class EnteredMaintenanceModeEvent(HostEvent):
   """
   This event records that the host has completely entered
   maintenance mode.
   
   A host in this mode has no running virtual machines and no
   provisioning operations are occurring.
   """
   pass

class EnteringMaintenanceModeEvent(HostEvent):
   """
   This event records that a host has begun the process of entering
   maintenance mode.
   
   All virtual machine operations
   are blocked, except the following:
   - MigrateVM
   - PowerOffVM
   - SuspendVM
   - ShutdownGuest
   - StandbyGuest
   """
   pass

class UpgradeEvent(Event):
   """
   These event types represent events converted from VirtualCenter 1.x.
   
   All upgraded events are converted to string values.
   
   Attributes:
       message: The formatted message from the upgrade.
   """
   message: str

class ErrorUpgradeEvent(UpgradeEvent):
   """This event is a general error event from upgrade."""
   pass


class EventDescription(pyVmomi.vmodl.DynamicData):
   """
   This data object provides static, locale-specific strings for event objects.
   
   Attributes:
       category: `pyVmomi.vim.event.EventDescription.EventCategory`
       eventInfo: The event class description details.
       enumeratedTypes: Localized descriptions of all enumerated types that are used for
           member declarations in event classes.
   """
   class EventCategory(pyVmomi.VmomiSupport.Enum):
      """
      Attributes:
          info: Returns informational events.
          warning: Returns warning events.
          error: Returns error events.
          user: Returns events pertaining to users.
      """
      info: _typing.ClassVar['EventDescription.EventCategory'] = 'info'
      warning: _typing.ClassVar['EventDescription.EventCategory'] = 'warning'
      error: _typing.ClassVar['EventDescription.EventCategory'] = 'error'
      user: _typing.ClassVar['EventDescription.EventCategory'] = 'user'

   class EventArgDesc(pyVmomi.vmodl.DynamicData):
      """
      Describes an available event argument name for an Event type, which
      can be used in `pyVmomi.vim.alarm.EventAlarmExpression`.
      
      Attributes:
          name: The name of the argument
          type: The type of the argument.
          description: The localized description of the event argument.
              
              The key holds
              the localization prefix for the argument, which is decided by
              the Event type that it is actually declared in, which may be a
              base type of this event type.
      """
      name: str
      type: str
      description: _typing.Optional[pyVmomi.vim.ElementDescription] = None

   class EventDetail(pyVmomi.vmodl.DynamicData):
      """
      Each Event object provides an automatic event message string through
      its `pyVmomi.vim.event.Event.fullFormattedMessage`
      property.
      
      However, you can use the EventDetail object's properties to
      format an event message string that is appropriate when viewed from
      a specific context. The variable information (vm.name, and so on) is
      derived from the Event object's event arguments
      (`pyVmomi.vim.event.Event.vm`, and so on).
      
      Attributes:
          key: Type of event being described.
          description: A string that is a short human-parseable description of the event.
              
              This is not the full message string (which may contain details
              of the arguments, etc.), but merely a more understandable, and
              localized, description of what the event stands for. It is meant
              for contexts where the name of the event has to be displayed
              to end-users, e.g. when creating Event-based Alarms.
              ` * 
              
              E.g., for `pyVmomi.vim.event.VmPoweredOnEvent`, the eventDescription
              in English might say \"VM Powered On\".
          category: A category of events.
          formatOnDatacenter: A string that is appropriate in the context of a specific
              Datacenter.
              
              For example, a renaming event in this context produces
              the following string:
              
              \"Renamed {vm.name} from {oldName} to {newName}\"
              
              where `pyVmomi.vim.event.VmRenamedEvent.oldName` and
              `pyVmomi.vim.event.VmRenamedEvent.newName` are properties of the
              VmRenamedEvent object.
          formatOnComputeResource: A string that is appropriate in the context of a specific cluster.
              
              For example, a powering on event in this context produces the
              following string:
              
              \"{vm.name} on {host.name} is powered on\".
          formatOnHost: A string that is appropriate in the context
              of a specific Host.
              
              For example, a powering on event in this
              context produces the following string:
              
              \"{vm.name} is powered on\"
          formatOnVm: A string that is appropriate for the context of a specific
              virtual machine.
              
              For example, a powering on event in this context
              produces the following string:
              
              \"Virtual machine on {host.name} is powered on\"
          fullFormat: A string whose context is not entity-specific.
              
              For example, a
              powering on event produces the following string:
              
              \"{vm.name} on {host.name} in {datacenter.name} is powered on\"
          longDescription: A detailed description of the event.
              
              It includes common causes
              and actions to remediate them. It may also include links to kb
              articles and other diagnostic information.
              For example, the BadUserNameSessionEvent may produce the
              following string:
              
                       <EventLongDescription id=\"vim.event.BadUserNameSessionEvent\">
                          <description>
                             The user could not be logged in because of an unknown or invalid
                             user name.
                          </description>
                          <cause>
                             <description>The user name was unknown to the system</description>
                             <action>Use a user name known to the system user directory</action>
                             <action>(On Linux) Check if the user directory is correctly
                                     configured.</action>
                             <action>Check the health of the domain controller (if you are using
                                     Active Directory)</action>
                          </cause>
                          <cause>
                             <description>The user provided an invalid password</description>
                             <action>Supply the correct password</action>
                          </cause>
                       </EventLongDescription>
      """
      key: type
      description: _typing.Optional[str] = None
      category: str
      formatOnDatacenter: str
      formatOnComputeResource: str
      formatOnHost: str
      formatOnVm: str
      fullFormat: str
      longDescription: _typing.Optional[str] = None

   category: list[pyVmomi.vim.ElementDescription] = []
   eventInfo: list[EventDescription.EventDetail] = []
   enumeratedTypes: list[pyVmomi.vim.EnumDescription] = []


class EventEx(Event):
   """
   EventEx is a dynamically typed Event class, whose type is indicated by its
   eventTypeId property.
   
   A collection of eventTypeIds is registered by Extensions, which can now
   pass in optional type information for each eventTypeId which indicates the
   applicable argument names and types, among other properties.
   
   EventEx allows event arguments of any type, though today, the system
   only supports \"string\" and \"moid\" (a string which can be interpreted as an
   object ID in the system) as argument types. In the future, the system
   may optionally strongly check the types of the arguments in the event
   against the declared type information, based on how the event type is
   declared.
   
   EventEx also allows arbitrary \"event object\"s - the object which the
   event refers to. You can put in any object identifier as the objectId,
   but objectType should be filled in only if the object is actually present
   in the VC Server's ManagedEntity inventory.
   
   Attributes:
       eventTypeId: The type of the event.
       severity: The severity level of the message: null=>info.
       message: An arbitrary message string, not localized.
       arguments: The event arguments associated with the event
       objectId: The ID of the object (VM, Host, Folder..) which the event pertains to.
           
           Federated or local inventory path.
       objectType: the type of the object, if known to the VirtualCenter inventory
       objectName: The name of the object
       fault: The fault that triggered the event, if any
   """
   eventTypeId: str
   severity: _typing.Optional[str] = None
   message: _typing.Optional[str] = None
   arguments: list[pyVmomi.vmodl.KeyAnyValue] = []
   objectId: _typing.Optional[str] = None
   objectType: _typing.Optional[type] = None
   objectName: _typing.Optional[str] = None
   fault: _typing.Optional[pyVmomi.vmodl.MethodFault] = None


class EventFilterSpec(pyVmomi.vmodl.DynamicData):
   """
   Event filter used to query events in the history collector database.
   
   The client creates an event history collector with a filter specification,
   then retrieves the events from the event history collector.
   
   Attributes:
       entity: The filter specification for retrieving events by managed entity.
           
           If the property is not set, then events attached to all managed entities
           are collected.
       time: The filter specification for retrieving tasks by time.
           
           If the property is not set, then events with any time stamp are collected.
       userName: The filter specification for retrieving events by username.
           
           If the property is not set, then events belonging to any user are collected.
       eventChainId: The filter specification for retrieving events by chain ID.
           
           If the property is not set, events with any chain ID are collected.
       alarm: This property, if set, limits the set of collected events to those
           associated with the specified alarm.
           
           If the property is not set, events are collected regardless of their
           association with alarms.
       scheduledTask: This property, if set, limits the set of collected events to those
           associated with the specified scheduled task.
           
           If the property is not set, events are collected regardless of their
           association with any scheduled task.
       disableFullMessage: Flag to specify whether or not to prepare the full formatted message
           for each event.
           
           If the property is not set, the collected events do not include
           the full formatted message.
       category: This property, if set, limits the set of collected events to those
           associated with the specified category.
           
           If the property is not set, events are collected regardless of their
           association with any category.
           \"category\" here is the same as Event.severity.
       type: This property, if set, limits the set of collected events to those
           specified types.
           
           If the property is not set, events are collected regardless of their
           types.
       tag: This property, if set, limits the set of filtered events to those that
           have it.
           
           If not set, or the size of it 0, the tag of an event is
           disregarded. A blank string indicates events without tags.
       eventTypeId: This property, if set, limits the set of collected events to those
           specified types.
           
           Note: if both `pyVmomi.vim.event.EventFilterSpec.eventTypeId` and `pyVmomi.vim.event.EventFilterSpec.type` are specified, an
           exception may be thrown by `pyVmomi.vim.event.EventManager.createCollector`.
           
           The semantics of how eventTypeId matching is done is as follows:
           - If the event being collected is of type `pyVmomi.vim.event.EventEx`
             or `pyVmomi.vim.event.ExtendedEvent`, then we match against the
             `eventTypeId` (for `EventEx`) or
             `eventId` (for `ExtendedEvent`) member of the Event.
           - Otherwise, we match against the type of the Event itself.
             
           If neither this property, nor `type`, is set, events are
           collected regardless of their types.
       maxCount: This property, if set, specifies the maximum number of returned events.
           
           If unset, the default maximum number will be used.
           Using this property with `pyVmomi.vim.event.EventManager.createCollector` is more
           efficient than a call to `pyVmomi.vim.HistoryCollector.setLatestPageSize`.
       delayedInit: This property, if set, specifies whether latest page should be populated on Collector creation.
           
           True for delayed population and false for immediate.
           If unset, the latest page is populated immediately.
           
           Since: vSphere API Release 8.0.3.0
       auditable: Allows the client to collect only auditable events.
           
           If True, collects only auditable events, i.e., `pyVmomi.vim.event.Event.auditId` is set.
           If False, collects only not auditable events, i.e., `pyVmomi.vim.event.Event.auditId` is unset.
           Mutually exclusive with `pyVmomi.vim.event.EventFilterSpec.auditId`.
           
           Since: vSphere API Release 9.1.0.0
       auditId: Allows the client to collect specific auditable events.
           
           If set, returns only events for which
           `Event.auditId` is in the `pyVmomi.vim.event.EventFilterSpec.auditId` list.
           Mutually exclusive with `pyVmomi.vim.event.EventFilterSpec.auditable`.
           
           Since: vSphere API Release 9.1.0.0
   """
   class RecursionOption(pyVmomi.VmomiSupport.Enum):
      """
      This option specifies how to select events based on child relationships
      in the inventory hierarchy.
      
      If a managed entity has children, their events
      can be retrieved with this filter option.
      
      Attributes:
          self: Returns events that pertain only to the specified managed entity,
              and not its children.
          children: Returns events pertaining to child entities only.
              
              Excludes
              events pertaining to the specified managed entity itself.
          all: Returns events pertaining either to the specified managed entity
              or to its child entities.
      """
      self: _typing.ClassVar['EventFilterSpec.RecursionOption'] = 'self'
      children: _typing.ClassVar['EventFilterSpec.RecursionOption'] = 'children'
      all: _typing.ClassVar['EventFilterSpec.RecursionOption'] = 'all'

   class ByEntity(pyVmomi.vmodl.DynamicData):
      """
      This option specifies a managed entity used to filter event history.
      
      If the specified managed entity is a Folder or a ResourcePool, the query
      will actually be performed on the entities contained within that Folder
      or ResourcePool, so you cannot query for events on Folders and
      ResourcePools themselves this way.
      
      Attributes:
          entity: The managed entity to which the event pertains.
          recursion: Specification of related managed entities in the inventory hierarchy.
      """
      entity: pyVmomi.vim.ManagedEntity
      recursion: EventFilterSpec.RecursionOption

   class ByTime(pyVmomi.vmodl.DynamicData):
      """
      This option specifies a time range used to filter event history.
      
      Attributes:
          beginTime: The beginning of the time range.
              
              If this property is not set, then events are collected from
              the earliest time in the database.
          endTime: The end of the time range.
              
              If this property is not specified, then events are collected up to
              the latest time in the database.
      """
      beginTime: _typing.Optional[_datetime.datetime] = None
      endTime: _typing.Optional[_datetime.datetime] = None

   class ByUsername(pyVmomi.vmodl.DynamicData):
      """
      This option specifies users used to filter event history.
      
      Attributes:
          systemUser: filter by system user
              true for system user event
          userList: all interested username list
              If this property is not set, then all regular user events are
              collected
      """
      systemUser: bool
      userList: list[str] = []

   entity: _typing.Optional[EventFilterSpec.ByEntity] = None
   time: _typing.Optional[EventFilterSpec.ByTime] = None
   userName: _typing.Optional[EventFilterSpec.ByUsername] = None
   eventChainId: _typing.Optional[int] = None
   alarm: _typing.Optional[pyVmomi.vim.alarm.Alarm] = None
   scheduledTask: _typing.Optional[pyVmomi.vim.scheduler.ScheduledTask] = None
   disableFullMessage: _typing.Optional[bool] = None
   category: list[str] = []
   type: list[type] = []
   tag: list[str] = []
   eventTypeId: list[str] = []
   maxCount: _typing.Optional[int] = None
   delayedInit: _typing.Optional[bool] = None
   auditable: _typing.Optional[bool] = None
   auditId: list[str] = []


class EventHistoryCollector(pyVmomi.vim.HistoryCollector):
   """
   EventHistoryCollector provides a mechanism for
   retrieving historical data and updates when the server appends new
   events.
   """
   @property
   def latestPage(self) -> list[Event]:
      """
      The items in the 'viewable latest page'.
      
      As new events that match the
      collector's `pyVmomi.vim.event.EventFilterSpec` are created, they are added to this
      page, and the oldest events are removed from the collector to keep the
      size of the page to that allowed by
      `pyVmomi.vim.HistoryCollector.setLatestPageSize`.
      
      The \"oldest event\" is the one with the smallest key (event ID). The
      events in the returned page are unordered.
      While `initialized` is `false` this property will remain empty and once the Collector is initialized it will be populated.
      While `initialized` is `true` this property is populated immediately.
      """
      ...
   @property
   def initialized(self) -> _typing.Optional[bool]:
      """
      Indicates whether the `pyVmomi.vim.event.EventHistoryCollector.latestPage` is initialized.
      
      If the
      `pyVmomi.vim.event.EventFilterSpec.delayedInit` is `false` or unset this property is always true.
      
      Since: vSphere API Release 8.0.3.0
      """
      ...

   def ReadNext(self, maxCount: int) -> list[Event]:
      """
      Reads the 'scrollable view' from the current position.
      
      The scrollable
      position is moved to the next newer page after the read. No item is
      returned when the end of the collector is reached.
      
      Args:
          maxCount: The maximum number of items in the page.
      """
      ...
   def ReadPrev(self, maxCount: int) -> list[Event]:
      """
      Reads the 'scrollable view' from the current position.
      
      The scrollable
      position is moved to the next older page after the read. No item is
      returned when the head of the collector is reached.
      
      Args:
          maxCount: The maximum number of items in the page.
      """
      ...


class EventManager(pyVmomi.VmomiSupport.ManagedObject):
   """
   This managed object type provides properties and methods for
   event management support.
   
   Event objects are used to record significant state changes of
   managed entities.
   """
   class EventViewSpec(pyVmomi.vmodl.DynamicData):
      """
      BaseClass allowing different views on filtered set.
      
      Since: vSphere API Release 9.0.0.0
      """
      pass

   class ViewByStartId(EventManager.EventViewSpec):
      """
      Defines the view parameters with starting event ID for the event query.
      
      Attributes:
          startEventId: An integer value specifying the ID of the event from which to start
              the query.
              
              Must be >= 0. The maximum event ID is defined by
              \"config.vpxd.event.maxEventId\" advanced vCenter configuration option
              which has a default value of 2147480000.
          isForward: A boolean flag indicating the direction of the query.
              
              If `true`, the query retrieves events with IDs greater than
              startEventId, representing newer events.
              If `false`, the query retrieves events with IDs less than
              startEventId, representing older events.
      
      Since: vSphere API Release 9.0.0.0
      """
      startEventId: int
      isForward: bool

   @property
   def description(self) -> EventDescription:
      """Static descriptive strings used in events."""
      ...
   @property
   def latestEvent(self) -> _typing.Optional[Event]:
      """The latest event that happened on the VirtualCenter server."""
      ...
   @property
   def maxCollector(self) -> int:
      """
      For each client, the maximum number of event collectors that can exist
      simultaneously.
      """
      ...

   def RetrieveArgumentDescription(self, eventTypeId: str) -> list[EventDescription.EventArgDesc]:
      """Retrieves the argument meta-data for a given Event type"""
      ...
   def CreateCollector(self, filter: EventFilterSpec) -> EventHistoryCollector:
      """
      Creates an event history collector, which is a specialized history collector
      that provides Event objects.
      
      Event collectors do not persist beyond the current client session.
      
      Args:
          filter: The event query filter.
      
      Returns:
          The event collector based on the filter.
      
      Raises:
          pyVmomi.vim.fault.InvalidState: if there are more than the maximum number of
              event collectors.
      """
      ...
   def LogUserEvent(self, entity: pyVmomi.vim.ManagedEntity, msg: str) -> None:
      """
      Logs a user defined event against a particular managed entity.
      
      Args:
          entity: The entity against which the event is logged. The entity must be
              the root folder, a DataCenter, a VirtualMachine, a HostSystem,
              or a ComputeResource.
          msg: The message to be logged.
      """
      ...
   def QueryEvent(self, filter: EventFilterSpec, eventViewSpec: _typing.Optional[EventManager.EventViewSpec]) -> list[Event]:
      """
      Returns events based on the specified `pyVmomi.vim.event.EventFilterSpec` and
      `pyVmomi.vim.event.EventManager.EventViewSpec` parameters.
      
      Returns an empty array when there are
      no events matching the filtering parameters.
      
      Args:
          filter: Defines a filtering criteria for the event query.
          eventViewSpec: Defines the view parameters for the event query.
              
              To retrieve the newest events in the system, use 2147480000
              (or the value of \"config.vpxd.event.maxEventId\" advanced vCenter
              configuration option) as `pyVmomi.vim.event.EventManager.ViewByStartId.startEventId` and
              set `pyVmomi.vim.event.EventManager.ViewByStartId.isForward` to false. To retrieve subsequent
              pages of results with older events, use the smallest event ID
              from the previous response as the `pyVmomi.vim.event.EventManager.ViewByStartId.startEventId`
              and set`pyVmomi.vim.event.EventManager.ViewByStartId.isForward` to false in the next query.
              To retrieve subsequent pages of results with newer events, use
              the biggest event ID from the previous page as the
              `pyVmomi.vim.event.EventManager.ViewByStartId.startEventId` and set
              `pyVmomi.vim.event.EventManager.ViewByStartId.isForward` to true in the next query.
              
              Since: vSphere API Release 9.0.0.0
      
      Returns:
          The events matching the filters.
      """
      ...
   def PostEvent(self, eventToPost: Event, taskInfo: _typing.Optional[pyVmomi.vim.TaskInfo]) -> None:
      """
      Posts the specified event, optionally associating it with
      a task.
      
      The event being posted should have the following info in it:
      - The `pyVmomi.vim.ManagedEntity` on which the event is being posted should
        be set in the appropriate `pyVmomi.vim.event.EntityEventArgument` field of the base
        `pyVmomi.vim.event.Event` class. It is OK to not set any entity, in which case the
        event is treated as an event about the system.
      - Some Event fields (`pyVmomi.vim.event.Event.key`, `pyVmomi.vim.event.Event.chainId`,
        `pyVmomi.vim.event.Event.createdTime`) are mandatory because of the nature of
        the structure, but any caller-supplied values will be overwritten by
        the system.
        
      If the event being posted is to be associated with an existing
      `pyVmomi.vim.Task`, the appropriate `pyVmomi.vim.TaskInfo` needs to be passed in.
      This task can either be one returned from a vSphere API operation or
      an extension task created by calling `pyVmomi.vim.TaskManager.createTask`.
      
      Audit-record posting requires the additional
      `Global.SetAuditId` privilege. A caller is treated as
      posting an audit record (and the additional privilege is enforced)
      when either of the following is true:
      - `pyVmomi.vim.event.Event.auditId` is supplied on the event.
      - The event type is registered in the server's audit-id mapping
        (see `EventManager.auditMappings`); for these types the
        server populates `pyVmomi.vim.event.Event.auditId` automatically.
        
      Callers that hold only `Global.LogEvent` may continue to
      post non-audit events without an explicit auditId.
      
      Args:
          eventToPost: Fully-specified event to post
          taskInfo: optional task associated with the event
      
      Raises:
          pyVmomi.vim.fault.InvalidEvent: no longer thrown by this API
      """
      ...

class ExitMaintenanceModeEvent(HostEvent):
   """
   This event records that the host is no longer in
   maintenance mode.
   """
   pass

class GeneralEvent(Event):
   """
   These are general events.
   
   Attributes:
       message: A short form of the message string, not localized.
   """
   message: str


class ExtendedEvent(GeneralEvent):
   """
   This event is the base class for extended events.
   
   Attributes:
       eventTypeId: The id of the type of extended event.
       managedObject: The object on which the event was logged.
       data: Key/value pairs associated with event.
   """
   class Pair(pyVmomi.vmodl.DynamicData):
      """key/value pair"""
      key: str
      value: str

   eventTypeId: str
   managedObject: pyVmomi.VmomiSupport.ManagedObject
   data: list[ExtendedEvent.Pair] = []

class FailoverLevelRestored(ClusterEvent):
   """
   This event records that the amount of cluster resources has increased
   and is now sufficient to satisfy the configured HA failover level.
   """
   pass


class FolderEventArgument(EntityEventArgument):
   """
   The event argument is a Folder object.
   
   Attributes:
       folder: The Folder object.
   """
   folder: pyVmomi.vim.Folder

class GeneralHostErrorEvent(GeneralEvent):
   """This event is the general error event for a host."""
   pass

class GeneralHostInfoEvent(GeneralEvent):
   """This event is the general information event for a host."""
   pass

class GeneralHostWarningEvent(GeneralEvent):
   """This event is the general warning event for a host."""
   pass


class GeneralUserEvent(GeneralEvent):
   """
   This event is the general user event type.
   
   Attributes:
       entity: The entity on which the event was logged.
   """
   entity: _typing.Optional[ManagedEntityEventArgument] = None

class GeneralVmErrorEvent(GeneralEvent):
   """This event is the general error event for a virtual machine."""
   pass

class GeneralVmInfoEvent(GeneralEvent):
   """This event is the general information event for a virtual machine."""
   pass

class GeneralVmWarningEvent(GeneralEvent):
   """This event is the general warning event for a virtual machine."""
   pass

class GhostDvsProxySwitchDetectedEvent(HostEvent):
   """
   This event records when Virtual Center server found DVS proxy switches
   on the host that don't match any DVS defined in Virtual Center.
   
   Attributes:
       switchUuid: The list of ghost DVS proxy switch uuids that were found.
   """
   switchUuid: list[str] = []

class GhostDvsProxySwitchRemovedEvent(HostEvent):
   """
   This event records when the ghost DVS proxy switches (a.k.a host
   proxy switches that don't match any DVS defined in Virtual Center)
   were removed on the host.
   
   Attributes:
       switchUuid: The list of ghost DVS proxy switch uuid that were removed.
   """
   switchUuid: list[str] = []


class GlobalMessageChangedEvent(SessionEvent):
   """
   This event records a change to the global message.
   
   Attributes:
       message: The new message that was set.
       prevMessage: The previous message that was set.
   """
   message: str
   prevMessage: _typing.Optional[str] = None


class HealthStatusChangedEvent(Event):
   """
   Event used to report change in health status of VirtualCenter components.
   
   Attributes:
       componentId: Unique ID of the VirtualCenter component.
       oldStatus: Previous health status of the component.
       newStatus: Current health status of the component.
       componentName: Component name.
       serviceId: Service Id of component.
   """
   componentId: str
   oldStatus: str
   newStatus: str
   componentName: str
   serviceId: _typing.Optional[str] = None

class HostAddFailedEvent(HostEvent):
   """This event records that adding a host failed."""
   hostname: str

class HostAddedEvent(HostEvent):
   """This event records the addition of a host to VirtualCenter."""
   pass

class HostAdminDisableEvent(HostEvent):
   """
   This event records that the permission on the host has been changed such
   that only the user account used for VirtualCenter operation will have
   Administrator permission.
   """
   pass

class HostAdminEnableEvent(HostEvent):
   """This event records that the administrator permission has been restored."""
   pass

class HostCnxFailedAccountFailedEvent(HostEvent):
   """
   This event records a failure to connect to a host
   due to a failure to set up a management account.
   """
   pass

class HostCnxFailedAlreadyManagedEvent(HostEvent):
   """
   This event records a failure to connect to a host
   due to the host being managed by a different VirtualCenter server.
   
   Attributes:
       serverName: The name of the VirtualCenter server that manages the host.
   """
   serverName: str

class HostCnxFailedBadCcagentEvent(HostEvent):
   """
   This event records a failure to connect to a host
   due to no response being received from the host agent.
   """
   pass

class HostCnxFailedBadUsernameEvent(HostEvent):
   """
   This event records a failure to connect to a host
   due to an invalid user name and password combination.
   """
   pass

class HostCnxFailedBadVersionEvent(HostEvent):
   """
   This event records a failure to connect to a host
   due to an incompatible client version.
   """
   pass

class HostCnxFailedCcagentUpgradeEvent(HostEvent):
   """
   This event records a failure to connect to a host
   due to a conflict with an upgrade or installation of the host agent.
   """
   pass

class HostCnxFailedEvent(HostEvent):
   """
   This event records a failure to connect to a host
   due to an unspecified condition.
   """
   pass

class HostCnxFailedNetworkErrorEvent(HostEvent):
   """
   This event records a failure to connect to a host
   due to a network error.
   """
   pass

class HostCnxFailedNoAccessEvent(HostEvent):
   """
   This event records a failure to connect to a host
   due to insufficient account privileges.
   """
   pass

class HostCnxFailedNoConnectionEvent(HostEvent):
   """
   This event records a failure to connect to a host
   due to a host not being present on the network.
   """
   pass

class HostCnxFailedNoLicenseEvent(HostEvent):
   """
   This event records a failure to connect to a host
   due to a licensing issue.
   """
   pass

class HostCnxFailedNotFoundEvent(HostEvent):
   """
   This event records a failure to connect to a host
   due to a failure to resolve the host name.
   """
   pass

class HostCnxFailedTimeoutEvent(HostEvent):
   """
   This event records a failure to connect to a host
   due to a timeout on the connection attempt.
   """
   pass

class HostComplianceCheckedEvent(HostEvent):
   """
   This event records that a compliance check was triggered
   on the host.
   """
   profile: ProfileEventArgument

class HostCompliantEvent(HostEvent):
   """This event records that host is in compliance."""
   pass

class HostConfigAppliedEvent(HostEvent):
   """This event records that a configuration was applied on a host"""
   pass

class HostConnectedEvent(HostEvent):
   """This event records a successful host connection."""
   pass

class HostConnectionLostEvent(HostEvent):
   """This event records the loss of a host connection."""
   pass

class HostDasDisabledEvent(HostEvent):
   """This event records when HA has been disabled on a host."""
   pass

class HostDasDisablingEvent(HostEvent):
   """Deprecated: As of vSphere API 5.0, the event is no longer relevant.This event records when HA is being disabled on a host."""
   pass

class HostDasEnabledEvent(HostEvent):
   """This event records when HA has been enabled on a host."""
   pass

class HostDasEnablingEvent(HostEvent):
   """This event records when HA is being enabled on a host."""
   pass


class HostDasErrorEvent(HostEvent):
   """
   Deprecated: As of vSphere API 5.0, the Server will generate the `pyVmomi.vim.event.EventEx` event
   with the `pyVmomi.vim.event.EventEx.eventTypeId` property set to \"com.vmware.vc.HA.HostAgentErrorEvent\".This event records when there is a HA error on a host.
   
   Attributes:
       reason: The reason for the failure.
   """
   class HostDasErrorReason(pyVmomi.VmomiSupport.Enum):
      """
      Attributes:
          configFailed: Error while configuring/unconfiguring HA
          timeout: Timeout while communicating with HA agent
          communicationInitFailed: HA communication initialization failed
          healthCheckScriptFailed: Health check script failed
          agentFailed: HA agent has an error
          agentShutdown: HA agent was shutdown
          isolationAddressUnpingable: HA isolation address unpingable
          other: Other reason
      """
      configFailed: _typing.ClassVar['HostDasErrorEvent.HostDasErrorReason'] = 'configFailed'
      timeout: _typing.ClassVar['HostDasErrorEvent.HostDasErrorReason'] = 'timeout'
      communicationInitFailed: _typing.ClassVar['HostDasErrorEvent.HostDasErrorReason'] = 'communicationInitFailed'
      healthCheckScriptFailed: _typing.ClassVar['HostDasErrorEvent.HostDasErrorReason'] = 'healthCheckScriptFailed'
      agentFailed: _typing.ClassVar['HostDasErrorEvent.HostDasErrorReason'] = 'agentFailed'
      agentShutdown: _typing.ClassVar['HostDasErrorEvent.HostDasErrorReason'] = 'agentShutdown'
      isolationAddressUnpingable: _typing.ClassVar['HostDasErrorEvent.HostDasErrorReason'] = 'isolationAddressUnpingable'
      other: _typing.ClassVar['HostDasErrorEvent.HostDasErrorReason'] = 'other'

   message: _typing.Optional[str] = None
   reason: _typing.Optional[str] = None

class HostDasEvent(HostEvent):
   """Top-level event for host DAS events to extend."""
   pass

class HostDasOkEvent(HostEvent):
   """Deprecated: As of vSphere API 5.0, the event is no longer relevant.This event records when HA on a host returns to normal after an error."""
   pass


class HostDisconnectedEvent(HostEvent):
   """
   This event records a disconnection from a host.
   
   Attributes:
       reason: Reason why the host was disconnected.
   """
   class ReasonCode(pyVmomi.VmomiSupport.Enum):
      """
      Attributes:
          sslThumbprintVerifyFailed: Failed to verify SSL thumbprint
          licenseExpired: License expired for the host
          agentUpgrade: Agent is being upgraded
          userRequest: User requested disconnect
          insufficientLicenses: License not available after host upgrade
          agentOutOfDate: Agent is out of date
          passwordDecryptFailure: Failed to decrypt password
          unknown: Unknown reason
          vcVRAMCapacityExceeded: The vRAM capacity of vCenter will be exceeded
      """
      sslThumbprintVerifyFailed: _typing.ClassVar['HostDisconnectedEvent.ReasonCode'] = 'sslThumbprintVerifyFailed'
      licenseExpired: _typing.ClassVar['HostDisconnectedEvent.ReasonCode'] = 'licenseExpired'
      agentUpgrade: _typing.ClassVar['HostDisconnectedEvent.ReasonCode'] = 'agentUpgrade'
      userRequest: _typing.ClassVar['HostDisconnectedEvent.ReasonCode'] = 'userRequest'
      insufficientLicenses: _typing.ClassVar['HostDisconnectedEvent.ReasonCode'] = 'insufficientLicenses'
      agentOutOfDate: _typing.ClassVar['HostDisconnectedEvent.ReasonCode'] = 'agentOutOfDate'
      passwordDecryptFailure: _typing.ClassVar['HostDisconnectedEvent.ReasonCode'] = 'passwordDecryptFailure'
      unknown: _typing.ClassVar['HostDisconnectedEvent.ReasonCode'] = 'unknown'
      vcVRAMCapacityExceeded: _typing.ClassVar['HostDisconnectedEvent.ReasonCode'] = 'vcVRAMCapacityExceeded'

   reason: _typing.Optional[str] = None


class HostEnableAdminFailedEvent(HostEvent):
   """This event records the failure to restore some of the administrator's permissions."""
   permissions: list[pyVmomi.vim.AuthorizationManager.Permission] = []


class HostEventArgument(EntityEventArgument):
   """
   The event argument is a Host object.
   
   Attributes:
       host: The host object.
   """
   host: pyVmomi.vim.HostSystem


class HostExtraNetworksEvent(HostDasEvent):
   """
   Deprecated: As of vSphere API 5.0, the event is no longer relevant.This event records the fact that a host has extra networks not used by
   other hosts for HA communication
   
   Attributes:
       ips: The comma-separated list of extra networks
   """
   ips: _typing.Optional[str] = None

class HostGetShortNameFailedEvent(HostEvent):
   """Deprecated: As of vSphere API 5.0, the event is no longer relevant.This event records that hostname -s failed or returned a name containing '.'."""
   pass

class HostInAuditModeEvent(HostEvent):
   """Host is booted in audit mode."""
   pass

class HostInventoryFullEvent(LicenseEvent):
   """This event records if the inventory of hosts has reached capacity."""
   capacity: int

class HostInventoryUnreadableEvent(Event):
   """
   Event indicating that the virtual machine inventory
   file on the host is damaged or unreadable.
   """
   pass

class HostIpChangedEvent(HostEvent):
   """
   This event records a change in host IP address.
   
   Attributes:
       oldIP: Old IP address of the host.
       newIP: New IP address of the host.
   """
   oldIP: str
   newIP: str

class HostIpInconsistentEvent(HostEvent):
   """
   Deprecated: As of vSphere API 5.0, the event is no longer relevant.This event records that the IP address resolution returned different
   addresses on the host.
   
   Please check your host's network configuration.
   """
   ipAddress: str
   ipAddress2: str

class HostIpToShortNameFailedEvent(HostEvent):
   """Deprecated: As of vSphere API 5.0, the event is no longer relevant.This event records that the host's IP address could not be resolved to a short name."""
   pass

class HostIsolationIpPingFailedEvent(HostDasEvent):
   """
   This event records that the isolation address could not be pinged.
   
   The default isolation address is the service console's default gateway.
   """
   isolationIp: str

class HostLicenseExpiredEvent(LicenseEvent):
   """This event records an expired host license."""
   pass


class HostLocalPortCreatedEvent(DvsEvent):
   """
   This event records when host local port is created to recover from
   management network connectivity loss.
   
   Attributes:
       hostLocalPort: The configuration of the new host local port.
   """
   hostLocalPort: pyVmomi.vim.dvs.DistributedVirtualPort.HostLocalPortInfo


class HostMissingNetworksEvent(HostDasEvent):
   """
   Deprecated: As of vSphere API 5.0, the event is no longer relevant.This event records the fact that a host is missing networks that
   other hosts are using for HA communication
   """
   ips: _typing.Optional[str] = None


class HostMonitoringStateChangedEvent(ClusterEvent):
   """
   This event records when host monitoring state has changed.
   
   Attributes:
       state: The service state in
           `pyVmomi.vim.cluster.DasConfigInfo.ServiceState`
       prevState: The previous service state in
           `pyVmomi.vim.cluster.DasConfigInfo.ServiceState`
   """
   state: str
   prevState: _typing.Optional[str] = None


class HostNoAvailableNetworksEvent(HostDasEvent):
   """
   This event records the fact that a host does not have any available networks
   for HA communication
   
   Attributes:
       ips: The comma-separated list of used networks
   """
   ips: _typing.Optional[str] = None

class HostNoHAEnabledPortGroupsEvent(HostDasEvent):
   """
   This event records the fact that a host does not have any HA-enabled port
   groups
   """
   pass

class HostNoRedundantManagementNetworkEvent(HostDasEvent):
   """
   This event records the fact that a host does not have a redundant
   management network.
   
   It is recommended that host management networks
   be configured with redundancy.
   """
   pass

class HostNonCompliantEvent(HostEvent):
   """This event records that host went out of compliance."""
   pass

class HostNotInClusterEvent(HostDasEvent):
   """This event records that the host is not a cluster member."""
   pass

class HostOvercommittedEvent(ClusterOvercommittedEvent):
   """
   This event records when a host's capacity cannot satisfy resource
   configuration constraints.
   """
   pass

class HostPrimaryAgentNotShortNameEvent(HostDasEvent):
   """
   Deprecated: As of vSphere API 5.0, the event is no longer relevant.This event records that the primary agent specified is not a short name.
   
   The name of the primary agent is usually stored as a short name. You should
   not normally see this error. Please check the network configurations of your
   hosts.
   """
   primaryAgent: str

class HostProfileAppliedEvent(HostEvent):
   """
   This event records that a Profile application was done
   on the host
   
   Attributes:
       profile: Link to the profile which was applied
   """
   profile: ProfileEventArgument

class HostReconnectionFailedEvent(HostEvent):
   """This event records a failed attempt to re-establish a host connection."""
   pass

class HostRemovedEvent(HostEvent):
   """This event records the removal of a host from VirtualCenter."""
   pass

class HostShortNameInconsistentEvent(HostDasEvent):
   """
   Deprecated: As of vSphere API 5.0, the event is no longer relevant.This event records that host name resolution returned different names on
   the host.
   
   Please check your host's network configuration and your DNS
   configuration. There may be duplicate entries.
   """
   shortName: str
   shortName2: str

class HostShortNameToIpFailedEvent(HostEvent):
   """Deprecated: As of vSphere API 5.0, the event is no longer relevant.This event records that the host's short name could not be resolved to an IP address."""
   shortName: str

class HostShutdownEvent(HostEvent):
   """
   This event records the shutdown of a host.
   
   Attributes:
       reason: The reason for the host shutdown.
   """
   reason: str

class HostSpecificationChangedEvent(HostEvent):
   """This event records that the host specification was changed."""
   pass

class HostSpecificationRequireEvent(HostEvent):
   """This event is issued to that the host specification should be updated."""
   pass


class HostSpecificationUpdateEvent(HostEvent):
   """
   This event suggests that update the host specification with the
   encapsulated copy.
   """
   hostSpec: pyVmomi.vim.profile.host.HostSpecification

class HostStatusChangedEvent(ClusterStatusChangedEvent):
   """This event records when a host's overall status changed."""
   pass

class HostSubSpecificationDeleteEvent(HostEvent):
   """
   This event suggests that delete the host sub specification specified by
   name.
   """
   subSpecName: str


class HostSubSpecificationUpdateEvent(HostEvent):
   """
   This event suggests that update the host sub specification with the
   encapsulated copy.
   """
   hostSubSpec: pyVmomi.vim.profile.host.HostSubSpecification


class HostSyncFailedEvent(HostEvent):
   """
   This event records a failure to sync up with the VirtualCenter agent on the host
   
   Attributes:
       reason: The reason for the failure.
   """
   reason: pyVmomi.vmodl.MethodFault

class HostUpgradeFailedEvent(HostEvent):
   """
   This event records a failure to connect to a host
   due to an installation or upgrade issue.
   """
   pass

class HostUserWorldSwapNotEnabledEvent(HostEvent):
   """
   Deprecated: As of vSphere API 5.0, the event is no longer relevant.This event records that the userworld swap is not enabled on the host.
   
   HA
   needs userworld swap to be configured on embedded ESX hosts to function.
   """
   pass


class HostVnicConnectedToCustomizedDVPortEvent(HostEvent):
   """
   This event records when some host Virtual NICs were reconfigured to use
   DVPorts with port level configuration, which might be different
   from the DVportgroup.
   
   Attributes:
       vnic: Information about the Virtual NIC that is using the DVport.
       prevPortKey: Information about the previous Virtual NIC that is using the DVport.
   """
   vnic: VnicPortArgument
   prevPortKey: _typing.Optional[str] = None


class HostWwnChangedEvent(HostEvent):
   """
   This event records a change in a host's WWN (World Wide Name).
   
   Attributes:
       oldNodeWwns: The old node WWN.
       oldPortWwns: The old port WWN.
       newNodeWwns: The new node WWN.
       newPortWwns: The new port WWN.
   """
   oldNodeWwns: list[pyVmomi.VmomiSupport.long] = []
   oldPortWwns: list[pyVmomi.VmomiSupport.long] = []
   newNodeWwns: list[pyVmomi.VmomiSupport.long] = []
   newPortWwns: list[pyVmomi.VmomiSupport.long] = []


class HostWwnConflictEvent(HostEvent):
   """
   This event records a conflict of host WWNs (World Wide Name).
   
   Attributes:
       conflictedVms: The virtual machine whose WWN conflicts with the
           current host's WWN.
       conflictedHosts: The host whose physical WWN conflicts with the
           current host's WWN.
       wwn: The WWN in conflict.
   """
   conflictedVms: list[VmEventArgument] = []
   conflictedHosts: list[HostEventArgument] = []
   wwn: pyVmomi.VmomiSupport.long

class IncorrectHostInformationEvent(LicenseEvent):
   """
   This event records if the host did not provide the information needed
   to acquire the correct set of licenses.
   """
   pass

class InfoUpgradeEvent(UpgradeEvent):
   """This event is a general information event from upgrade."""
   pass

class InsufficientFailoverResourcesEvent(ClusterEvent):
   """
   This event records that the cluster resources are insufficient
   to satisfy the configured HA failover level.
   """
   pass

class InvalidEditionEvent(LicenseEvent):
   """This event records if the edition is set to an invalid value."""
   feature: str


class LicenseExpiredEvent(Event):
   """This event records the expiration of a license."""
   feature: pyVmomi.vim.LicenseManager.FeatureInfo

class LicenseNonComplianceEvent(LicenseEvent):
   """
   This event records that the inventory is not license compliant.
   
   Attributes:
       url: Gives the url at which more details about non-compliance
           can be found.
   """
   url: str

class LicenseRestrictedEvent(LicenseEvent):
   """
   This event records if the required licenses could not be reserved because
   of a restriction in the option file.
   """
   pass

class LicenseServerAvailableEvent(LicenseEvent):
   """
   This event is reported if the LicenseServer was previously unreachable
   and is now reachable.
   """
   licenseServer: str

class LicenseServerUnavailableEvent(LicenseEvent):
   """This event is reported if the LicenseServer becomes unreachable."""
   licenseServer: str


class LocalDatastoreCreatedEvent(HostEvent):
   """
   This event records when a local datastore is created.
   
   Attributes:
       datastore: The associated datastore.
       datastoreUrl: Url of the associated datastore.
   """
   datastore: DatastoreEventArgument
   datastoreUrl: _typing.Optional[str] = None

class LocalTSMEnabledEvent(HostEvent):
   """Local Tech Support Mode for the host has been enabled."""
   pass

class LockerMisconfiguredEvent(Event):
   """
   Locker has not been configured properly.
   
   This event is fired when the datastore configured to back the locker
   does not exist or when connectivity to the datastore is lost.
   
   Attributes:
       datastore: The datastore that has been configured to back the locker
   """
   datastore: DatastoreEventArgument


class LockerReconfiguredEvent(Event):
   """
   Locker was reconfigured to a new location.
   
   Attributes:
       oldDatastore: The datastore that was previously backing the locker.
           
           This field is not
           set if a datastore was not backing the locker previously.
       newDatastore: The datastore that is now used to back the locker.
           
           This field is not set if no datastore is currently backing the locker.
   """
   oldDatastore: _typing.Optional[DatastoreEventArgument] = None
   newDatastore: _typing.Optional[DatastoreEventArgument] = None


class ManagedEntityEventArgument(EntityEventArgument):
   """
   The general event argument for a managed entity.
   
   Attributes:
       entity: The managed entity.
   """
   entity: pyVmomi.vim.ManagedEntity


class MigrationEvent(VmEvent):
   """
   These are events used to describe migration warning and errors
   
   Attributes:
       fault: The fault that describes the migration issue.
           
           This is typically either a
           MigrationFault or a VmConfigFault.
   """
   fault: pyVmomi.vmodl.MethodFault

class MigrationErrorEvent(MigrationEvent):
   """A migration error."""
   pass

class MigrationHostErrorEvent(MigrationEvent):
   """
   A migration error that includes the destination host.
   
   Attributes:
       dstHost: The name of the destination host.
   """
   dstHost: HostEventArgument

class MigrationHostWarningEvent(MigrationEvent):
   """
   A migration warning that includes the destination host.
   
   Attributes:
       dstHost: The name of the destination host.
   """
   dstHost: HostEventArgument

class MigrationResourceErrorEvent(MigrationEvent):
   """
   A migration error that includes both the destination host and resource pool.
   
   Attributes:
       dstPool: The name of the destination resource pool.
       dstHost: The name of the destination host.
   """
   dstPool: ResourcePoolEventArgument
   dstHost: HostEventArgument

class MigrationResourceWarningEvent(MigrationEvent):
   """
   A migration warning that includes both the destination host and resource pool.
   
   Attributes:
       dstPool: The name of the destination resource pool.
       dstHost: The name of the destination host.
   """
   dstPool: ResourcePoolEventArgument
   dstHost: HostEventArgument

class MigrationWarningEvent(MigrationEvent):
   """A migration warning."""
   pass

class MtuMatchEvent(DvsHealthStatusChangeEvent):
   """
   The value of MTU configured in the vSphere Distributed Switch
   matches physical switch.
   """
   pass

class MtuMismatchEvent(DvsHealthStatusChangeEvent):
   """
   The value of MTU configured in the vSphere Distributed Switch
   mismatches physical switch.
   """
   pass


class NASDatastoreCreatedEvent(HostEvent):
   """
   This event records when a NAS datastore is created.
   
   Attributes:
       datastore: The associated datastore.
       datastoreUrl: Url of the associated datastore.
   """
   datastore: DatastoreEventArgument
   datastoreUrl: _typing.Optional[str] = None


class NetworkEventArgument(EntityEventArgument):
   """
   The event argument is a Network object.
   
   Attributes:
       network: The Network object.
   """
   network: pyVmomi.vim.Network

class NetworkRollbackEvent(Event):
   """
   This event records when networking configuration on the host
   is rolled back as it disconnects the host from vCenter server.
   
   Attributes:
       methodName: Method name which caused the disconnect
       transactionId: Transaction ID for the method call that caused the disconnect
   """
   methodName: str
   transactionId: str

class NoAccessUserEvent(SessionEvent):
   """
   This event records a failed user logon due to insufficient access permission.
   
   Attributes:
       ipAddress: The IP address of the peer that initiated the connection.
           
           This may
           be the client that originated the session, or it may be an intervening
           proxy if the binding uses a protocol that supports proxies, such as HTTP.
   """
   ipAddress: str

class NoDatastoresConfiguredEvent(HostEvent):
   """No datastores have been configured on the host."""
   pass


class NoLicenseEvent(LicenseEvent):
   """
   These are events reported by License Manager.
   
   A NoLicenseEvent is reported if the required licenses could not be
   reserved. Each feature that is not fully licensed is reported.
   """
   feature: pyVmomi.vim.LicenseManager.FeatureInfo

class NoMaintenanceModeDrsRecommendationForVM(VmEvent):
   """
   This event records that DRS did not recommend a migration for a
   powered on virtual machine, even though its host is going
   into maintenance mode.
   
   DRS may not be able to recommend a migration for a virtual machine
   for reasons, include but not limited to:
   - No other connected host is compatible with this virtual machine.
   - None of the other compatible hosts have sufficient resources
     to satisfy the reservation requirements of this virtual machine.
   - Moving to any other host would violate a DRS rule. For example, all
     other compatible hosts have some incompatible virtual machines
     running.
   - DRS is disabled on this virtual machine.
   - This virtual machine was still in the process of migrating
     into the host going into maintenance mode and was not
     considered by DRS.
   - This virtual machine was in the process of migrating to another
     host when the host tried to enter maintenance mode.
   """
   pass

class NonVIWorkloadDetectedOnDatastoreEvent(DatastoreEvent):
   """This event records that non-VI workload is detected on the datastore."""
   pass

class NotEnoughResourcesToStartVmEvent(VmEvent):
   """
   This event records when the HA does not find sufficient resources to failover a
   virtual machine.
   
   Attributes:
       reason: The reason why the virtual machine could not be restarted
   """
   reason: str

class OutOfSyncDvsHost(DvsEvent):
   """
   The list of hosts that have the DVS configuration on the host
   diverged from that of the Virtual Center Server.
   
   Attributes:
       hostOutOfSync: The host that went out of sync.
   """
   hostOutOfSync: list[DvsOutOfSyncHostArgument] = []

class PermissionEvent(AuthorizationEvent):
   """
   This event records a permission operation.
   
   Attributes:
       entity: The entity to which the permission applied.
       principal: The user name or group to which the permission was granted.
       group: Whether or not the principal was a group.
   """
   entity: ManagedEntityEventArgument
   principal: str
   group: bool

class PermissionAddedEvent(PermissionEvent):
   """
   This event records the creation of a permission.
   
   Attributes:
       role: The associated role.
       propagate: Whether or not the permission applies to sub-entities.
   """
   role: RoleEventArgument
   propagate: bool

class PermissionRemovedEvent(PermissionEvent):
   """This event records the removal of a permission."""
   pass


class PermissionUpdatedEvent(PermissionEvent):
   """
   This event records the update of a permission.
   
   Attributes:
       role: The associated role.
       propagate: Whether or not the permission applies to sub-entities.
       prevRole: The previous associated role.
       prevPropagate: Previous propagate value.
   """
   role: RoleEventArgument
   propagate: bool
   prevRole: _typing.Optional[RoleEventArgument] = None
   prevPropagate: _typing.Optional[bool] = None

class ProfileEvent(Event):
   """
   This event records a Profile specific event.
   
   Attributes:
       profile: Link to the profile to which this event applies
   """
   profile: ProfileEventArgument

class ProfileAssociatedEvent(ProfileEvent):
   """This event records that a Profile was associated with a managed entity."""
   pass

class ProfileChangedEvent(ProfileEvent):
   """This event records that the profile has been edited"""
   pass

class ProfileCreatedEvent(ProfileEvent):
   """This event records that a Profile was created."""
   pass

class ProfileDissociatedEvent(ProfileEvent):
   """This event records that a Profile was dissociated from a managed entity"""
   pass


class ProfileEventArgument(EventArgument):
   """The event argument is a Profile object"""
   profile: pyVmomi.vim.profile.Profile
   name: str


class ProfileReferenceHostChangedEvent(ProfileEvent):
   """
   This event records that the reference host associated with this profile has changed
   
   Attributes:
       referenceHost: The newly associated reference host with this profile
       referenceHostName: The newly associated reference host name
       prevReferenceHostName: The previous reference host name
   """
   referenceHost: _typing.Optional[pyVmomi.vim.HostSystem] = None
   referenceHostName: _typing.Optional[str] = None
   prevReferenceHostName: _typing.Optional[str] = None

class ProfileRemovedEvent(ProfileEvent):
   """This event records that a Profile was removed."""
   pass


class RecoveryEvent(DvsEvent):
   """
   This event is generated when recovery takes place on a management vmknic
   
   Attributes:
       hostName: The host on which recovery happened
       portKey: The key of the new port
       dvsUuid: The uuid of the DVS
       vnic: The virtual management NIC device where recovery was done
   """
   hostName: str
   portKey: str
   dvsUuid: _typing.Optional[str] = None
   vnic: _typing.Optional[str] = None

class RemoteTSMEnabledEvent(HostEvent):
   """Remote Tech Support Mode for the host has been enabled."""
   pass

class ResourcePoolEvent(Event):
   """This event is the base class for all resource pool events."""
   resourcePool: ResourcePoolEventArgument

class ResourcePoolCreatedEvent(ResourcePoolEvent):
   """
   This event records when a new resource pool is created.
   
   Attributes:
       parent: The parent resource pool that new resource pool belongs to.
   """
   parent: ResourcePoolEventArgument

class ResourcePoolDestroyedEvent(ResourcePoolEvent):
   """This event records when a resource pool is destroyed."""
   pass


class ResourcePoolEventArgument(EntityEventArgument):
   """
   The event argument is a ResourcePool object.
   
   Attributes:
       resourcePool: The ResourcePool object.
   """
   resourcePool: pyVmomi.vim.ResourcePool

class ResourcePoolMovedEvent(ResourcePoolEvent):
   """
   This event records when a resource pool is moved.
   
   Attributes:
       oldParent: The old parent of the resource Pool.
       newParent: The new parent of the resource Pool.
   """
   oldParent: ResourcePoolEventArgument
   newParent: ResourcePoolEventArgument


class ResourcePoolReconfiguredEvent(ResourcePoolEvent):
   """
   This event records when a resource pool configuration is changed.
   
   Attributes:
       configChanges: The configuration values changed during the reconfiguration.
   """
   configChanges: _typing.Optional[ChangesInfoEventArgument] = None

class ResourceViolatedEvent(ResourcePoolEvent):
   """
   This event records when a conflict with a resource pool's resource
   configuration is detected.
   """
   pass

class RoleEvent(AuthorizationEvent):
   """
   This event records a role operation.
   
   Attributes:
       role: The associated role.
   """
   role: RoleEventArgument


class RoleAddedEvent(RoleEvent):
   """
   This event records the creation of a role.
   
   Attributes:
       privilegeList: The privileges granted to the role.
   """
   privilegeList: list[str] = []

class RoleEventArgument(EventArgument):
   """
   The event argument is a Role object.
   
   Attributes:
       roleId: The ID of the role.
       name: The name of the role.
   """
   roleId: int
   name: str

class RoleRemovedEvent(RoleEvent):
   """This class records the removal of a role."""
   pass


class RoleUpdatedEvent(RoleEvent):
   """
   This event records the creation of a role.
   
   Attributes:
       privilegeList: The privileges granted to the role.
       prevRoleName: The name of the previous role.
       privilegesAdded: The privileges added to the role.
       privilegesRemoved: The privileges removed from the role.
   """
   privilegeList: list[str] = []
   prevRoleName: _typing.Optional[str] = None
   privilegesAdded: list[str] = []
   privilegesRemoved: list[str] = []


class RollbackEvent(DvsEvent):
   """
   This event is generated when network configuration rollback
   occurs on a host due configuration change that disconnected
   the host from vSphere server
   
   Attributes:
       hostName: The host on which rollback happened
       methodName: The API method that was rolled back
   """
   hostName: str
   methodName: _typing.Optional[str] = None

class ScheduledTaskEvent(Event):
   """
   These events are scheduled task events.
   
   Attributes:
       scheduledTask: The scheduled task object.
       entity: The entity on which the scheduled task registered.
   """
   scheduledTask: ScheduledTaskEventArgument
   entity: ManagedEntityEventArgument

class ScheduledTaskCompletedEvent(ScheduledTaskEvent):
   """This event records the completion of a scheduled task."""
   pass

class ScheduledTaskCreatedEvent(ScheduledTaskEvent):
   """This event records the creation of a scheduled task."""
   pass

class ScheduledTaskEmailCompletedEvent(ScheduledTaskEvent):
   """
   This event records the sending of a notification via email for a scheduled task.
   
   Attributes:
       to: The destination email address.
   """
   to: str


class ScheduledTaskEmailFailedEvent(ScheduledTaskEvent):
   """
   This event records the failure of an attempt to send a notification via email
   for a scheduled task.
   
   Attributes:
       to: The destination email address.
       reason: The reason for the failure.
   """
   to: str
   reason: pyVmomi.vmodl.MethodFault


class ScheduledTaskEventArgument(EntityEventArgument):
   """
   The event argument is a scheduled task object.
   
   Attributes:
       scheduledTask: The scheduled task object.
   """
   scheduledTask: pyVmomi.vim.scheduler.ScheduledTask


class ScheduledTaskFailedEvent(ScheduledTaskEvent):
   """
   This event records the failure of a scheduled task.
   
   Attributes:
       reason: The reason for the failure.
   """
   reason: pyVmomi.vmodl.MethodFault


class ScheduledTaskReconfiguredEvent(ScheduledTaskEvent):
   """
   This event records the reconfiguration of a scheduled task.
   
   Attributes:
       configChanges: The configuration values changed during the reconfiguration.
   """
   configChanges: _typing.Optional[ChangesInfoEventArgument] = None

class ScheduledTaskRemovedEvent(ScheduledTaskEvent):
   """This event records the removal of a scheduled task."""
   pass

class ScheduledTaskStartedEvent(ScheduledTaskEvent):
   """This event records when a scheduled task started."""
   pass

class ServerLicenseExpiredEvent(LicenseEvent):
   """This event records an expired VirtualCenter server license."""
   product: str

class ServerStartedSessionEvent(SessionEvent):
   """This event records the starting of the VirtualCenter server."""
   pass

class SessionTerminatedEvent(SessionEvent):
   """
   This event records the termination of a session.
   
   Attributes:
       sessionId: The unique identifier of the terminated session.
       terminatedUsername: The name of the user owning the terminated session.
   """
   sessionId: str
   terminatedUsername: str


class TaskEvent(Event):
   """
   This event records the creation of a Task.
   
   Note that the embedded TaskInfo object is a snapshot of the
   Task state at the time of its creation, so its state will always be
   \"queued\". To find the current status of the task, query for the
   current state of the Task using the eventChainId in the embedded
   TaskInfo object.
   
   Attributes:
       info: The information about the task.
   """
   info: pyVmomi.vim.TaskInfo

class TaskTimeoutEvent(TaskEvent):
   """This event records when a task is cleaned up b/c of timeout"""
   pass

class TeamingMatchEvent(DvsHealthStatusChangeEvent):
   """
   The teaming configuration of the uplink ports in the DVS matches
   physical switch configuration.
   """
   pass

class TeamingMisMatchEvent(DvsHealthStatusChangeEvent):
   """
   The teaming configuration of the uplink ports in the DVS
   does not match physical switch configuration.
   """
   pass

class TemplateUpgradeEvent(Event):
   """This event is the base class for all the template upgrade events."""
   legacyTemplate: str

class TemplateBeingUpgradedEvent(TemplateUpgradeEvent):
   """This event records the start of a template upgrade."""
   pass


class TemplateUpgradeFailedEvent(TemplateUpgradeEvent):
   """This event records that the template upgrade failed."""
   reason: pyVmomi.vmodl.MethodFault

class TemplateUpgradedEvent(TemplateUpgradeEvent):
   """This event records that the template upgrade succeeded."""
   pass


class TgwEventArgument(EntityEventArgument):
   """
   The event argument is a transit gateway object.
   
   Attributes:
       tgw: The transit gateway object.
   
   Since: vSphere API Release 9.1.0.0
   """
   tgw: pyVmomi.vim.TransitGateway

class TimedOutHostOperationEvent(HostEvent):
   """
   This event indicates that an operation performed on the host timed out.
   
   Typically,
   a previous event in the sequence of events contains more
   information about the cause of the operation timing out.
   """
   pass

class UnlicensedVirtualMachinesEvent(LicenseEvent):
   """
   This event records that we have unlicensed virtual machines on the
   specified host.
   
   This can be both a `vim.ManagedEntity.configIssue` and an entry in the event log.
   """
   unlicensed: int
   available: int

class UnlicensedVirtualMachinesFoundEvent(LicenseEvent):
   """
   This event records that we discovered unlicensed virtual machines on
   the specified host.
   
   After this event is entered into the event log, we
   expect to see a corresponding `vim.event.Event.UnlicensedVirtualMachinesEvent` `vim.ManagedEntity.configIssue` on the host.
   """
   available: int

class UpdatedAgentBeingRestartedEvent(HostEvent):
   """
   This event records that the agent has been patched and will be
   restarted.
   """
   pass

class UplinkPortMtuNotSupportEvent(DvsHealthStatusChangeEvent):
   """
   Mtu health check status of an uplink port is changed, and in the latest mtu health check,
   not all the vlans' MTU setting on physical switch allows vSphere Distributed Switch
   max MTU size packets passing.
   """
   pass

class UplinkPortMtuSupportEvent(DvsHealthStatusChangeEvent):
   """
   Mtu health check status of an uplink port is changed, and in the latest mtu health check,
   all the vlans' MTU setting on physical switch allows vSphere Distributed Switch
   max MTU size packets passing.
   """
   pass

class UplinkPortVlanTrunkedEvent(DvsHealthStatusChangeEvent):
   """
   Vlans health check status of an uplink port is changed, and in the latest vlan health check,
   all the vlans are trunked by the physical switch connected to the uplink port.
   """
   pass

class UplinkPortVlanUntrunkedEvent(DvsHealthStatusChangeEvent):
   """
   Vlans health check status of an uplink port is changed, and in the latest vlan health check,
   not all the vlans are trunked by the physical switch connected to the uplink port.
   """
   pass

class UserAssignedToGroup(HostEvent):
   """This event records that a user account membership was added to a group."""
   userLogin: str
   group: str


class UserLoginSessionEvent(SessionEvent):
   """
   This event records a user logon.
   
   Attributes:
       ipAddress: The IP address of the peer that initiated the connection.
           
           This may
           be the client that originated the session, or it may be an intervening
           proxy if the binding uses a protocol that supports proxies, such as HTTP.
       userAgent: The user agent or application
       locale: The locale of the session.
       sessionId: The unique identifier for the session.
   """
   ipAddress: str
   userAgent: _typing.Optional[str] = None
   locale: str
   sessionId: str


class UserLogoutSessionEvent(SessionEvent):
   """
   This event records a user logoff, disconnection, or session timeout.
   
   Attributes:
       ipAddress: The IP address of client
       userAgent: The user agent or application
       callCount: Number of API invocations made by the session
       sessionId: The unique identifier for the session.
       loginTime: Timestamp when the user logged on for this session.
   """
   ipAddress: _typing.Optional[str] = None
   userAgent: _typing.Optional[str] = None
   callCount: _typing.Optional[pyVmomi.VmomiSupport.long] = None
   sessionId: _typing.Optional[str] = None
   loginTime: _typing.Optional[_datetime.datetime] = None

class UserPasswordChanged(HostEvent):
   """This event records that a user password changed."""
   userLogin: str

class UserUnassignedFromGroup(HostEvent):
   """This event records that a user account membership was removed from a group."""
   userLogin: str
   group: str

class UserUpgradeEvent(UpgradeEvent):
   """This event is a general user event from upgrade."""
   pass


class VMFSDatastoreCreatedEvent(HostEvent):
   """
   This event records when a VMFS datastore is created.
   
   Attributes:
       datastore: The associated datastore.
       datastoreUrl: Url of the associated datastore.
   """
   datastore: DatastoreEventArgument
   datastoreUrl: _typing.Optional[str] = None

class VMFSDatastoreExpandedEvent(HostEvent):
   """
   This event records when a datastore is expanded.
   
   Attributes:
       datastore: The associated datastore.
   """
   datastore: DatastoreEventArgument

class VMFSDatastoreExtendedEvent(HostEvent):
   """
   This event records when a datastore is extended.
   
   Attributes:
       datastore: The associated datastore.
   """
   datastore: DatastoreEventArgument

class VMotionLicenseExpiredEvent(LicenseEvent):
   """This event records an expired VMotion license."""
   pass


class VcAgentUninstallFailedEvent(HostEvent):
   """
   This event records when the VirtualCenter agent on a host failed to uninstall.
   
   Attributes:
       reason: The reason why the uninstall failed, if known.
           
           See `pyVmomi.vim.fault.AgentInstallFailed.Reason`
   """
   reason: _typing.Optional[str] = None

class VcAgentUninstalledEvent(HostEvent):
   """This event records when the VirtualCenter agent on a host is uninstalled."""
   pass


class VcAgentUpgradeFailedEvent(HostEvent):
   """
   This event records when the VirtualCenter agent on a host failed to upgrade.
   
   Attributes:
       reason: The reason why the upgrade failed, if known.
           
           See `pyVmomi.vim.fault.AgentInstallFailed.Reason`
   """
   reason: _typing.Optional[str] = None

class VcAgentUpgradedEvent(HostEvent):
   """This event records when the VirtualCenter agent on a host upgraded."""
   pass

class VimAccountPasswordChangedEvent(HostEvent):
   """
   Password for the Vim account user on the host has been changed.
   
   This is an account created by VirtualCenter and used to manage the host.
   """
   pass

class VmAcquiredMksTicketEvent(VmEvent):
   """This event records a user successfully acquiring an MKS ticket"""
   pass

class VmAcquiredTicketEvent(VmEvent):
   """
   This event records a user successfully acquiring a ticket
   
   Attributes:
       ticketType: The type of the ticket @see VirtualMachine.TicketType
   """
   ticketType: str

class VmAutoRenameEvent(VmEvent):
   """
   This event records that a virtual machine was automatically renamed
   because of a name conflict.
   
   Attributes:
       oldName: The name of the virtual machine before renaming.
       newName: The name of the virtual machine after renaming.
   """
   oldName: str
   newName: str

class VmCloneEvent(VmEvent):
   """The is the base event for all clone operations."""
   pass

class VmBeingClonedEvent(VmCloneEvent):
   """
   This event records a virtual machine being cloned.
   
   Attributes:
       destFolder: The destination folder to which the virtual machine is being cloned.
       destName: The name of the destination virtual machine.
       destHost: The destination host to which the virtual machine is being cloned.
   """
   destFolder: FolderEventArgument
   destName: str
   destHost: HostEventArgument

class VmBeingClonedNoFolderEvent(VmCloneEvent):
   """
   This event records a virtual machine being cloned.
   
   Attributes:
       destName: The name of the destination virtual machine.
       destHost: The destination host to which the virtual machine is being cloned.
   """
   destName: str
   destHost: HostEventArgument


class VmBeingCreatedEvent(VmEvent):
   """
   This event records a virtual machine being created.
   
   Attributes:
       configSpec: The configuration specification that was used to create this virtual machine.
   """
   configSpec: _typing.Optional[pyVmomi.vim.vm.ConfigSpec] = None

class VmBeingDeployedEvent(VmEvent):
   """
   This event records a virtual machine being deployed from a template.
   
   Attributes:
       srcTemplate: The template object from which the virtual machine is being deployed.
   """
   srcTemplate: VmEventArgument


class VmBeingHotMigratedEvent(VmEvent):
   """
   This event records that a virtual machine is being hot-migrated.
   
   Attributes:
       destHost: The destination host to which the virtual machine is to be migrated.
       destDatacenter: The destination datacenter to which the virtual machine is being migrated
       destDatastore: The destination primary datastore to which the virtual machine is being migrated
   """
   destHost: HostEventArgument
   destDatacenter: _typing.Optional[DatacenterEventArgument] = None
   destDatastore: _typing.Optional[DatastoreEventArgument] = None


class VmBeingMigratedEvent(VmEvent):
   """
   This event records that a virtual machine is being migrated.
   
   Attributes:
       destHost: The destination host.
       destDatacenter: The destination datacenter
       destDatastore: The destination primary datastore
   """
   destHost: HostEventArgument
   destDatacenter: _typing.Optional[DatacenterEventArgument] = None
   destDatastore: _typing.Optional[DatastoreEventArgument] = None

class VmRelocateSpecEvent(VmEvent):
   """This event is the base event for relocate and clone base events."""
   pass


class VmBeingRelocatedEvent(VmRelocateSpecEvent):
   """
   This event records that a virtual machine is being relocated.
   
   Attributes:
       destHost: The destination host to which the virtual machine is being relocated.
       destDatacenter: The destination datacenter to which the virtual machine is being relocated
       destDatastore: The destination primary datastore to which the virtual machine is being relocated
   """
   destHost: HostEventArgument
   destDatacenter: _typing.Optional[DatacenterEventArgument] = None
   destDatastore: _typing.Optional[DatastoreEventArgument] = None


class VmCloneFailedEvent(VmCloneEvent):
   """
   This event records a failure to clone a virtual machine.
   
   Attributes:
       destFolder: The destination folder to which the virtual machine is being cloned.
       destName: The name of the destination virtual machine.
       destHost: The destination host to which the virtual machine was being cloned.
       reason: The reason why this clone operation failed.
   """
   destFolder: FolderEventArgument
   destName: str
   destHost: HostEventArgument
   reason: pyVmomi.vmodl.MethodFault

class VmClonedEvent(VmCloneEvent):
   """
   This event records the completion of a virtual machine cloning operation.
   
   Attributes:
       sourceVm: The source virtual machine for the clone operation.
   """
   sourceVm: VmEventArgument

class VmConfigMissingEvent(VmEvent):
   """This event records if the configuration file can not be found."""
   pass

class VmConnectedEvent(VmEvent):
   """This event records that a virtual machine is connected."""
   pass

class VmCreatedEvent(VmEvent):
   """This event records that a virtual machine was successfully created."""
   pass


class VmDasBeingResetEvent(VmEvent):
   """
   This event records when a virtual machine is reset by
   HA VM Health Monitoring on hosts that do not support the
   create screenshot api or if the createscreenshot api fails.
   
   Attributes:
       reason: The reason why this vm is being reset
   """
   class ReasonCode(pyVmomi.VmomiSupport.Enum):
      """
      Attributes:
          vmtoolsHeartbeatFailure: vmtools heartbeat failure
          appHeartbeatFailure: application heartbeat failure
          appImmediateResetRequest: immediate reset request
          vmcpResetApdCleared: reset issued by VMCP when APD cleared
          guestOsCrashFailure: guest OS crash failure
      """
      vmtoolsHeartbeatFailure: _typing.ClassVar['VmDasBeingResetEvent.ReasonCode'] = 'vmtoolsHeartbeatFailure'
      appHeartbeatFailure: _typing.ClassVar['VmDasBeingResetEvent.ReasonCode'] = 'appHeartbeatFailure'
      appImmediateResetRequest: _typing.ClassVar['VmDasBeingResetEvent.ReasonCode'] = 'appImmediateResetRequest'
      vmcpResetApdCleared: _typing.ClassVar['VmDasBeingResetEvent.ReasonCode'] = 'vmcpResetApdCleared'
      guestOsCrashFailure: _typing.ClassVar['VmDasBeingResetEvent.ReasonCode'] = 'guestOsCrashFailure'

   reason: _typing.Optional[str] = None

class VmDasBeingResetWithScreenshotEvent(VmDasBeingResetEvent):
   """
   This event records when a virtual machine is reset by
   HA VM Health Monitoring on hosts that support the create screenshot api
   
   Attributes:
       screenshotFilePath: The datastore path of the screenshot taken before resetting.
   """
   screenshotFilePath: str

class VmDasResetFailedEvent(VmEvent):
   """
   This event records when HA VM Health Monitoring fails to reset
   a virtual machine after failure
   """
   pass

class VmDasUpdateErrorEvent(VmEvent):
   """
   The event records that an error occurred when updating the HA agents
   with the current state of the virtual machine.
   
   If this occurs during a
   powerOn operation, the virtual machine will not be failed over in the
   event of a host failure. If it occurs during a powerOff, the virtual
   machine will be automatically powered on if the host it was last running
   on crashes.
   """
   pass

class VmDasUpdateOkEvent(VmEvent):
   """
   This event records that HA agents have been updated with the current
   state of the virtual machine.
   """
   pass

class VmDateRolledBackEvent(VmEvent):
   """This event records when the VirtualCenter server date rolled back."""
   pass


class VmDeployFailedEvent(VmEvent):
   """
   This event records a failure to deploy from a template.
   
   Attributes:
       destDatastore: The destination datastore to which the template was being deployed.
       reason: The reason for the failure.
   """
   destDatastore: EntityEventArgument
   reason: pyVmomi.vmodl.MethodFault

class VmDeployedEvent(VmEvent):
   """
   This event records the completion of a virtual machine deployment operation.
   
   Attributes:
       srcTemplate: The template object from which the virtual machine has been deployed.
   """
   srcTemplate: VmEventArgument

class VmDisconnectedEvent(VmEvent):
   """This event records that a virtual machine disconnected."""
   pass

class VmDiscoveredEvent(VmEvent):
   """This event records a virtual machine discovery."""
   pass


class VmDiskFailedEvent(VmEvent):
   """
   This event records a failure to create a virtual disk in a virtual machine.
   
   Attributes:
       disk: The name of the virtual disk.
       reason: The reason for the failure.
   """
   disk: str
   reason: pyVmomi.vmodl.MethodFault

class VmEmigratingEvent(VmEvent):
   """This event records a virtual machine emigration."""
   pass

class VmEndRecordingEvent(VmEvent):
   """Deprecated: as of vSphere API 6.0This event indicates the end of a recording session on a virtual machine."""
   pass

class VmEndReplayingEvent(VmEvent):
   """Deprecated: as of vSphere API 6.0This event indicates the end of a replay session on a virtual machine."""
   pass


class VmEventArgument(EntityEventArgument):
   """
   The event argument is a VirtualMachine object.
   
   Attributes:
       vm: The VirtualMachine object.
   """
   vm: pyVmomi.vim.VirtualMachine


class VmFailedMigrateEvent(VmEvent):
   """
   This event records a failure to migrate a virtual machine.
   
   Attributes:
       destHost: The destination host.
       reason: The reason for the failure.
       destDatacenter: The destination datacenter
       destDatastore: The destination primary datastore
   """
   destHost: HostEventArgument
   reason: pyVmomi.vmodl.MethodFault
   destDatacenter: _typing.Optional[DatacenterEventArgument] = None
   destDatastore: _typing.Optional[DatastoreEventArgument] = None


class VmFailedRelayoutEvent(VmEvent):
   """
   This event records a specific failure to relay out a virtual machine,
   such as a failure to access the disk.
   """
   reason: pyVmomi.vmodl.MethodFault

class VmFailedRelayoutOnVmfs2DatastoreEvent(VmEvent):
   """
   This event records a failure to relay out a virtual machine
   when the virtual machine still has disks on a VMFS2 volume.
   """
   pass


class VmFailedStartingSecondaryEvent(VmEvent):
   """
   This event records vmotion failure when starting a secondary VM.
   
   Attributes:
       reason: The reason for the failure.
           
           See `pyVmomi.vim.event.VmFailedStartingSecondaryEvent.FailureReason`
   """
   class FailureReason(pyVmomi.VmomiSupport.Enum):
      """
      The reason for the failure.
      
      Attributes:
          incompatibleHost: Remote host is incompatible for secondary virtual machine.
              
              For instance, the host doesn't have access to the virtual machine's
              network or datastore.
          loginFailed: Login to remote host failed.
          registerVmFailed: Registration of the secondary virtual machine
              on the remote host failed.
          migrateFailed: Migration failed.
      """
      incompatibleHost: _typing.ClassVar['VmFailedStartingSecondaryEvent.FailureReason'] = 'incompatibleHost'
      loginFailed: _typing.ClassVar['VmFailedStartingSecondaryEvent.FailureReason'] = 'loginFailed'
      registerVmFailed: _typing.ClassVar['VmFailedStartingSecondaryEvent.FailureReason'] = 'registerVmFailed'
      migrateFailed: _typing.ClassVar['VmFailedStartingSecondaryEvent.FailureReason'] = 'migrateFailed'

   reason: _typing.Optional[str] = None


class VmFailedToPowerOffEvent(VmEvent):
   """
   This event records a failure to power off a virtual machine.
   
   Attributes:
       reason: The reason for the failure.
   """
   reason: pyVmomi.vmodl.MethodFault


class VmFailedToPowerOnEvent(VmEvent):
   """
   This event records a failure to power on a virtual machine.
   
   Attributes:
       reason: The reason for the failure.
   """
   reason: pyVmomi.vmodl.MethodFault


class VmFailedToRebootGuestEvent(VmEvent):
   """
   This event records a failure to reboot the guest on a virtual machine.
   
   Attributes:
       reason: The reason for the failure.
   """
   reason: pyVmomi.vmodl.MethodFault


class VmFailedToResetEvent(VmEvent):
   """
   This event records a failure to reset a virtual machine.
   
   Attributes:
       reason: The reason for the failure.
   """
   reason: pyVmomi.vmodl.MethodFault


class VmFailedToShutdownGuestEvent(VmEvent):
   """
   This event records a failure to shut down the guest on a virtual machine.
   
   Attributes:
       reason: The reason for the failure.
   """
   reason: pyVmomi.vmodl.MethodFault


class VmFailedToStandbyGuestEvent(VmEvent):
   """
   This event records a failure to set the guest on a virtual machine to a standby
   state.
   
   Attributes:
       reason: The reason for the failure.
   """
   reason: pyVmomi.vmodl.MethodFault


class VmFailedToSuspendEvent(VmEvent):
   """
   This event records a failure to suspend a virtual machine.
   
   Attributes:
       reason: The reason for the failure.
   """
   reason: pyVmomi.vmodl.MethodFault

class VmFailedUpdatingSecondaryConfig(VmEvent):
   """
   This event records after a failover the new new primary failed to
   update the config of the secondary vm.
   """
   pass


class VmFailoverFailed(VmEvent):
   """
   This event records when a virtual machine failover was unsuccessful.
   
   Attributes:
       reason: The reason for the failure
   """
   reason: _typing.Optional[pyVmomi.vmodl.MethodFault] = None


class VmFaultToleranceStateChangedEvent(VmEvent):
   """
   This event records a fault tolerance state change.
   
   A default alarm will be triggered upon this event, which would
   change the vm state:
   the vm state is red if the newState is needSecondary;
   the vm state is yellow if the newState is disabled;
   the vm state is green if the newState is notConfigured, starting,
   enabled or running
   
   Attributes:
       oldState: The old fault toleeance state.
       newState: The new fault tolerance state.
   """
   oldState: pyVmomi.vim.VirtualMachine.FaultToleranceState
   newState: pyVmomi.vim.VirtualMachine.FaultToleranceState

class VmFaultToleranceTurnedOffEvent(VmEvent):
   """
   This event records that all secondary virtual machines have
   been removed and fault tolerance protection turned off for
   this virtual machine.
   """
   pass


class VmFaultToleranceVmTerminatedEvent(VmEvent):
   """
   This event records a secondary or primary VM is terminated.
   
   The reason could be : divergence, lost connection to secondary, partial
   hardware failure of secondary, or by user.
   
   Attributes:
       reason: The reason for the failure.
           
           see `pyVmomi.vim.VirtualMachine.NeedSecondaryReason`
   """
   reason: _typing.Optional[str] = None

class VmGuestOSCrashedEvent(VmEvent):
   """This event notifies that a guest OS has crashed"""
   pass

class VmGuestRebootEvent(VmEvent):
   """This is a virtual machine guest reboot request event."""
   pass

class VmGuestShutdownEvent(VmEvent):
   """This is a virtual machine guest shutdown request event."""
   pass

class VmGuestStandbyEvent(VmEvent):
   """This is a virtual machine guest standby request event."""
   pass


class VmHealthMonitoringStateChangedEvent(ClusterEvent):
   """
   This event records when host monitoring state has changed.
   
   Attributes:
       state: The service state in
           `pyVmomi.vim.cluster.DasConfigInfo.VmMonitoringState`
       prevState: The previous service state in
           `pyVmomi.vim.cluster.DasConfigInfo.VmMonitoringState`
   """
   state: str
   prevState: _typing.Optional[str] = None

class VmInstanceUuidAssignedEvent(VmEvent):
   """
   This event records the assignment of a new instance UUID
   to a virtual machine.
   
   Attributes:
       instanceUuid: The new instance UUID.
   """
   instanceUuid: str

class VmInstanceUuidChangedEvent(VmEvent):
   """
   This event records a change in a virtual machine's instance UUID.
   
   Attributes:
       oldInstanceUuid: The old instance UUID.
       newInstanceUuid: The new instance UUID.
   """
   oldInstanceUuid: str
   newInstanceUuid: str

class VmInstanceUuidConflictEvent(VmEvent):
   """
   This event records a conflict of virtual machine instance UUIDs.
   
   Attributes:
       conflictedVm: The virtual machine whose instance UUID conflicts with the
           current virtual machine's instance UUID.
       instanceUuid: The instance UUID in conflict.
   """
   conflictedVm: VmEventArgument
   instanceUuid: str

class VmMacAssignedEvent(VmEvent):
   """
   This event records the assignment of a new MAC address
   to a virtual network adapter.
   
   Attributes:
       adapter: The name of the virtual adapter.
       mac: The new MAC address.
   """
   adapter: str
   mac: str

class VmMacChangedEvent(VmEvent):
   """
   This event records a change in a virtual machine's MAC address.
   
   Attributes:
       adapter: The name of the virtual network adapter.
       oldMac: The old MAC address.
       newMac: The new MAC address.
   """
   adapter: str
   oldMac: str
   newMac: str

class VmMacConflictEvent(VmEvent):
   """
   This event records a MAC address conflict for a virtual machine.
   
   Attributes:
       conflictedVm: The virtual machine whose MAC address conflicts with
           the current virtual machine's address.
       mac: The MAC address that is in conflict.
   """
   conflictedVm: VmEventArgument
   mac: str

class VmMaxFTRestartCountReached(VmEvent):
   """This event is fired when FT VM reached the max restart count"""
   pass

class VmMaxRestartCountReached(VmEvent):
   """This event is fired when the VM reached the max restart count"""
   pass


class VmMessageErrorEvent(VmEvent):
   """
   This event records when an error message (consisting of a collection of \"observations\")
   is thrown by the virtual machine.
   
   This is a generic event for such messages.
   
   Attributes:
       message: A raw message returned by the virtualization platform.
       messageInfo: A set of localizable message data that comprise this event.
           
           Only available on servers that support localization.
   """
   message: str
   messageInfo: list[pyVmomi.vim.vm.Message] = []


class VmMessageEvent(VmEvent):
   """
   This event records when an informational message (consisting of a collection of \"observations\")
   is thrown by the virtual machine.
   
   This is a generic event for such messages.
   
   Attributes:
       message: A raw message returned by the virtualization platform.
       messageInfo: A set of localizable message data that comprise this event.
           
           Only available on servers that support localization.
   """
   message: str
   messageInfo: list[pyVmomi.vim.vm.Message] = []


class VmMessageWarningEvent(VmEvent):
   """
   This event records when a warning message (consisting of a collection of \"observations\")
   is thrown by the virtual machine.
   
   This is a generic event for such messages.
   
   Attributes:
       message: A raw message returned by the virtualization platform.
   """
   message: str
   messageInfo: list[pyVmomi.vim.vm.Message] = []

class VmNoCompatibleHostForSecondaryEvent(VmEvent):
   """
   This event records that no compatible host was found to place a
   secondary VM.
   
   A default alarm will be triggered upon this event, which by default
   would trigger a SNMP trap.
   """
   pass

class VmNoNetworkAccessEvent(VmEvent):
   """
   This event records a migration failure when the destination host
   is not on the same network as the source host.
   
   Attributes:
       destHost: The destination host.
   """
   destHost: HostEventArgument

class VmOrphanedEvent(VmEvent):
   """This event records a virtual machine for which no host is responsible."""
   pass

class VmPoweredOffEvent(VmEvent):
   """This event records when a virtual machine finished powering off."""
   pass

class VmPowerOffOnIsolationEvent(VmPoweredOffEvent):
   """
   This event records when a virtual machine has been powered off on an isolated host
   in a HA cluster.
   
   Attributes:
       isolatedHost: The isolated host on which a virtual machine is powered off.
   """
   isolatedHost: HostEventArgument

class VmPoweringOnWithCustomizedDVPortEvent(VmEvent):
   """
   This event records when a virtual machine was powering on using
   DVPorts with port level configuration, which might be different
   from the DVportgroup.
   
   Attributes:
       vnic: The list of Virtual NIC that were using the DVports.
   """
   vnic: list[VnicPortArgument] = []


class VmPrimaryFailoverEvent(VmEvent):
   """
   This event records a fault tolerance failover.
   
   The reason could be : lost connection to primary, partial hardware failure
   of primary or by user.
   
   Attributes:
       reason: The reason for the failure.
           
           see `pyVmomi.vim.VirtualMachine.NeedSecondaryReason`
   """
   reason: _typing.Optional[str] = None


class VmReconfiguredEvent(VmEvent):
   """
   This event records a reconfiguration of the virtual machine.
   
   Attributes:
       configSpec: The configuration specification that was used for the reconfiguration.
       configChanges: The configuration values changed during the reconfiguration.
   """
   configSpec: pyVmomi.vim.vm.ConfigSpec
   configChanges: _typing.Optional[ChangesInfoEventArgument] = None

class VmRegisteredEvent(VmEvent):
   """This event records that a virtual machine was successfully registered."""
   pass

class VmRelayoutSuccessfulEvent(VmEvent):
   """
   This event records that a virtual machine was successfully
   converted to the new virtual machine format on a VMFS3 volume.
   """
   pass

class VmRelayoutUpToDateEvent(VmEvent):
   """
   This event records that a virtual machine is already in the
   correct format.
   
   No relay out is necessary.
   """
   pass

class VmReloadFromPathEvent(VmEvent):
   """
   This event records that a virtual machine was successfully reloaded from a
   new configuration path.
   """
   configPath: str

class VmReloadFromPathFailedEvent(VmEvent):
   """
   This event records that a virtual machine reload from a new configuration
   path failed.
   """
   configPath: str


class VmRelocateFailedEvent(VmRelocateSpecEvent):
   """
   This event records a failure to relocate a virtual machine.
   
   Attributes:
       destHost: The destination host to which the virtual machine is being relocated.
       reason: The reason why this relocate operation failed.
       destDatacenter: The destination datacenter to which the virtual machine was being relocated
       destDatastore: The destination primary datastore to which the virtual machine was being relocated
   """
   destHost: HostEventArgument
   reason: pyVmomi.vmodl.MethodFault
   destDatacenter: _typing.Optional[DatacenterEventArgument] = None
   destDatastore: _typing.Optional[DatastoreEventArgument] = None


class VmRelocatedEvent(VmRelocateSpecEvent):
   """
   This event records the completion of a virtual machine relocation.
   
   Attributes:
       sourceHost: The source host from which the virtual machine was relocated.
       sourceDatacenter: The source datacenter from which the virtual machine relocated
       sourceDatastore: The source primary datastore from which the virtual machine relocated
   """
   sourceHost: HostEventArgument
   sourceDatacenter: _typing.Optional[DatacenterEventArgument] = None
   sourceDatastore: _typing.Optional[DatastoreEventArgument] = None

class VmRemoteConsoleConnectedEvent(VmEvent):
   """This event records that a remote console was connected to the VM"""
   pass

class VmRemoteConsoleDisconnectedEvent(VmEvent):
   """This event records that a remote console was disconnected from the VM"""
   pass

class VmRemovedEvent(VmEvent):
   """This event records a virtual machine removed from VirtualCenter management."""
   pass

class VmRenamedEvent(VmEvent):
   """
   This event records the renaming of a virtual machine.
   
   Attributes:
       oldName: The old name of the virtual machine.
       newName: The new name of the virtual machine.
   """
   oldName: str
   newName: str

class VmRequirementsExceedCurrentEVCModeEvent(VmEvent):
   """
   The virtual machine is using features that exceed what the
   host is capable of providing.
   
   This may occur when joining an EVC cluster
   while the virtual machine is powered on.
   The most common resolution is to power cycle the virtual machine.
   """
   pass

class VmResettingEvent(VmEvent):
   """This event records a virtual machine resetting."""
   pass

class VmResourcePoolMovedEvent(VmEvent):
   """
   This event records when a virtual machine is moved from one resource pool to another.
   
   Attributes:
       oldParent: The old parent resourcePool of the moved virtual machine.
       newParent: The new parent resourcePool of the moved virtual machine.
   """
   oldParent: ResourcePoolEventArgument
   newParent: ResourcePoolEventArgument


class VmResourceReallocatedEvent(VmEvent):
   """
   This event records a change in resource allocation of a virtual machine.
   
   Attributes:
       configChanges: The configuration values changed during the reconfiguration.
   """
   configChanges: _typing.Optional[ChangesInfoEventArgument] = None

class VmRestartedOnAlternateHostEvent(VmPoweredOnEvent):
   """
   Deprecated: As of vSphere API 5.0, the Server will generate the `pyVmomi.vim.event.EventEx` event
   with the `pyVmomi.vim.event.EventEx.eventTypeId` property set to \"com.vmware.vc.ha.VmRestartedByHAEvent\".This event records that the virtual machine was restarted on a host, since
   its original host had failed.
   
   Attributes:
       sourceHost: The host that failed.
   """
   sourceHost: HostEventArgument

class VmResumingEvent(VmEvent):
   """This event records a virtual machine resuming."""
   pass

class VmSecondaryAddedEvent(VmEvent):
   """This event records a secondary VM is added."""
   pass


class VmSecondaryDisabledBySystemEvent(VmEvent):
   """
   This event records that a fault tolerance secondary VM has been
   disabled by vCenter because the VM could not be powered on.
   """
   reason: _typing.Optional[pyVmomi.vmodl.MethodFault] = None

class VmSecondaryDisabledEvent(VmEvent):
   """This event records a secondary VM is disabled."""
   pass

class VmSecondaryEnabledEvent(VmEvent):
   """This event records a secondary VM is enabled."""
   pass

class VmSecondaryStartedEvent(VmEvent):
   """This event records a secondary VM is started successfully."""
   pass


class VmShutdownOnIsolationEvent(VmPoweredOffEvent):
   """
   This event records when a virtual machine has been shut down on an isolated host
   in a HA cluster.
   
   Attributes:
       isolatedHost: The isolated host on which a virtual machine was shutdown.
       shutdownResult: Indicates if the shutdown was successful.
           
           If the shutdown failed, the virtual
           machine was powered off. see `pyVmomi.vim.event.VmShutdownOnIsolationEvent.Operation`
   """
   class Operation(pyVmomi.VmomiSupport.Enum):
      """
      Attributes:
          shutdown: The virtual machine was shut down
          poweredOff: The virtual machine was powered off because shut down failed
      """
      shutdown: _typing.ClassVar['VmShutdownOnIsolationEvent.Operation'] = 'shutdown'
      poweredOff: _typing.ClassVar['VmShutdownOnIsolationEvent.Operation'] = 'poweredOff'

   isolatedHost: HostEventArgument
   shutdownResult: _typing.Optional[str] = None

class VmStartRecordingEvent(VmEvent):
   """Deprecated: as of vSphere API 6.0This event indicates the start of a recording session on a virtual machine."""
   pass

class VmStartReplayingEvent(VmEvent):
   """Deprecated: as of vSphere API 6.0This event indicates the start of a replay session on a virtual machine."""
   pass

class VmStartingEvent(VmEvent):
   """This event records a virtual machine powering on."""
   pass

class VmStartingSecondaryEvent(VmEvent):
   """This event records a vmotion to start a secondary VM."""
   pass

class VmStaticMacConflictEvent(VmEvent):
   """
   This event records a static MAC address conflict for a virtual machine.
   
   Attributes:
       conflictedVm: The virtual machine whose static MAC address conflicts with
           the current virtual machine's address.
       mac: The static MAC address that is in conflict.
   """
   conflictedVm: VmEventArgument
   mac: str

class VmStoppingEvent(VmEvent):
   """This event records a virtual machine stopping."""
   pass

class VmSuspendedEvent(VmEvent):
   """This event records when a virtual machine finished suspending."""
   pass

class VmSuspendingEvent(VmEvent):
   """This event records a virtual machine suspending."""
   pass


class VmTimedoutStartingSecondaryEvent(VmEvent):
   """
   This event records timeout when starting a secondary VM.
   
   A default alarm will be triggered upon this event, which by default
   would trigger a SNMP trap.
   
   Attributes:
       timeout: The duration of the timeout in milliseconds.
   """
   timeout: _typing.Optional[pyVmomi.VmomiSupport.long] = None

class VmUnsupportedStartingEvent(VmStartingEvent):
   """This event records when an unsupported guest is powering on."""
   guestId: str

class VmUpgradeCompleteEvent(VmEvent):
   """
   This event records the successful completion of an upgrade operation.
   
   Attributes:
       version: The version of the agent.
   """
   version: str

class VmUpgradeFailedEvent(VmEvent):
   """This event records a failure to upgrade virtual hardware."""
   pass

class VmUpgradingEvent(VmEvent):
   """
   This event records the process of upgrading the virtual hardware on a
   virtual machine.
   
   Attributes:
       version: The version of the agent.
   """
   version: str

class VmUuidAssignedEvent(VmEvent):
   """
   This event records the assignment of a new BIOS UUID
   to a virtual machine.
   
   Attributes:
       uuid: The new BIOS UUID.
   """
   uuid: str

class VmUuidChangedEvent(VmEvent):
   """
   This event records a change in a virtual machine's BIOS UUID.
   
   Attributes:
       oldUuid: The old BIOS UUID.
       newUuid: The new BIOS UUID.
   """
   oldUuid: str
   newUuid: str

class VmUuidConflictEvent(VmEvent):
   """
   This event records a conflict of virtual machine BIOS UUIDs.
   
   Attributes:
       conflictedVm: The virtual machine whose UUID conflicts with the
           current virtual machine's UUID.
       uuid: The BIOS UUID in conflict.
   """
   conflictedVm: VmEventArgument
   uuid: str


class VmVnicPoolReservationViolationClearEvent(DvsEvent):
   """
   This event is generated when the reservations used by all
   the virtual network adapters belonging to the virtual NIC network
   resource pool goes below the reservation allocated to the resource pool
   
   Attributes:
       vmVnicResourcePoolKey: The key of the Virtual NIC network resource pool
       vmVnicResourcePoolName: The name of the Virtual NIC network resource pool
   """
   vmVnicResourcePoolKey: str
   vmVnicResourcePoolName: _typing.Optional[str] = None


class VmVnicPoolReservationViolationRaiseEvent(DvsEvent):
   """
   This event is generated when the reservations used by all
   the virtual network adapters belonging to the virtual NIC network
   resource pool exceeds the reservation allocated to the resource pool
   
   Attributes:
       vmVnicResourcePoolKey: The key of the Virtual NIC network resource pool
       vmVnicResourcePoolName: The name of the Virtual NIC network resource pool
   """
   vmVnicResourcePoolKey: str
   vmVnicResourcePoolName: _typing.Optional[str] = None


class VmWwnAssignedEvent(VmEvent):
   """
   This event records the assignment of a new WWN (World Wide Name)
   to a virtual machine.
   
   Attributes:
       nodeWwns: The new node WWN.
       portWwns: The new port WWN.
   """
   nodeWwns: list[pyVmomi.VmomiSupport.long] = []
   portWwns: list[pyVmomi.VmomiSupport.long] = []


class VmWwnChangedEvent(VmEvent):
   """
   This event records a change in a virtual machine's WWN (World Wide Name).
   
   Attributes:
       oldNodeWwns: The old node WWN.
       oldPortWwns: The old port WWN.
       newNodeWwns: The new node WWN.
       newPortWwns: The new port WWN.
   """
   oldNodeWwns: list[pyVmomi.VmomiSupport.long] = []
   oldPortWwns: list[pyVmomi.VmomiSupport.long] = []
   newNodeWwns: list[pyVmomi.VmomiSupport.long] = []
   newPortWwns: list[pyVmomi.VmomiSupport.long] = []


class VmWwnConflictEvent(VmEvent):
   """
   This event records a conflict of virtual machine WWNs (World Wide Name).
   
   Attributes:
       conflictedVms: The virtual machine whose WWN conflicts with the
           current virtual machine's WWN.
       conflictedHosts: The host whose physical WWN conflicts with the
           current virtual machine's WWN.
       wwn: The WWN in conflict.
   """
   conflictedVms: list[VmEventArgument] = []
   conflictedHosts: list[HostEventArgument] = []
   wwn: pyVmomi.VmomiSupport.long


class VnicPortArgument(pyVmomi.vmodl.DynamicData):
   """
   This argument records a Virtual NIC device that connects to a DVPort.
   
   Attributes:
       vnic: The Virtual NIC devices that were using the DVports.
       port: The DVPorts that were being used.
   """
   vnic: str
   port: pyVmomi.vim.dvs.PortConnection

class WarningUpgradeEvent(UpgradeEvent):
   """This event is a general warning event from upgrade."""
   pass

class iScsiBootFailureEvent(HostEvent):
   """Could not boot from iScsi."""
   pass
