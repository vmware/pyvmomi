# Copyright (c) 2006-2026 Broadcom. All Rights Reserved.
# The term "Broadcom" refers to Broadcom Inc. and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

import datetime as _datetime
import typing as _typing
import pyVmomi.VmomiSupport
import pyVmomi.vim
import pyVmomi.vmodl
import pyVmomi.vim.action



class Alarm(pyVmomi.vim.ExtensibleManagedObject):
   """
   This managed object type defines an alarm that is triggered and
   an action that occurs due to the triggered alarm when certain conditions
   are met on a specific `pyVmomi.vim.ManagedEntity` object.
   """
   @property
   def info(self) -> AlarmInfo:
      """Information about this alarm."""
      ...

   def Remove(self) -> None:
      """Removes the alarm."""
      ...
   def Reconfigure(self, spec: AlarmSpec) -> None:
      """
      Reconfigures the alarm properties.
      
      This operation requires access
      privileges on the entity with which the alarm is associated.
      
      In addition to the Alarm.Edit privilege, may also require the
      Global.ScriptAction if a RunScriptAction action is specified in
      the AlarmSpec.
      
      Args:
          spec: The new specification for the alarm.
      
      Raises:
          pyVmomi.vim.fault.InvalidName: if the alarm name is empty or too long.
          pyVmomi.vim.fault.DuplicateName: if an alarm with the name already exists.
      """
      ...


class AlarmAction(pyVmomi.vmodl.DynamicData):
   """
   Action invoked by triggered alarm.
   
   This is an abstract type.
   """
   pass


class AlarmDescription(pyVmomi.vmodl.DynamicData):
   """
   Static strings for alarms.
   
   Attributes:
       expr: Descriptions of expression types for a trigger.
       stateOperator: `pyVmomi.vim.alarm.StateAlarmExpression.StateOperator`
       metricOperator: `pyVmomi.vim.alarm.MetricAlarmExpression.MetricOperator`
       hostSystemConnectionState: `pyVmomi.vim.HostSystem.ConnectionState`
       virtualMachinePowerState: `pyVmomi.vim.VirtualMachine.PowerState`
       datastoreConnectionState: `pyVmomi.vim.Datastore.Summary.accessible` and
           `pyVmomi.vim.host.MountInfo.accessible`
       hostSystemPowerState: `pyVmomi.vim.HostSystem.PowerState`
       virtualMachineGuestHeartbeatStatus: `pyVmomi.vim.ManagedEntity.Status`
       entityStatus: `pyVmomi.vim.ManagedEntity.Status`
       action: Action class descriptions for an alarm.
   """
   expr: list[pyVmomi.vim.TypeDescription] = []
   stateOperator: list[pyVmomi.vim.ElementDescription] = []
   metricOperator: list[pyVmomi.vim.ElementDescription] = []
   hostSystemConnectionState: list[pyVmomi.vim.ElementDescription] = []
   virtualMachinePowerState: list[pyVmomi.vim.ElementDescription] = []
   datastoreConnectionState: list[pyVmomi.vim.ElementDescription] = []
   hostSystemPowerState: list[pyVmomi.vim.ElementDescription] = []
   virtualMachineGuestHeartbeatStatus: list[pyVmomi.vim.ElementDescription] = []
   entityStatus: list[pyVmomi.vim.ElementDescription] = []
   action: list[pyVmomi.vim.TypeDescription] = []


class AlarmExpression(pyVmomi.vmodl.DynamicData):
   """
   Base type for the expressions specifying the conditions that define
   the status of an alarm.
   """
   pass


