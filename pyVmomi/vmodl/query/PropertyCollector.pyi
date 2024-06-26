# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import ClassVar
from typing import NoReturn
from typing import Optional

from pyVmomi.VmomiSupport import Enum
from pyVmomi.VmomiSupport import ManagedObject
from pyVmomi.VmomiSupport import PropertyPath

from pyVmomi.vmodl import DynamicData
from pyVmomi.vmodl import DynamicProperty
from pyVmomi.vmodl import MethodFault

class PropertyCollector(ManagedObject):
   class FilterSpec(DynamicData):
      propSet: list[PropertySpec] = []
      objectSet: list[ObjectSpec] = []
      reportMissingObjectsInResults: Optional[bool] = None

   class PropertySpec(DynamicData):
      type: type
      all: Optional[bool] = None
      pathSet: list[PropertyPath] = []

   class ObjectSpec(DynamicData):
      obj: ManagedObject
      skip: Optional[bool] = None
      selectSet: list[SelectionSpec] = []

   class SelectionSpec(DynamicData):
      name: Optional[str] = None

   class TraversalSpec(SelectionSpec):
      type: type
      path: PropertyPath
      skip: Optional[bool] = None
      selectSet: list[SelectionSpec] = []

   class Filter(ManagedObject):
      @property
      def spec(self) -> FilterSpec: ...
      @property
      def partialUpdates(self) -> bool: ...

      def Destroy(self) -> NoReturn: ...

   class ObjectContent(DynamicData):
      obj: ManagedObject
      propSet: list[DynamicProperty] = []
      missingSet: list[MissingProperty] = []

   class UpdateSet(DynamicData):
      version: str
      filterSet: list[FilterUpdate] = []
      truncated: Optional[bool] = None

   class FilterUpdate(DynamicData):
      filter: Filter
      objectSet: list[ObjectUpdate] = []
      missingSet: list[MissingObject] = []

   class ObjectUpdate(DynamicData):
      class Kind(Enum):
         modify: ClassVar['Kind'] = 'modify'
         enter: ClassVar['Kind'] = 'enter'
         leave: ClassVar['Kind'] = 'leave'

      kind: Kind
      obj: ManagedObject
      changeSet: list[Change] = []
      missingSet: list[MissingProperty] = []

   class Change(DynamicData):
      class Op(Enum):
         add: ClassVar['Op'] = 'add'
         remove: ClassVar['Op'] = 'remove'
         assign: ClassVar['Op'] = 'assign'
         indirectRemove: ClassVar['Op'] = 'indirectRemove'

      name: PropertyPath
      op: Op
      val: Optional[object] = None

   class MissingProperty(DynamicData):
      path: PropertyPath
      fault: MethodFault

   class MissingObject(DynamicData):
      obj: ManagedObject
      fault: MethodFault

   class WaitOptions(DynamicData):
      maxWaitSeconds: Optional[int] = None
      maxObjectUpdates: Optional[int] = None

   class RetrieveOptions(DynamicData):
      maxObjects: Optional[int] = None

   class RetrieveResult(DynamicData):
      token: Optional[str] = None
      objects: list[ObjectContent] = []

   @property
   def filter(self) -> list[Filter]: ...

   def CreateFilter(self, spec: FilterSpec, partialUpdates: bool) -> Filter: ...
   def RetrieveContents(self, specSet: list[FilterSpec]) -> list[ObjectContent]: ...
   def CheckForUpdates(self, version: Optional[str]) -> Optional[UpdateSet]: ...
   def WaitForUpdates(self, version: Optional[str]) -> UpdateSet: ...
   def CancelWaitForUpdates(self) -> NoReturn: ...
   def WaitForUpdatesEx(self, version: Optional[str], options: Optional[WaitOptions]) -> Optional[UpdateSet]: ...
   def RetrievePropertiesEx(self, specSet: list[FilterSpec], options: RetrieveOptions) -> Optional[RetrieveResult]: ...
   def ContinueRetrievePropertiesEx(self, token: str) -> RetrieveResult: ...
   def CancelRetrievePropertiesEx(self, token: str) -> NoReturn: ...
   def CreatePropertyCollector(self) -> PropertyCollector: ...
   def Destroy(self) -> NoReturn: ...
