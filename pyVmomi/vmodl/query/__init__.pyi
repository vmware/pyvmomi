# Copyright (c) 2006-2026 Broadcom. All Rights Reserved.
# The term "Broadcom" refers to Broadcom Inc. and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

import typing as _typing
import pyVmomi.VmomiSupport
import pyVmomi.vmodl



class InvalidCollectorVersion(pyVmomi.vmodl.MethodFault):
   pass


class InvalidProperty(pyVmomi.vmodl.MethodFault):
   name: pyVmomi.VmomiSupport.PropertyPath


class PropertyCollector(pyVmomi.VmomiSupport.ManagedObject):
   class FilterSpec(pyVmomi.vmodl.DynamicData):
      propSet: list[PropertySpec] = []
      objectSet: list[ObjectSpec] = []
      reportMissingObjectsInResults: _typing.Optional[bool] = None

   class PropertySpec(pyVmomi.vmodl.DynamicData):
      type: type
      all: _typing.Optional[bool] = None
      pathSet: list[pyVmomi.VmomiSupport.PropertyPath] = []

   class ObjectSpec(pyVmomi.vmodl.DynamicData):
      obj: pyVmomi.VmomiSupport.ManagedObject
      skip: _typing.Optional[bool] = None
      selectSet: list[SelectionSpec] = []

   class SelectionSpec(pyVmomi.vmodl.DynamicData):
      name: _typing.Optional[str] = None

   class TraversalSpec(SelectionSpec):
      type: type
      path: pyVmomi.VmomiSupport.PropertyPath
      skip: _typing.Optional[bool] = None
      selectSet: list[SelectionSpec] = []

   class Filter(pyVmomi.VmomiSupport.ManagedObject):
      @property
      def spec(self) -> FilterSpec: ...
      @property
      def partialUpdates(self) -> bool: ...

      def Destroy(self) -> None: ...

   class ObjectContent(pyVmomi.vmodl.DynamicData):
      obj: pyVmomi.VmomiSupport.ManagedObject
      propSet: list[pyVmomi.vmodl.DynamicProperty] = []
      missingSet: list[MissingProperty] = []

   class UpdateSet(pyVmomi.vmodl.DynamicData):
      version: str
      filterSet: list[FilterUpdate] = []
      truncated: _typing.Optional[bool] = None

   class FilterUpdate(pyVmomi.vmodl.DynamicData):
      filter: Filter
      objectSet: list[ObjectUpdate] = []
      missingSet: list[MissingObject] = []

   class ObjectUpdate(pyVmomi.vmodl.DynamicData):
      class Kind(pyVmomi.VmomiSupport.Enum):
         modify: _typing.ClassVar['Kind'] = 'modify'
         enter: _typing.ClassVar['Kind'] = 'enter'
         leave: _typing.ClassVar['Kind'] = 'leave'

      kind: Kind
      obj: pyVmomi.VmomiSupport.ManagedObject
      changeSet: list[Change] = []
      missingSet: list[MissingProperty] = []

   class Change(pyVmomi.vmodl.DynamicData):
      class Op(pyVmomi.VmomiSupport.Enum):
         add: _typing.ClassVar['Op'] = 'add'
         remove: _typing.ClassVar['Op'] = 'remove'
         assign: _typing.ClassVar['Op'] = 'assign'
         indirectRemove: _typing.ClassVar['Op'] = 'indirectRemove'

      name: pyVmomi.VmomiSupport.PropertyPath
      op: Op
      val: _typing.Optional[object] = None

   class MissingProperty(pyVmomi.vmodl.DynamicData):
      path: pyVmomi.VmomiSupport.PropertyPath
      fault: pyVmomi.vmodl.MethodFault

   class MissingObject(pyVmomi.vmodl.DynamicData):
      obj: pyVmomi.VmomiSupport.ManagedObject
      fault: pyVmomi.vmodl.MethodFault

   class WaitOptions(pyVmomi.vmodl.DynamicData):
      maxWaitSeconds: _typing.Optional[int] = None
      maxObjectUpdates: _typing.Optional[int] = None

   class RetrieveOptions(pyVmomi.vmodl.DynamicData):
      maxObjects: _typing.Optional[int] = None

   class RetrieveResult(pyVmomi.vmodl.DynamicData):
      token: _typing.Optional[str] = None
      objects: list[ObjectContent] = []

   @property
   def filter(self) -> list[Filter]: ...

   def CreateFilter(self, spec: FilterSpec, partialUpdates: bool) -> Filter: ...
   def RetrieveContents(self, specSet: list[FilterSpec]) -> list[ObjectContent]: ...
   def CheckForUpdates(self, version: _typing.Optional[str]) -> _typing.Optional[UpdateSet]: ...
   def WaitForUpdates(self, version: _typing.Optional[str]) -> UpdateSet: ...
   def CancelWaitForUpdates(self) -> None: ...
   def WaitForUpdatesEx(self, version: _typing.Optional[str], options: _typing.Optional[WaitOptions]) -> _typing.Optional[UpdateSet]: ...
   def RetrievePropertiesEx(self, specSet: list[FilterSpec], options: RetrieveOptions) -> _typing.Optional[RetrieveResult]: ...
   def ContinueRetrievePropertiesEx(self, token: str) -> RetrieveResult: ...
   def CancelRetrievePropertiesEx(self, token: str) -> None: ...
   def CreatePropertyCollector(self) -> PropertyCollector: ...
   def Destroy(self) -> None: ...