class AlarmFilterSpec(pyVmomi.vmodl.DynamicData):
   """
   Alarm Filter used to filter/group alarms.
   
   Attributes:
       status: Status array which could be used to filter alarms according to their
           triggered state.
           
           If all triggered alarms need to be matched an empty array or
           ManagedEntity::red and ManagedEntity::yellow could be filled in the array.
       typeEntity: Use values from `pyVmomi.vim.alarm.AlarmFilterSpec.AlarmTypeByEntity`
       typeTrigger: Use values from `pyVmomi.vim.alarm.AlarmFilterSpec.AlarmTypeByTrigger`
   """
   class AlarmTypeByEntity(pyVmomi.VmomiSupport.Enum):
      """
      Alarm entity type
      
      Attributes:
          entityTypeAll: Alarms on all entity types.
          entityTypeHost: Host alarms
          entityTypeVm: VM alarms
      """
      entityTypeAll: _typing.ClassVar['AlarmFilterSpec.AlarmTypeByEntity'] = 'entityTypeAll'
      entityTypeHost: _typing.ClassVar['AlarmFilterSpec.AlarmTypeByEntity'] = 'entityTypeHost'
      entityTypeVm: _typing.ClassVar['AlarmFilterSpec.AlarmTypeByEntity'] = 'entityTypeVm'

   class AlarmTypeByTrigger(pyVmomi.VmomiSupport.Enum):
      """
      Alarm triggering type.
      
      The main divisions are event triggered and
      metric- or state-based alarms.
      
      Attributes:
          triggerTypeAll: All alarm types.
          triggerTypeEvent: Event based alarms
          triggerTypeMetric: Metric or state alarms
      """
      triggerTypeAll: _typing.ClassVar['AlarmFilterSpec.AlarmTypeByTrigger'] = 'triggerTypeAll'
      triggerTypeEvent: _typing.ClassVar['AlarmFilterSpec.AlarmTypeByTrigger'] = 'triggerTypeEvent'
      triggerTypeMetric: _typing.ClassVar['AlarmFilterSpec.AlarmTypeByTrigger'] = 'triggerTypeMetric'

   status: list[pyVmomi.vim.ManagedEntity.Status] = []
   typeEntity: _typing.Optional[str] = None
   typeTrigger: _typing.Optional[str] = None


class AlarmSpec(pyVmomi.vmodl.DynamicData):
   """
   Parameters for alarm creation.
   
   Attributes:
       name: Name of the alarm.
       systemName: System name of the alarm.
           
           This is set only for predefined Alarms - i.e. Alarms created by the
           server or extensions automatically. After creation this value cannot be
           modified. User-created Alarms do not have a systemName at all.
           
           The purpose of this field is to identify system-created Alarms
           reliably, even if they are edited by users.
           
           When creating Alarms with systemName, the systemName and the name of the
           alarm should be equal.
           
           When reconfiguring an Alarm with systemName, the same systemName should
           be passed in the new AlarmSpec. Renaming Alarms with systemName is not
           allowed, i.e. when reconfiguring, the name passed in the new AlarmSpec
           should be equal to either the systemName or its localized version (the
           current name in the Alarm's info).
       description: Description of the alarm.
       enabled: Flag to indicate whether or not the alarm is enabled or disabled.
       expression: Top-level alarm expression that defines trigger conditions.
       action: Action to perform when the alarm is triggered.
       actionFrequency: Frequency in seconds, which specifies how often appropriate actions
           should repeat when an alarm does not change state.
       setting: Tolerance and maximum frequency settings.
   """
   name: str
   systemName: _typing.Optional[str] = None
   description: str
   enabled: bool
   expression: AlarmExpression
   action: _typing.Optional[AlarmAction] = None
   actionFrequency: _typing.Optional[int] = None
   setting: _typing.Optional[AlarmSetting] = None


class AlarmInfo(AlarmSpec):
   """
   Attributes of an alarm.
   
   Attributes:
       key: The unique key.
       alarm: The alarm object.
       entity: The entity on which the alarm is registered.
       lastModifiedTime: The time the alarm was created or modified.
       lastModifiedUser: User name that modified the alarm most recently.
       creationEventId: The event ID that records the alarm creation.
   """
   key: str
   alarm: Alarm
   entity: pyVmomi.vim.ManagedEntity
   lastModifiedTime: _datetime.datetime
   lastModifiedUser: str
   creationEventId: int


