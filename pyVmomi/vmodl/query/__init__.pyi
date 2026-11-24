# Copyright (c) 2006-2026 Broadcom. All Rights Reserved.
# The term "Broadcom" refers to Broadcom Inc. and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

import typing as _typing
import pyVmomi.VmomiSupport
import pyVmomi.vmodl



class InvalidCollectorVersion(pyVmomi.vmodl.MethodFault):
   """
   InvalidCollectorVersion is thrown when a collector version is out
   of date or invalid.
   """
   pass


class InvalidProperty(pyVmomi.vmodl.MethodFault):
   """
   Thrown when an invalid property path has been referenced.
   
   Attributes:
       name: The property name that generated the error.
   """
   name: pyVmomi.VmomiSupport.PropertyPath


class PropertyCollector(pyVmomi.VmomiSupport.ManagedObject):
   """
   The `pyVmomi.vmodl.query.PropertyCollector` managed object retrieves and detects changes
   to the properties of other managed objects.
   
   The `pyVmomi.vmodl.query.PropertyCollector.retrievePropertiesEx` method provides one-time property retrieval. The
   `pyVmomi.vmodl.query.PropertyCollector.waitForUpdatesEx` method provides incremental change detection and
   supports both polling and notification.
   
   For change detection a client creates one or more filters to specify the
   subset of managed objects in which the client is interested. Filters keep
   per-session state to track incremental changes. Because this state is
   per-session:
   - A session cannot share its `pyVmomi.vmodl.query.PropertyCollector` filters with other
     sessions
   - two different clients can share the same session, and so can
     share the same filters, but this is not recommended
   - When a session terminates, the associated `pyVmomi.vmodl.query.PropertyCollector` filters
     are automatically destroyed.
   """
   class FilterSpec(pyVmomi.vmodl.DynamicData):
      """
      Specify the property data that is included in a filter.
      
      A filter can
      specify part of a single managed object, or parts of multiple related
      managed objects in an inventory hierarchy - for example, to collect
      updates from all virtual machines in a given folder.
      
      Attributes:
          propSet: Set of properties to include in the filter, specified for each object
              type.
          objectSet: Set of specifications that determine the objects to filter.
          reportMissingObjectsInResults: Control how to report missing objects during filter creation.
              
              If false or unset and `pyVmomi.vmodl.query.PropertyCollector.FilterSpec.objectSet` refers to missing objects,
              filter creation will fail with a `pyVmomi.vmodl.fault.ManagedObjectNotFound` fault.
              
              If true and `pyVmomi.vmodl.query.PropertyCollector.FilterSpec.objectSet` refers
              to missing objects, filter creation will not fail and missing objects
              will be reported via filter results. This is the recommended setting
              when `pyVmomi.vmodl.query.PropertyCollector.FilterSpec.objectSet` refers to
              transient objects.
              
              In an `pyVmomi.vmodl.query.PropertyCollector.UpdateSet` missing objects will
              appear in the `pyVmomi.vmodl.query.PropertyCollector.FilterUpdate.missingSet` field.
              
              In a `pyVmomi.vmodl.query.PropertyCollector.RetrieveResult` missing objects will
              simply be omitted from the objects field.
              
              For a call to `pyVmomi.vmodl.query.PropertyCollector.retrieveContents` missing objects will simply
              be omitted from the results.
      """
      propSet: list[PropertyCollector.PropertySpec] = []
      objectSet: list[PropertyCollector.ObjectSpec] = []
      reportMissingObjectsInResults: _typing.Optional[bool] = None

   class PropertySpec(pyVmomi.vmodl.DynamicData):
      """
      Within a `pyVmomi.vmodl.query.PropertyCollector.FilterSpec`, A `pyVmomi.vmodl.query.PropertyCollector.PropertySpec` specifies which properties should be
      reported to the client for objects of the given managed object type that
      are visited and not skipped.
      
      One more subtle side effect is that if a
      managed object is visited and not skipped, but there is no `pyVmomi.vmodl.query.PropertyCollector.PropertySpec` associated with the managed object's
      type, the managed object will not be reported to the client.
      
      Also, the set of properties applicable to a given managed object type
      is the union of the properties implied by the `pyVmomi.vmodl.query.PropertyCollector.PropertySpec` objects even, in the case of a `pyVmomi.vmodl.query.PropertyCollector.RetrieveResult`, where there may be an applicable
      `pyVmomi.vmodl.query.PropertyCollector.PropertySpec` in more than one filter.
      
      Attributes:
          type: Name of the managed object type being collected.
          all: Specifies whether or not all properties of the object are read.
              
              If
              this property is set to true, the `pyVmomi.vmodl.query.PropertyCollector.PropertySpec.pathSet` property is ignored.
          pathSet: Specifies which managed object properties are retrieved.
              
              If the `pyVmomi.vmodl.query.PropertyCollector.PropertySpec.pathSet` is empty, then the
              `pyVmomi.vmodl.query.PropertyCollector` retrieves references to the managed objects
              and no managed object properties are collected.
      """
      type: type
      all: _typing.Optional[bool] = None
      pathSet: list[pyVmomi.VmomiSupport.PropertyPath] = []

   class ObjectSpec(pyVmomi.vmodl.DynamicData):
      """
      Within a `pyVmomi.vmodl.query.PropertyCollector.FilterSpec`, the `pyVmomi.vmodl.query.PropertyCollector.ObjectSpec` data object type specifies the managed
      object at which the filter begins to collect the managed object
      references and properties specified by the associated `pyVmomi.vmodl.query.PropertyCollector.PropertySpec` set.
      
      If the \"skip\" property is present
      and set to true, then the filter does not check to see if the starting
      object's type matches any of the types listed in the associated sets of
      `pyVmomi.vmodl.query.PropertyCollector.PropertySpec` data objects.
      
      If the `pyVmomi.vmodl.query.PropertyCollector.ObjectSpec.selectSet` property is
      present, then this specifies additional objects to filter. These objects
      are defined by one or more `pyVmomi.vmodl.query.PropertyCollector.SelectionSpec`
      objects.
      
      Attributes:
          obj: Starting object.
          skip: Flag to specify whether or not to report this managed object's
              properties.
              
              If the flag is true, the filter will not report this
              managed object's properties.
          selectSet: Set of selections to specify additional objects to filter.
      """
      obj: pyVmomi.VmomiSupport.ManagedObject
      skip: _typing.Optional[bool] = None
      selectSet: list[PropertyCollector.SelectionSpec] = []

   class SelectionSpec(pyVmomi.vmodl.DynamicData):
      """
      The `pyVmomi.vmodl.query.PropertyCollector.SelectionSpec` is the base type for data
      object types that specify what additional objects to filter.
      
      The base
      type contains only an optional \"name\" field, which allows a selection to
      be named for future reference. More information is available in the
      subtype.
      
      Named selections support recursive specifications on an object
      hierarchy. When used by a derived object, the \"name\" field allows other
      `pyVmomi.vmodl.query.PropertyCollector.SelectionSpec` objects to refer to the object by
      name. When used as the base type only, the \"name\" field indicates
      recursion to the derived object by name.
      
      Names are meaningful only within the same FilterSpec.
      
      Attributes:
          name: Name of the selection specification.
      """
      name: _typing.Optional[str] = None

   class TraversalSpec(PropertyCollector.SelectionSpec):
      """
      The `pyVmomi.vmodl.query.PropertyCollector.TraversalSpec` data object type specifies
      how to derive a new set of objects to add to the filter.
      
      It specifies a property path whose value is either another managed
      object or an array of managed objects included in the set of objects for
      consideration. This data object can also be named, using the \"name\"
      field in the base type.
      
      Attributes:
          type: Name of the object type containing the property.
          path: Name of the property to use in order to select additional objects.
          skip: Flag to indicate whether or not to filter the object in the \"path\"
              field.
          selectSet: Optional set of selections to specify additional objects to filter.
      """
      type: type
      path: pyVmomi.VmomiSupport.PropertyPath
      skip: _typing.Optional[bool] = None
      selectSet: list[PropertyCollector.SelectionSpec] = []

   class Filter(pyVmomi.VmomiSupport.ManagedObject):
      """
      The `pyVmomi.vmodl.query.PropertyCollector.Filter` managed object type defines a filter
      that controls the properties for which a `pyVmomi.vmodl.query.PropertyCollector` detects
      incremental changes.
      
      Filters are subordinate objects; they are part of the `pyVmomi.vmodl.query.PropertyCollector` and do not have independent lifetimes. A Filter
      is automatically destroyed when the session on which it was created is
      closed or the `pyVmomi.vmodl.query.PropertyCollector` on which it was created is
      destroyed.
      """
      @property
      def spec(self) -> PropertyCollector.FilterSpec:
         """Specifications for this filter."""
         ...
      @property
      def partialUpdates(self) -> bool:
         """
         Flag to indicate if a change to a nested property reports only the
         nested change or the entire specified property value.
         
         If the value is
         true, a change reports only the nested property. If the value is
         false, a change reports the enclosing property named in the filter.
         """
         ...

      def Destroy(self) -> None:
         """
         Destroys this filter.
         
         This operation can be called explicitly, or it can take place
         implicitly when the session that created the filter is closed.
         """
         ...

   class ObjectContent(pyVmomi.vmodl.DynamicData):
      """
      The `pyVmomi.vmodl.query.PropertyCollector.ObjectContent` data object type contains the
      contents retrieved for a single managed object.
      
      Attributes:
          obj: Reference to the managed object that contains properties of interest.
          propSet: Set of name-value pairs for the properties of the managed object.
          missingSet: Properties for which values could not be retrieved and the associated
              fault.
      """
      obj: pyVmomi.VmomiSupport.ManagedObject
      propSet: list[pyVmomi.vmodl.DynamicProperty] = []
      missingSet: list[PropertyCollector.MissingProperty] = []

   class UpdateSet(pyVmomi.vmodl.DynamicData):
      """
      A set of updates that represent the changes since a prior call to `pyVmomi.vmodl.query.PropertyCollector.checkForUpdates`, `pyVmomi.vmodl.query.PropertyCollector.waitForUpdates`, or `pyVmomi.vmodl.query.PropertyCollector.waitForUpdatesEx`.
      
      Attributes:
          version: New data version to pass in the next call to `pyVmomi.vmodl.query.PropertyCollector.checkForUpdates`,
              `pyVmomi.vmodl.query.PropertyCollector.waitForUpdates`, or `pyVmomi.vmodl.query.PropertyCollector.waitForUpdatesEx`.
              
              These versions,
              although they are opaque, are strongly ordered in the sense that passing
              a version to `pyVmomi.vmodl.query.PropertyCollector.waitForUpdates`, `pyVmomi.vmodl.query.PropertyCollector.checkForUpdates` or
              `pyVmomi.vmodl.query.PropertyCollector.waitForUpdatesEx` requests updates that reflect changes in the
              objects selected by the Filter that happened after the specified version.
          filterSet: Set of managed object updates detected by specific filters.
              
              Updates
              are reported in sets. Each set is associated with a reference to a
              filter that detected the updates in the set.
          truncated: If true, this `pyVmomi.vmodl.query.PropertyCollector.UpdateSet` contains results
              from a suspended change calculation, which places restrictions on the
              use of version.
              
              The `pyVmomi.vmodl.query.PropertyCollector` may suspend a calculation due to server
              policy or if the total number of `pyVmomi.vmodl.query.PropertyCollector.ObjectUpdate` entries summed across every `pyVmomi.vmodl.query.PropertyCollector.FilterUpdate` reached the maximum specified in
              `pyVmomi.vmodl.query.PropertyCollector.WaitOptions.maxObjectUpdates`. The client
              can pass the \"truncated data version\" to `pyVmomi.vmodl.query.PropertyCollector.waitForUpdatesEx` to
              resume the update calculation, which will start on the filter where it
              left off. A truncated data version cannot be used more than once and
              may not be passed to `pyVmomi.vmodl.query.PropertyCollector.checkForUpdates` or `pyVmomi.vmodl.query.PropertyCollector.waitForUpdates`. `pyVmomi.vmodl.query.PropertyCollector.UpdateSet.truncated` will
              never be true in an `pyVmomi.vmodl.query.PropertyCollector.UpdateSet` returned from
              `pyVmomi.vmodl.query.PropertyCollector.checkForUpdates` or `pyVmomi.vmodl.query.PropertyCollector.waitForUpdates`.
              
              If false, this `pyVmomi.vmodl.query.PropertyCollector.UpdateSet` contains a
              complete change calculation or the last part of a series of suspended
              change calculations. The version may be passed to `pyVmomi.vmodl.query.PropertyCollector.checkForUpdates`, `pyVmomi.vmodl.query.PropertyCollector.waitForUpdates`, or `pyVmomi.vmodl.query.PropertyCollector.waitForUpdatesEx` more than once. Re-using a version allows a client
              to recover a change sequence after a transient failure on a previous
              call.
      """
      version: str
      filterSet: list[PropertyCollector.FilterUpdate] = []
      truncated: _typing.Optional[bool] = None

   class FilterUpdate(pyVmomi.vmodl.DynamicData):
      """
      The `pyVmomi.vmodl.query.PropertyCollector.FilterUpdate` data object type contains a
      list of updates to data visible through a specific filter.
      
      Note that if a
      property changes through multiple filters, then a client receives an
      update for each filter.
      
      Attributes:
          filter: Filter that was updated.
          objectSet: Set of changes to object properties in the filter.
          missingSet: Objects that could not be found on the server, but were specified in a
              `pyVmomi.vmodl.query.PropertyCollector.FilterSpec.objectSet`.
              
              This field will only be populated for objects that were determined
              to be missing since the data version passed to `pyVmomi.vmodl.query.PropertyCollector.checkForUpdates`, `pyVmomi.vmodl.query.PropertyCollector.waitForUpdates`, or `pyVmomi.vmodl.query.PropertyCollector.waitForUpdatesEx` and will not contain objects that were missing
              prior to that data version.
      """
      filter: PropertyCollector.Filter
      objectSet: list[PropertyCollector.ObjectUpdate] = []
      missingSet: list[PropertyCollector.MissingObject] = []

   class ObjectUpdate(pyVmomi.vmodl.DynamicData):
      """
      The `pyVmomi.vmodl.query.PropertyCollector.ObjectUpdate` data object type contains
      information about changes to a particular managed object.
      
      We distinguish
      updates when an object is created, destroyed, or modified, as well as
      when the object enters or leaves the set of objects dynamically
      associated with a filter.
      
      Attributes:
          kind: Kind of update that caused the filter to report a change.
          obj: Reference to the managed object to which this update applies.
          changeSet: Optional set of changes to the object.
              
              Present only if the \"kind\" is
              either \"modify\" or \"enter\".
          missingSet: Properties whose value could not be retrieved and their associated
              faults.
              
              Present only if the \"kind\" is either \"modify\" or \"enter\".
      """
      class Kind(pyVmomi.VmomiSupport.Enum):
         """
         Enumeration of different kinds of updates.
         
         Attributes:
             modify: A property of the managed object changed its value.
             enter: A managed object became visible to a filter for the first time.
                 
                 For instance, this can happen if a virtual machine is added to a
                 folder.
             leave: A managed object left the set of objects visible to a filter.
                 
                 For
                 instance, this can happen when a virtual machine is destroyed.
         """
         modify: _typing.ClassVar['PropertyCollector.ObjectUpdate.Kind'] = 'modify'
         enter: _typing.ClassVar['PropertyCollector.ObjectUpdate.Kind'] = 'enter'
         leave: _typing.ClassVar['PropertyCollector.ObjectUpdate.Kind'] = 'leave'

      kind: PropertyCollector.ObjectUpdate.Kind
      obj: pyVmomi.VmomiSupport.ManagedObject
      changeSet: list[PropertyCollector.Change] = []
      missingSet: list[PropertyCollector.MissingProperty] = []

   class Change(pyVmomi.vmodl.DynamicData):
      """
      Describes a change to a property.
      
      Attributes:
          name: Property or nested property to which the change applies.
              
              Nested
              properties are specified by paths; for example,
              - foo.bar
              - foo.arProp[\"key val\"]
              - foo.arProp[\"key val\"].baz
          op: Change operation for the property.
              
              Valid values are:
              
              add: 
              The property is a collection and the change inserts an element
              into the collection.
              
              remove: 
              The property is a collection and the change deletes an element
              from the collection.
              
              assign: 
              The change is a new value for the property.
              
              indirectRemove: 
              The property was removed because a containing property was removed
              or unset
          val: New value for the property when \"op\" is either \"add\" or \"assign\".
      """
      class Op(pyVmomi.VmomiSupport.Enum):
         """Enumeration of possible changes to a property."""
         add: _typing.ClassVar['PropertyCollector.Change.Op'] = 'add'
         remove: _typing.ClassVar['PropertyCollector.Change.Op'] = 'remove'
         assign: _typing.ClassVar['PropertyCollector.Change.Op'] = 'assign'
         indirectRemove: _typing.ClassVar['PropertyCollector.Change.Op'] = 'indirectRemove'

      name: pyVmomi.VmomiSupport.PropertyPath
      op: PropertyCollector.Change.Op
      val: _typing.Optional[object] = None

   class MissingProperty(pyVmomi.vmodl.DynamicData):
      """
      Used for reporting properties for which values could not be retrieved.
      
      Attributes:
          path: Property for which a value could not be retrieved
          fault: Fault describing the failure to retrieve the property value.
              
              The possible faults for missing properties are:
              - `pyVmomi.vmodl.fault.SystemError` if there was some unknown problem
                reading the value
              - `pyVmomi.vmodl.fault.SecurityError` if the logged in session did
                not have permission to read the value
      """
      path: pyVmomi.VmomiSupport.PropertyPath
      fault: pyVmomi.vmodl.MethodFault

   class MissingObject(pyVmomi.vmodl.DynamicData):
      """
      Used for reporting missing objects that were explicitly referenced by a
      filter spec.
      
      In other words, any of the objects referenced in `pyVmomi.vmodl.query.PropertyCollector.FilterSpec.objectSet`
      
      Attributes:
          obj: The object that is being reported missing
          fault: Fault describing the failure to lookup this object
              
              The possible faults for missing objects are:
              - `pyVmomi.vmodl.fault.SystemError` if there was some unknown problem
                looking up the object
              - `pyVmomi.vmodl.fault.ManagedObjectNotFound` if the object is no
                longer available
      """
      obj: pyVmomi.VmomiSupport.ManagedObject
      fault: pyVmomi.vmodl.MethodFault

   class WaitOptions(pyVmomi.vmodl.DynamicData):
      """
      Options for `pyVmomi.vmodl.query.PropertyCollector.waitForUpdatesEx`.
      
      Attributes:
          maxWaitSeconds: The number of seconds the `pyVmomi.vmodl.query.PropertyCollector` should wait
              before returning null.
              
              Returning updates may take longer if the
              actual calculation time exceeds `pyVmomi.vmodl.query.PropertyCollector.WaitOptions.maxWaitSeconds`. Additionally `pyVmomi.vmodl.query.PropertyCollector` policy may
              cause it to return null sooner than `pyVmomi.vmodl.query.PropertyCollector.WaitOptions.maxWaitSeconds`.
              
              An unset value causes `pyVmomi.vmodl.query.PropertyCollector.waitForUpdatesEx` to wait as
              long as possible for updates. Policy may still cause the
              `pyVmomi.vmodl.query.PropertyCollector` to return null at some point.
              
              A value of 0 causes `pyVmomi.vmodl.query.PropertyCollector.waitForUpdatesEx` to do one update
              calculation and return any results. This behavior is similar to `pyVmomi.vmodl.query.PropertyCollector.checkForUpdates`.
              
              A positive value causes `pyVmomi.vmodl.query.PropertyCollector.waitForUpdatesEx` to return
              null if no updates are available within the specified number of
              seconds. The choice of a positive value often depends on the
              client communication stack. For example it may be helpful to
              choose a duration shorter than a local HTTP request timeout.
              Typically it should be no shorter than a few minutes.
              
              A negative value is illegal.
          maxObjectUpdates: The maximum number of `pyVmomi.vmodl.query.PropertyCollector.ObjectUpdate`
              entries that should be returned in a single result from `pyVmomi.vmodl.query.PropertyCollector.waitForUpdatesEx`.
              
              See `pyVmomi.vmodl.query.PropertyCollector.UpdateSet.truncated`
              
              An unset value indicates that there is no maximum. In this case
              `pyVmomi.vmodl.query.PropertyCollector` policy may still limit the number of objects
              that appear in an `pyVmomi.vmodl.query.PropertyCollector.UpdateSet`.
              
              A positive value causes `pyVmomi.vmodl.query.PropertyCollector.waitForUpdatesEx` to suspend
              the update calculation when the total count of `pyVmomi.vmodl.query.PropertyCollector.ObjectUpdate` entries ready to return reaches
              the specified maximum. `pyVmomi.vmodl.query.PropertyCollector` policy may still
              limit the total count to something less than `pyVmomi.vmodl.query.PropertyCollector.WaitOptions.maxObjectUpdates`.
              
              A value less than or equal to 0 is illegal.
      """
      maxWaitSeconds: _typing.Optional[int] = None
      maxObjectUpdates: _typing.Optional[int] = None

   class RetrieveOptions(pyVmomi.vmodl.DynamicData):
      """
      Options for `pyVmomi.vmodl.query.PropertyCollector.retrievePropertiesEx`.
      
      Attributes:
          maxObjects: The maximum number of `pyVmomi.vmodl.query.PropertyCollector.ObjectContent` data
              objects that should be returned in a single result from `pyVmomi.vmodl.query.PropertyCollector.retrievePropertiesEx`.
              
              An unset value indicates that there is no maximum. In this
              case `pyVmomi.vmodl.query.PropertyCollector` policy may still limit the number
              of objects. Any remaining objects may be retrieved with `pyVmomi.vmodl.query.PropertyCollector.continueRetrievePropertiesEx`.
              
              A positive value causes `pyVmomi.vmodl.query.PropertyCollector.retrievePropertiesEx` to
              suspend the retrieval when the count of objects reaches the
              specified maximum. `pyVmomi.vmodl.query.PropertyCollector` policy may still
              limit the count to something less than `pyVmomi.vmodl.query.PropertyCollector.RetrieveOptions.maxObjects`. Any remaining
              objects may be retrieved with `pyVmomi.vmodl.query.PropertyCollector.continueRetrievePropertiesEx`.
              
              A value less than or equal to 0 is illegal.
      """
      maxObjects: _typing.Optional[int] = None

   class RetrieveResult(pyVmomi.vmodl.DynamicData):
      """
      Result of `pyVmomi.vmodl.query.PropertyCollector.retrievePropertiesEx` and `pyVmomi.vmodl.query.PropertyCollector.continueRetrievePropertiesEx`
      
      Attributes:
          token: A token used to retrieve further retrieve results.
              
              If set, the token should be passed to `pyVmomi.vmodl.query.PropertyCollector.continueRetrievePropertiesEx` to retrieve more results. Each token
              may be passed to continueRetrievePropertiesEx only once, and only in
              the same session in which it was returned and to the same
              `pyVmomi.vmodl.query.PropertyCollector` object that returned it.
              
              If unset, there are no further results to retrieve after this
              `pyVmomi.vmodl.query.PropertyCollector.RetrieveResult`.
          objects: retrieved objects.
      """
      token: _typing.Optional[str] = None
      objects: list[PropertyCollector.ObjectContent] = []

   @property
   def filter(self) -> list[PropertyCollector.Filter]:
      """
      The filters that this `pyVmomi.vmodl.query.PropertyCollector` uses to determine the list of
      properties for which it detects incremental changes.
      """
      ...

   def CreateFilter(self, spec: PropertyCollector.FilterSpec, partialUpdates: bool) -> PropertyCollector.Filter:
      """
      Creates a new filter for the given set of managed objects.
      
      Args:
          spec: The specifications for the filter.
          partialUpdates: Flag to specify whether a change to a nested property should report
              only the nested change or the entire specified property value. If the
              value is true, a change should report only the nested property. If
              the value is false, a change should report the enclosing property
              named in the filter.
      
      Returns:
          A reference to the new filter.
      
      Raises:
          pyVmomi.vmodl.query.InvalidProperty: if \"spec\" has a property that is not defined on one of the objects.
      """
      ...
   def RetrieveContents(self, specSet: list[PropertyCollector.FilterSpec]) -> list[PropertyCollector.ObjectContent]:
      """
      Deprecated: As of vSphere API 4.1, use `pyVmomi.vmodl.query.PropertyCollector.retrievePropertiesEx`.Retrieves the specified properties of the specified managed objects.
      
      This method is similar to creating the filters, receiving the
      property values, and destroying the filters. The main difference is that
      the output blends the results from all the filters and reports a given
      managed object at most once no matter how many filters apply.
      
      The method isn't requiring any privilege, because it's used to
      access properties that are publicly available, without authenticated
      session. That isn't sequrity isse, because the property collector is
      doing another explicit access evaluation and it's returning data only
      from objects to which the user has access.
      
      The filter creation step can throw all of the same faults as `pyVmomi.vmodl.query.PropertyCollector.createFilter`.
      
      Args:
          specSet: Specifies the properties to retrieve.
      
      Returns:
          The data contents of the specified objects.
      
      Raises:
          pyVmomi.vmodl.query.InvalidProperty: See `pyVmomi.vmodl.query.PropertyCollector.createFilter`
      """
      ...
   def CheckForUpdates(self, version: _typing.Optional[str]) -> _typing.Optional[PropertyCollector.UpdateSet]:
      """
      Deprecated: As of vSphere API 4.1, use
      `pyVmomi.vmodl.query.PropertyCollector.waitForUpdatesEx` with a
      `pyVmomi.vmodl.query.PropertyCollector.WaitOptions.maxWaitSeconds` of 0.Checks for updates on properties specified by the union of all current
      filters.
      
      If no updates are pending, this method returns null.
      
      Args:
          version: The data version currently known to the client. The value
              must be either
              - the special initial version (an empty string)
              - a data version returned from `pyVmomi.vmodl.query.PropertyCollector.checkForUpdates` or `pyVmomi.vmodl.query.PropertyCollector.waitForUpdates` by the same `pyVmomi.vmodl.query.PropertyCollector` on the same session.
              - a non-truncated data version returned from `pyVmomi.vmodl.query.PropertyCollector.waitForUpdatesEx` by the same `pyVmomi.vmodl.query.PropertyCollector` on the same
                session.
      
      Returns:
          Changes since the passed in data version. If no updates are
          pending, then this method returns null.
      
      Raises:
          pyVmomi.vmodl.query.InvalidCollectorVersion: if the data version does not meet the
              requirements above.
      """
      ...
   def WaitForUpdates(self, version: _typing.Optional[str]) -> PropertyCollector.UpdateSet:
      """
      Deprecated: As of vSphere API 4.1, use `pyVmomi.vmodl.query.PropertyCollector.waitForUpdatesEx`.Calculate the set of updates for each existing filter in the session,
      returning when at least one filter has updates.
      
      Args:
          version: The data version currently known to the client. The value
              must be either
              - the special initial version (an empty string)
              - a data version returned from `pyVmomi.vmodl.query.PropertyCollector.checkForUpdates` or `pyVmomi.vmodl.query.PropertyCollector.waitForUpdates` by the same `pyVmomi.vmodl.query.PropertyCollector` on the same session
              - a non-truncated data version returned from `pyVmomi.vmodl.query.PropertyCollector.waitForUpdatesEx` by the same `pyVmomi.vmodl.query.PropertyCollector` on the same
                session.
      
      Returns:
          Changes since the passed in data version.
      
      Raises:
          pyVmomi.vmodl.query.InvalidCollectorVersion: if the data version does not meet the
              requirements above.
      """
      ...
   def CancelWaitForUpdates(self) -> None:
      """
      Attempts to cancel outstanding calls to `pyVmomi.vmodl.query.PropertyCollector.waitForUpdates` or `pyVmomi.vmodl.query.PropertyCollector.waitForUpdatesEx` in the current session.
      
      If an update calculation is
      in process this method has no effect. If an update calculation is not in
      process any waiting calls complete quickly and report a `pyVmomi.vmodl.fault.RequestCanceled` fault.
      """
      ...
   def WaitForUpdatesEx(self, version: _typing.Optional[str], options: _typing.Optional[PropertyCollector.WaitOptions]) -> _typing.Optional[PropertyCollector.UpdateSet]:
      """
      Calculate the set of updates for each existing filter in the session.
      
      `pyVmomi.vmodl.query.PropertyCollector.waitForUpdatesEx` may return only partial update
      calculations. See `pyVmomi.vmodl.query.PropertyCollector.UpdateSet.truncated` for a
      more detailed explanation. `pyVmomi.vmodl.query.PropertyCollector.waitForUpdatesEx` may also return null
      after a timeout, either as requested by `pyVmomi.vmodl.query.PropertyCollector.WaitOptions.maxWaitSeconds` or due to `pyVmomi.vmodl.query.PropertyCollector`
      policy.
      
      If an application uses waitForUpdatesEx it is strongly recommended
      that it not make concurrent calls to `pyVmomi.vmodl.query.PropertyCollector.waitForUpdates`, `pyVmomi.vmodl.query.PropertyCollector.checkForUpdates`, or `pyVmomi.vmodl.query.PropertyCollector.waitForUpdatesEx` in the same
      session. Concurrent calls may cause suspended change calculations to be
      discarded.
      
      Args:
          version: The data version currently known to the client. The value must be
              either
              - the special initial data version (an empty string),
              - a data version returned from `pyVmomi.vmodl.query.PropertyCollector.checkForUpdates` or `pyVmomi.vmodl.query.PropertyCollector.waitForUpdates`
              - a non-truncated data version returned from `pyVmomi.vmodl.query.PropertyCollector.waitForUpdatesEx`
              - a truncated data version returned from the last call to `pyVmomi.vmodl.query.PropertyCollector.waitForUpdatesEx` with no intervening calls to `pyVmomi.vmodl.query.PropertyCollector.waitForUpdates` or `pyVmomi.vmodl.query.PropertyCollector.checkForUpdates`.
          options: Additional options controlling the change calculation. If omitted,
              equivalent to an options argument with no fields set.
      
      Returns:
          Changes since the passed in version or null if there are no
          changes.
      
      Raises:
          pyVmomi.vmodl.query.InvalidCollectorVersion: if the data version does not meet the
              requirements above.
      """
      ...
   def RetrievePropertiesEx(self, specSet: list[PropertyCollector.FilterSpec], options: PropertyCollector.RetrieveOptions) -> _typing.Optional[PropertyCollector.RetrieveResult]:
      """
      Retrieves the specified properties of the specified managed objects.
      
      This method is similar to creating the filters, receiving the
      property values, and destroying the filters. The main difference is that
      the output blends the results from all the filters and reports a given
      managed object at most once no matter how many filters apply.
      
      The method isn't requiring any privilege, because it's used to
      access properties that are publicly available, without authenticated
      session. That isn't sequrity isse, because the property collector is
      doing another explicit access evaluation and it's returning data only
      from objects to which the user has access.
      
      The filter creation step can throw all of the same faults as `pyVmomi.vmodl.query.PropertyCollector.createFilter`.
      
      Args:
          specSet: Specifies the properties to retrieve.
          options: Additional method options. If omitted, equivalent to an options
              argument with no fields set.
      
      Returns:
          retrieved objects or null if there are no matching objects.
      
      Raises:
          pyVmomi.vmodl.query.InvalidProperty: See `pyVmomi.vmodl.query.PropertyCollector.createFilter`
      """
      ...
   def ContinueRetrievePropertiesEx(self, token: str) -> PropertyCollector.RetrieveResult:
      """
      Retrieves additional results from a retrieval started by `pyVmomi.vmodl.query.PropertyCollector.retrievePropertiesEx` on the same session on the same `pyVmomi.vmodl.query.PropertyCollector`.
      
      Args:
          token: the token returned in the previous `pyVmomi.vmodl.query.PropertyCollector.RetrieveResult` returned on the same session by the
              same `pyVmomi.vmodl.query.PropertyCollector`.
      
      Returns:
          retrieved objects.
      
      Raises:
          pyVmomi.vmodl.query.InvalidProperty: Thrown when an invalid property path has been referenced.
      """
      ...
   def CancelRetrievePropertiesEx(self, token: str) -> None:
      """
      Discards remaining results from a retrieval started by `pyVmomi.vmodl.query.PropertyCollector.retrievePropertiesEx` on the same session on the same `pyVmomi.vmodl.query.PropertyCollector`.
      
      Args:
          token: the token returned in the previous `pyVmomi.vmodl.query.PropertyCollector.RetrieveResult` returned on the same session by the
              same `pyVmomi.vmodl.query.PropertyCollector`.
      
      Raises:
          pyVmomi.vmodl.query.InvalidProperty: Thrown when an invalid property path has been referenced.
      """
      ...
   def CreatePropertyCollector(self) -> PropertyCollector:
      """
      Creates a new session-specific `pyVmomi.vmodl.query.PropertyCollector` that can
      be used to retrieve property updates independent of any other
      `pyVmomi.vmodl.query.PropertyCollector`.
      
      The newly created `pyVmomi.vmodl.query.PropertyCollector`
      is not tied to the creating `pyVmomi.vmodl.query.PropertyCollector` in any way and
      exists until it is destroyed
      by a call to `pyVmomi.vmodl.query.PropertyCollector.destroy` or until the session
      on which the PropertyCollector was created is closed. This is in contrast
      to the default `pyVmomi.vmodl.query.PropertyCollector`, which always exists, but still has
      session-specific data such as filters and unfinished update calculations
      that are discarded when the associated session is closed.
      
      A new `pyVmomi.vmodl.query.PropertyCollector` can be useful when multiple modules or even
      multiple clients that share the
      same session need to create their own `pyVmomi.vmodl.query.PropertyCollector.Filter`
      objects and process updates independently. They may also be useful
      to allow important updates to be seen on one `pyVmomi.vmodl.query.PropertyCollector` while
      a large update is being calculated on another. The underlying
      issue that this addresses is that any call to `pyVmomi.vmodl.query.PropertyCollector.waitForUpdates`,
      `pyVmomi.vmodl.query.PropertyCollector.checkForUpdates`, or `pyVmomi.vmodl.query.PropertyCollector.waitForUpdatesEx` does updates on all the
      filters created on a given `pyVmomi.vmodl.query.PropertyCollector` on a given session.
      
      A more subtle use of multiple `pyVmomi.vmodl.query.PropertyCollector` objects is implied
      by the fact that the returned version value for the various updates
      calculations is strongly ordered. The only way this can make sense is that
      two different versions calculated on the same `pyVmomi.vmodl.query.PropertyCollector` on
      the same session cannot ever be created in parallel. This means that multiple
      calls to `pyVmomi.vmodl.query.PropertyCollector.waitForUpdates`, `pyVmomi.vmodl.query.PropertyCollector.checkForUpdates`, or
      `pyVmomi.vmodl.query.PropertyCollector.waitForUpdatesEx` made to the same `pyVmomi.vmodl.query.PropertyCollector` on the
      same session on different threads of the same client, or even on different
      clients that share the same session are still handled on the server serially.
      Use of different `pyVmomi.vmodl.query.PropertyCollector` instances allows the server to
      handle these calculations in parallel.
      
      Typically a service that supports the `pyVmomi.vmodl.query.PropertyCollector` managed
      object type will automatically create a default `pyVmomi.vmodl.query.PropertyCollector`
      and provide some way to obtain a reference to this
      `pyVmomi.vmodl.query.PropertyCollector`. If not, it will have to provide some
      service-specific way to create the a `pyVmomi.vmodl.query.PropertyCollector`.
      
      Returns:
          A reference to the new `pyVmomi.vmodl.query.PropertyCollector`.
      """
      ...
   def Destroy(self) -> None:
      """
      Destroys this `pyVmomi.vmodl.query.PropertyCollector`.
      
      A `pyVmomi.vmodl.query.PropertyCollector` that was created by
      `pyVmomi.vmodl.query.PropertyCollector.createPropertyCollector` is automatically destroyed when the
      session on which it was created is closed. This method can be used to
      destroy them explicitly.
      
      An automatically created `pyVmomi.vmodl.query.PropertyCollector` provided by a service
      is not session specific and may not be destroyed.
      """
      ...
