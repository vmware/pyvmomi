from typing import List
from enum import Enum
from pyVmomi import vmodl
from pyVmomi.VmomiSupport import ManagedObject, NoneType, PropertyPath


class PropertyCollector(ManagedObject):
    @property
    def filter(self) -> List[PropertyCollector.Filter]: ...
    def CreateFilter(self, spec: PropertyCollector.FilterSpec, partialUpdates: bool) -> PropertyCollector.Filter: ...
    def RetrieveContents(self, specSet: List[PropertyCollector.FilterSpec]) -> List[PropertyCollector.ObjectContent]: ...
    def CheckForUpdates(self, version: str) -> PropertyCollector.UpdateSet: ...
    def WaitForUpdates(self, version: str) -> PropertyCollector.UpdateSet: ...
    def CancelWaitForUpdates(self) -> NoneType: ...
    def WaitForUpdatesEx(self, version: str, options: PropertyCollector.WaitOptions) -> PropertyCollector.UpdateSet: ...
    def RetrievePropertiesEx(self, specSet: List[PropertyCollector.FilterSpec], options: PropertyCollector.RetrieveOptions) -> PropertyCollector.RetrieveResult: ...
    def ContinueRetrievePropertiesEx(self, token: str) -> PropertyCollector.RetrieveResult: ...
    def CancelRetrievePropertiesEx(self, token: str) -> NoneType: ...
    def CreatePropertyCollector(self) -> PropertyCollector: ...
    def Destroy(self) -> NoneType: ...


    class Filter(ManagedObject):
        @property
        def spec(self) -> PropertyCollector.FilterSpec: ...
        @property
        def partialUpdates(self) -> bool: ...
        def Destroy(self) -> NoneType: ...


    class Change(vmodl.DynamicData):
        @property
        def name(self) -> PropertyPath: ...
        @name.setter
        def name(self, value: PropertyPath):
            self._name = value
        @property
        def op(self) -> PropertyCollector.Change.Op: ...
        @op.setter
        def op(self, value: PropertyCollector.Change.Op):
            self._op = value
        @property
        def val(self) -> object: ...
        @val.setter
        def val(self, value: object):
            self._val = value


        class Op(Enum):
            add = "add"
            remove = "remove"
            assign = "assign"
            indirectRemove = "indirectRemove"


    class FilterSpec(vmodl.DynamicData):
        @property
        def propSet(self) -> List[PropertyCollector.PropertySpec]: ...
        @propSet.setter
        def propSet(self, value: List[PropertyCollector.PropertySpec]):
            self._propSet = value
        @property
        def objectSet(self) -> List[PropertyCollector.ObjectSpec]: ...
        @objectSet.setter
        def objectSet(self, value: List[PropertyCollector.ObjectSpec]):
            self._objectSet = value
        @property
        def reportMissingObjectsInResults(self) -> bool: ...
        @reportMissingObjectsInResults.setter
        def reportMissingObjectsInResults(self, value: bool):
            self._reportMissingObjectsInResults = value


    class FilterUpdate(vmodl.DynamicData):
        @property
        def filter(self) -> PropertyCollector.Filter: ...
        @filter.setter
        def filter(self, value: PropertyCollector.Filter):
            self._filter = value
        @property
        def objectSet(self) -> List[PropertyCollector.ObjectUpdate]: ...
        @objectSet.setter
        def objectSet(self, value: List[PropertyCollector.ObjectUpdate]):
            self._objectSet = value
        @property
        def missingSet(self) -> List[PropertyCollector.MissingObject]: ...
        @missingSet.setter
        def missingSet(self, value: List[PropertyCollector.MissingObject]):
            self._missingSet = value


    class MissingObject(vmodl.DynamicData):
        @property
        def obj(self) -> ManagedObject: ...
        @obj.setter
        def obj(self, value: ManagedObject):
            self._obj = value
        @property
        def fault(self) -> vmodl.MethodFault: ...
        @fault.setter
        def fault(self, value: vmodl.MethodFault):
            self._fault = value


    class MissingProperty(vmodl.DynamicData):
        @property
        def path(self) -> PropertyPath: ...
        @path.setter
        def path(self, value: PropertyPath):
            self._path = value
        @property
        def fault(self) -> vmodl.MethodFault: ...
        @fault.setter
        def fault(self, value: vmodl.MethodFault):
            self._fault = value


    class ObjectContent(vmodl.DynamicData):
        @property
        def obj(self) -> ManagedObject: ...
        @obj.setter
        def obj(self, value: ManagedObject):
            self._obj = value
        @property
        def propSet(self) -> List[vmodl.DynamicProperty]: ...
        @propSet.setter
        def propSet(self, value: List[vmodl.DynamicProperty]):
            self._propSet = value
        @property
        def missingSet(self) -> List[PropertyCollector.MissingProperty]: ...
        @missingSet.setter
        def missingSet(self, value: List[PropertyCollector.MissingProperty]):
            self._missingSet = value


    class ObjectSpec(vmodl.DynamicData):
        @property
        def obj(self) -> ManagedObject: ...
        @obj.setter
        def obj(self, value: ManagedObject):
            self._obj = value
        @property
        def skip(self) -> bool: ...
        @skip.setter
        def skip(self, value: bool):
            self._skip = value
        @property
        def selectSet(self) -> List[PropertyCollector.SelectionSpec]: ...
        @selectSet.setter
        def selectSet(self, value: List[PropertyCollector.SelectionSpec]):
            self._selectSet = value


    class ObjectUpdate(vmodl.DynamicData):
        @property
        def kind(self) -> PropertyCollector.ObjectUpdate.Kind: ...
        @kind.setter
        def kind(self, value: PropertyCollector.ObjectUpdate.Kind):
            self._kind = value
        @property
        def obj(self) -> ManagedObject: ...
        @obj.setter
        def obj(self, value: ManagedObject):
            self._obj = value
        @property
        def changeSet(self) -> List[PropertyCollector.Change]: ...
        @changeSet.setter
        def changeSet(self, value: List[PropertyCollector.Change]):
            self._changeSet = value
        @property
        def missingSet(self) -> List[PropertyCollector.MissingProperty]: ...
        @missingSet.setter
        def missingSet(self, value: List[PropertyCollector.MissingProperty]):
            self._missingSet = value


        class Kind(Enum):
            modify = "modify"
            enter = "enter"
            leave = "leave"


    class PropertySpec(vmodl.DynamicData):
        @property
        def type(self) -> type: ...
        @type.setter
        def type(self, value: type):
            self._type = value
        @property
        def all(self) -> bool: ...
        @all.setter
        def all(self, value: bool):
            self._all = value
        @property
        def pathSet(self) -> List[PropertyPath]: ...
        @pathSet.setter
        def pathSet(self, value: List[PropertyPath]):
            self._pathSet = value


    class RetrieveOptions(vmodl.DynamicData):
        @property
        def maxObjects(self) -> int: ...
        @maxObjects.setter
        def maxObjects(self, value: int):
            self._maxObjects = value


    class RetrieveResult(vmodl.DynamicData):
        @property
        def token(self) -> str: ...
        @token.setter
        def token(self, value: str):
            self._token = value
        @property
        def objects(self) -> List[PropertyCollector.ObjectContent]: ...
        @objects.setter
        def objects(self, value: List[PropertyCollector.ObjectContent]):
            self._objects = value


    class SelectionSpec(vmodl.DynamicData):
        @property
        def name(self) -> str: ...
        @name.setter
        def name(self, value: str):
            self._name = value


    class TraversalSpec(PropertyCollector.SelectionSpec):
        @property
        def type(self) -> type: ...
        @type.setter
        def type(self, value: type):
            self._type = value
        @property
        def path(self) -> PropertyPath: ...
        @path.setter
        def path(self, value: PropertyPath):
            self._path = value
        @property
        def skip(self) -> bool: ...
        @skip.setter
        def skip(self, value: bool):
            self._skip = value
        @property
        def selectSet(self) -> List[PropertyCollector.SelectionSpec]: ...
        @selectSet.setter
        def selectSet(self, value: List[PropertyCollector.SelectionSpec]):
            self._selectSet = value


    class UpdateSet(vmodl.DynamicData):
        @property
        def version(self) -> str: ...
        @version.setter
        def version(self, value: str):
            self._version = value
        @property
        def filterSet(self) -> List[PropertyCollector.FilterUpdate]: ...
        @filterSet.setter
        def filterSet(self, value: List[PropertyCollector.FilterUpdate]):
            self._filterSet = value
        @property
        def truncated(self) -> bool: ...
        @truncated.setter
        def truncated(self, value: bool):
            self._truncated = value


    class WaitOptions(vmodl.DynamicData):
        @property
        def maxWaitSeconds(self) -> int: ...
        @maxWaitSeconds.setter
        def maxWaitSeconds(self, value: int):
            self._maxWaitSeconds = value
        @property
        def maxObjectUpdates(self) -> int: ...
        @maxObjectUpdates.setter
        def maxObjectUpdates(self, value: int):
            self._maxObjectUpdates = value


class InvalidCollectorVersion(vmodl.MethodFault): ...


class InvalidProperty(vmodl.MethodFault):
    @property
    def name(self) -> PropertyPath: ...
    @name.setter
    def name(self, value: PropertyPath):
        self._name = value