class AlarmManager(pyVmomi.VmomiSupport.ManagedObject):
   """
   The alarm manager is a singleton object for managing alarms
   within a service instance.
   """
   @property
   def defaultExpression(self) -> list[AlarmExpression]:
      """
      The default setting for each alarm expression, used to populate the
      initial client wizard screen.
      """
      ...
   @property
   def description(self) -> AlarmDescription:
      """The static descriptive strings used in alarms."""
      ...

   def Create(self, entity: pyVmomi.vim.ManagedEntity, spec: AlarmSpec) -> Alarm:
      """
      Creates an alarm.
      
      In addition to the Alarm.Create privilege, may also require the
      Global.ScriptAction if a RunScriptAction action is specified in
      the AlarmSpec.
      
      Args:
          entity: The entity with which the alarm is associated.
          spec: The specification for the new alarm.
      
      Returns:
          A reference to the Alarm object created by the
          operation.
      
      Raises:
          pyVmomi.vim.fault.InvalidName: if the alarm name is empty or too long.
          pyVmomi.vim.fault.DuplicateName: if an alarm with the name already exists.
      """
      ...
   def GetAlarm(self, entity: _typing.Optional[pyVmomi.vim.ManagedEntity]) -> list[Alarm]:
      """
      Available alarms defined on the entity.
      
      These alarms do not include any inherited alarms; that is,
      alarms associated with parent entities.
      
      Args:
          entity: The entity. If not set, alarms are returned for
              all visible entities.
      
      Returns:
          A reference to the Alarm objects returned by the
          operation.
      """
      ...
   def GetAlarmActionsEnabled(self, entity: pyVmomi.vim.ManagedEntity) -> bool:
      """
      Returns true if alarm actions are enabled on the specified managed entity.
      
      Args:
          entity: The managed entity to look up.
      """
      ...
   def SetAlarmActionsEnabled(self, entity: pyVmomi.vim.ManagedEntity, enabled: bool) -> None:
      """
      Enables or disables alarms on the specified managed entity.
      
      Args:
          entity: The managed entity on which to set a schedule.
          enabled: true, if alarms are enabled during the schedule.
      """
      ...
   def GetAlarmState(self, entity: pyVmomi.vim.ManagedEntity) -> list[AlarmState]:
      """
      The state of instantiated alarms on the entity.
      
      Args:
          entity: The entity.
      
      Returns:
          The state of instantiated alarms.
      """
      ...
   def AcknowledgeAlarm(self, alarm: Alarm, entity: pyVmomi.vim.ManagedEntity) -> None:
      """
      Acknowledge the alarm on a managed entity.
      
      The actions associated
      with the alarm will not fire until the alarm's next distinct
      occurrence; that is, until after the alarm has entered the green
      or gray states at least once. Calling this method on an acknowledged
      or non-triggered alarm.
      
      Args:
          alarm: The Alarm to acknowledge.
          entity: The ManagedEntity for which to acknowledge the Alarm.
      """
      ...
   def ClearTriggeredAlarms(self, filter: AlarmFilterSpec) -> None:
      """
      Resets all triggered alarms to green.
      
      Should be used when mass alarm reset is needed.
      """
      ...
   def DisableAlarm(self, alarm: Alarm, entity: pyVmomi.vim.ManagedEntity) -> None:
      """
      Disables alarm for a specific entity.
      
      Args:
          alarm: The Alarm being disabled.
          entity: The ManagedEntity on which to disable the alarm.
      """
      ...
   def EnableAlarm(self, alarm: Alarm, entity: pyVmomi.vim.ManagedEntity) -> None:
      """
      Enables alarm for a specific entity.
      
      Args:
          alarm: The Alarm being enabled.
          entity: The ManagedEntity on which to enable the alarm.
      """
      ...


class AlarmSetting(pyVmomi.vmodl.DynamicData):
   """
   Tolerance and frequency limits of an alarm.
   
   Attributes:
       toleranceRange: Tolerance range for the metric triggers, measured in one hundredth percentage.
           
           A zero value means that the alarm
           triggers whenever the metric value is above
           or below the specified value.
           A nonzero value means that the alarm
           triggers only after reaching a certain percentage
           above or below the nominal trigger value.
       reportingFrequency: How often the alarm is triggered, measured in seconds.
           
           A zero value means that the alarm is allowed
           to trigger as often as possible.
           A nonzero value means that any subsequent triggers
           are suppressed for a period of seconds following a
           reported trigger.
   """
   toleranceRange: int
   reportingFrequency: int


class AlarmState(pyVmomi.vmodl.DynamicData):
   """
   Information about the alarm's state.
   
   Attributes:
       key: Unique key that identifies the alarm.
       entity: Entity on which the alarm is instantiated.
       alarm: Alarm object from which the AlarmState object is instantiated.
       overallStatus: Overall status of the alarm object.
           
           This is the value of the alarm's top-level expression.
           In releases after vSphere API 5.0, vSphere Servers might not
           generate property collector update notifications for this property.
           To obtain the latest value of the property, you can use
           PropertyCollector methods RetrievePropertiesEx or WaitForUpdatesEx.
           If you use the PropertyCollector.WaitForUpdatesEx method, specify
           an empty string for the version parameter.
           Since this property is on a DataObject, an update returned by WaitForUpdatesEx may
           contain values for this property when some other property on the DataObject changes.
           If this update is a result of a call to WaitForUpdatesEx with a non-empty
           version parameter, the value for this property may not be current.
       time: Time the alarm triggered.
       acknowledged: Flag to indicate if the alarm's actions have been acknowledged for the
           associated ManagedEntity.
       acknowledgedByUser: The user who acknowledged this triggering.
           
           If the triggering has not
           been acknowledged, then the value is not valid.
       acknowledgedTime: The time this triggering was acknowledged.
           
           If the triggering has not
           been acknowledged, then the value is not valid.
       eventKey: Contains the key of the event that has triggered the alarm.
           
           The value
           is set only for event based alarms. The value is not set for gray or
           manually reset alarms (via vim.AlarmManager.setAlarmStatus).
       disabled: Flag to indicate if the alarm is disabled for the associated
           ManagedEntity.
   """
   key: str
   entity: pyVmomi.vim.ManagedEntity
   alarm: Alarm
   overallStatus: pyVmomi.vim.ManagedEntity.Status
   time: _datetime.datetime
   acknowledged: _typing.Optional[bool] = None
   acknowledgedByUser: _typing.Optional[str] = None
   acknowledgedTime: _typing.Optional[_datetime.datetime] = None
   eventKey: _typing.Optional[int] = None
   disabled: _typing.Optional[bool] = None


class AlarmTriggeringAction(AlarmAction):
   """
   This data object type describes one or more
   triggering transitions and an action to be done
   when an alarm is triggered.
   
   There are four triggering transitions; at least one of them must
   be provided. A gray state is considered the same as a green state,
   for the purpose of detecting transitions.
   
   Attributes:
       action: The action to be done when the alarm is triggered.
       transitionSpecs: Indicates on which transitions this action executes and repeats.
           
           This is optional only for backwards compatibility.
       green2yellow: Flag to specify that the alarm should trigger on a transition
           from green to yellow.
       yellow2red: Flag to specify that the alarm should trigger on a transition
           from yellow to red.
       red2yellow: Flag to specify that the alarm should trigger on a transition
           from red to yellow.
       yellow2green: Flag to specify that the alarm should trigger on a transition
           from yellow to green.
   """
   class TransitionSpec(pyVmomi.vmodl.DynamicData):
      """
      Specification indicating which on transitions this action fires.
      
      The existence of a Spec indicates that this action fires on
      transitions from that Spec's startState to finalState.
      
      There are six acceptable {startState, finalState} pairs:
      {green, yellow}, {green, red}, {yellow, red}, {red, yellow},
      {red, green} and {yellow, green}.
      Direct transitions have precedence over indirect.
      At least one of these pairs must be specified.
      Any deviation from the above will render the enclosing AlarmSpec invalid.
      
      Attributes:
          startState: The state from which the alarm must transition for the action to
              fire.
              
              Valid choices are red, yellow and green.
          finalState: The state to which the alarm must transition for the action to fire.
              
              Valid choices are red, yellow, and green.
          repeats: Whether or not the action repeats, as per the actionFrequency defined
              in the enclosing Alarm.
      """
      startState: pyVmomi.vim.ManagedEntity.Status
      finalState: pyVmomi.vim.ManagedEntity.Status
      repeats: bool

   action: pyVmomi.vim.action.Action
   transitionSpecs: list[AlarmTriggeringAction.TransitionSpec] = []
   green2yellow: bool
   yellow2red: bool
   red2yellow: bool
   yellow2green: bool

class AndAlarmExpression(AlarmExpression):
   """
   A data object type that links multiple alarm expressions with AND operators.
   
   Attributes:
       expression: List of alarm expressions that define the overall status of the alarm.
           - The state of the alarm expression is gray if all subexpressions are gray.
             Otherwise, gray subexpressions are ignored.
           - The state is red if all subexpressions are red.
           - Otherwise, the state is yellow if all subexpressions are red or yellow.
           - Otherwise, the state of the alarm expression is green.
   """
   expression: list[AlarmExpression] = []


class EventAlarmExpression(AlarmExpression):
   """
   An alarm expression that uses the event stream to trigger the alarm.
   
   This alarm is triggered when an event matching this expression gets logged.
   
   Attributes:
       comparisons: The attributes/values to compare.
       eventType: The type of the event to trigger the alarm on.
       eventTypeId: The eventTypeId of the event to match.
           
           The semantics of how eventTypeId matching is done is as follows:
           - If the event being matched is of type `pyVmomi.vim.event.EventEx`
             or `pyVmomi.vim.event.ExtendedEvent`, then we match this value
             against the `eventTypeId` (for `EventEx`) or
             `eventId` (for `ExtendedEvent`) member of the Event.
           - Otherwise, we match it against the type of the Event itself.
             
           Either `eventType` or `eventTypeId` must
           be set.
       objectType: Name of the type of managed object on which the event is logged.
           
           An event alarm defined on a `pyVmomi.vim.ManagedEntity`
           is propagated to child entities in the VirtualCenter inventory depending
           on the value of this attribute. If objectType is any of the following,
           the alarm is propagated down to all children of that type:
           - A datacenter: `pyVmomi.vim.Datacenter`.
           - A cluster of host systems: `pyVmomi.vim.ClusterComputeResource`.
           - A single host system: `pyVmomi.vim.HostSystem`.
           - A resource pool representing a set of physical resources on a single host:
             `pyVmomi.vim.ResourcePool`.
           - A virtual machine: `pyVmomi.vim.VirtualMachine`.
           - A datastore: `pyVmomi.vim.Datastore`.
           - A network: `pyVmomi.vim.Network`.
           - A distributed virtual switch: `pyVmomi.vim.DistributedVirtualSwitch`.
             
           If objectType is unspecified or not contained in the above list,
           the event alarm is not propagated down to child entities in the
           VirtualCenter inventory.
           
           It is possible to specify an event alarm containing two (or more) different
           EventAlarmExpression's which contain different objectTypes. In such a case,
           the event is propagated to all child entities with specified type(s).
       status: The alarm's new state when this condition is evaluated and satisfied.
           
           If not specified then there is no change to alarm status, and all
           actions are fired (rather than those for the transition).
   """
   class ComparisonOperator(pyVmomi.VmomiSupport.Enum):
      """
      Basic Comparison operators
      
      Attributes:
          equals: attribute equals specified value
          notEqualTo: attribute does not equal specified value
          startsWith: attribute starts with specified value
          doesNotStartWith: attribute does not start with specified value
          endsWith: attribute ends with specified value
          doesNotEndWith: attribute does not end with specified value
      """
      equals: _typing.ClassVar['EventAlarmExpression.ComparisonOperator'] = 'equals'
      notEqualTo: _typing.ClassVar['EventAlarmExpression.ComparisonOperator'] = 'notEqualTo'
      startsWith: _typing.ClassVar['EventAlarmExpression.ComparisonOperator'] = 'startsWith'
      doesNotStartWith: _typing.ClassVar['EventAlarmExpression.ComparisonOperator'] = 'doesNotStartWith'
      endsWith: _typing.ClassVar['EventAlarmExpression.ComparisonOperator'] = 'endsWith'
      doesNotEndWith: _typing.ClassVar['EventAlarmExpression.ComparisonOperator'] = 'doesNotEndWith'

   class Comparison(pyVmomi.vmodl.DynamicData):
      """
      Encapsulates Comparison of an event's attribute to a value.
      
      Attributes:
          attributeName: The attribute of the event to compare
          operator: An operator from the list above
          value: The value to compare against
      """
      attributeName: str
      operator: str
      value: str

   comparisons: list[EventAlarmExpression.Comparison] = []
   eventType: type
   eventTypeId: _typing.Optional[str] = None
   objectType: _typing.Optional[type] = None
   status: _typing.Optional[pyVmomi.vim.ManagedEntity.Status] = None

class GroupAlarmAction(AlarmAction):
   """
   This data object type describes a group of
   actions that occur when the alarm is triggered.
   
   These actions are not
   necessarily executed in order.
   
   Attributes:
       action: The list of alarm actions that occur when the alarm is triggered.
   """
   action: list[AlarmAction] = []


class MetricAlarmExpression(AlarmExpression):
   """
   An alarm expression that uses a metric as the condition that triggers an
   alarm.
   
   Base type.
   
   There are two alarm operands: yellow and red. At least one of them
   must be set. The value of the alarm expression is determined as follows:
   - If the host is not connected, the host metric expression is gray.
   - If the vm is not connected, the vm metric expression is gray.
   - If red is set but yellow is not, the expression is red when
     the metric is over (isAbove operator) or under (isBelow operator)
     the red value. Otherwise, the expression is green.
   - If yellow is set but red is not, the expression is yellow when
     the metric is over (isAbove) or under (isBelow)
     the yellow value. Otherwise, the expression is green.
   - If both yellow and red are set, the value of the expression is red
     when the metric is over (isAbove) or under (isBelow) the red value.
     Otherwise, the expression is yellow when the metric is over (isAbove)
     or under (isBelow) the yellow value. Otherwise, the expression is green.
   
   Attributes:
       operator: The operation to be tested on the metric.
       type: Name of the object type containing the property.
       metric: The instance of the metric.
       yellow: Whether or not to test for a yellow condition.
           
           If not set, do not calculate yellow status.
           If set, it contains the threshold value that triggers yellow status.
       yellowInterval: Time interval in seconds for which the yellow condition must be true
           before the yellow status is triggered.
           
           If unset, the yellow status is
           triggered immediately when the yellow condition becomes true.
       red: Whether or not to test for a red condition.
           
           If not set, do not calculate red status.
           If set, it contains the threshold value that triggers red status.
       redInterval: Time interval in seconds for which the red condition must be true
           before the red status is triggered.
           
           If unset, the red status is
           triggered immediately when the red condition becomes true.
   """
   class MetricOperator(pyVmomi.VmomiSupport.Enum):
      """
      The operation on the target metric item.
      
      Attributes:
          isAbove: Test if the target metric item is above the given red or yellow values.
          isBelow: Test if the target metric item is below the given red or yellow values.
      """
      isAbove: _typing.ClassVar['MetricAlarmExpression.MetricOperator'] = 'isAbove'
      isBelow: _typing.ClassVar['MetricAlarmExpression.MetricOperator'] = 'isBelow'

   operator: MetricAlarmExpression.MetricOperator
   type: type
   metric: pyVmomi.vim.PerformanceManager.MetricId
   yellow: _typing.Optional[int] = None
   yellowInterval: _typing.Optional[int] = None
   red: _typing.Optional[int] = None
   redInterval: _typing.Optional[int] = None

class OrAlarmExpression(AlarmExpression):
   """
   A data object type that links multiple alarm expressions with OR operators.
   
   Attributes:
       expression: List of alarm expressions that define the overall status of the alarm.
           - The state of the alarm expression is gray if all subexpressions are gray.
             Otherwise, gray subexpressions are ignored.
           - The state is red if any subexpression is red.
           - Otherwise, the state is yellow if any subexpression is yellow.
           - Otherwise, the state of the alarm expression is green.
   """
   expression: list[AlarmExpression] = []


class StateAlarmExpression(AlarmExpression):
   """
   An alarm expression that uses the running state of either a virtual machine or
   a host as the condition that triggers the alarm.
   
   Base type.
   
   There are two alarm operands: yellow and red. At least one of them
   must be set. The value of the alarm expression is determined as follows:
   - If the red state is set but the yellow state is not: the expression is red when
     the state operand matches (isEqual operator) or does not match (isUnequal operator)
     the state of the managed entity. The expression is green otherwise.
   - If yellow is set but red is not: the expression is yellow when
     the state operand matches (isEqual) or does not match (isUnequal)
     the state of the managed entity. The expression is green otherwise.
   - If both yellow and red are set, the value of the expression is red when
     the red state operand matches (isEqual) or does not match (isUnequal)
     the state of the managed entity. Otherwise, the expression is
     yellow when the yellow state operand matches (isEqual) or does not match (isUnequal)
     the state of the managed entity. Otherwise, the expression is green.
   
   Attributes:
       operator: The operation to be tested on the target state.
       type: Name of the object type containing the property.
       statePath: Path of the state property.
           
           The supported values:
           - for vim.VirtualMachine type:
           - runtime.powerState or summary.quickStats.guestHeartbeatStatus
           - for vim.HostSystem type: runtime.connectionState
       yellow: Whether or not to test for a yellow condition.
           
           If this property is not set, do not calculate yellow status.
       red: Whether or not to test for a red condition.
           
           If this property is not set, do not calculate red status.
   """
   class StateOperator(pyVmomi.VmomiSupport.Enum):
      """
      The operation on the target state.
      
      Attributes:
          isEqual: Test if the target state matches the given red or yellow states.
          isUnequal: Test if the target state does not match the given red or yellow states.
      """
      isEqual: _typing.ClassVar['StateAlarmExpression.StateOperator'] = 'isEqual'
      isUnequal: _typing.ClassVar['StateAlarmExpression.StateOperator'] = 'isUnequal'

   operator: StateAlarmExpression.StateOperator
   type: type
   statePath: pyVmomi.VmomiSupport.PropertyPath
   yellow: _typing.Optional[str] = None
   red: _typing.Optional[str] = None
