from typing import List
from pyVmomi import pbm, vmodl
from pyVmomi.VmomiSupport import ManagedObject


class CapabilityMetadataManager(ManagedObject): ...


class CapabilityInstance(vmodl.DynamicData):
    @property
    def id(self) -> CapabilityMetadata.UniqueId: ...
    @id.setter
    def id(self, value: CapabilityMetadata.UniqueId):
        self._id = value
    @property
    def constraint(self) -> List[ConstraintInstance]: ...
    @constraint.setter
    def constraint(self, value: List[ConstraintInstance]):
        self._constraint = value


class CapabilityMetadata(vmodl.DynamicData):
    @property
    def id(self) -> CapabilityMetadata.UniqueId: ...
    @id.setter
    def id(self, value: CapabilityMetadata.UniqueId):
        self._id = value
    @property
    def summary(self) -> pbm.ExtendedElementDescription: ...
    @summary.setter
    def summary(self, value: pbm.ExtendedElementDescription):
        self._summary = value
    @property
    def mandatory(self) -> bool: ...
    @mandatory.setter
    def mandatory(self, value: bool):
        self._mandatory = value
    @property
    def hint(self) -> bool: ...
    @hint.setter
    def hint(self, value: bool):
        self._hint = value
    @property
    def keyId(self) -> str: ...
    @keyId.setter
    def keyId(self, value: str):
        self._keyId = value
    @property
    def allowMultipleConstraints(self) -> bool: ...
    @allowMultipleConstraints.setter
    def allowMultipleConstraints(self, value: bool):
        self._allowMultipleConstraints = value
    @property
    def propertyMetadata(self) -> List[PropertyMetadata]: ...
    @propertyMetadata.setter
    def propertyMetadata(self, value: List[PropertyMetadata]):
        self._propertyMetadata = value


    class UniqueId(vmodl.DynamicData):
        @property
        def namespace(self) -> str: ...
        @namespace.setter
        def namespace(self, value: str):
            self._namespace = value
        @property
        def id(self) -> str: ...
        @id.setter
        def id(self, value: str):
            self._id = value


class ConstraintInstance(vmodl.DynamicData):
    @property
    def propertyInstance(self) -> List[PropertyInstance]: ...
    @propertyInstance.setter
    def propertyInstance(self, value: List[PropertyInstance]):
        self._propertyInstance = value


class GenericTypeInfo(TypeInfo):
    @property
    def genericTypeName(self) -> str: ...
    @genericTypeName.setter
    def genericTypeName(self, value: str):
        self._genericTypeName = value


class PropertyInstance(vmodl.DynamicData):
    @property
    def id(self) -> str: ...
    @id.setter
    def id(self, value: str):
        self._id = value
    @property
    def operator(self) -> str: ...
    @operator.setter
    def operator(self, value: str):
        self._operator = value
    @property
    def value(self) -> object: ...
    @value.setter
    def value(self, value: object):
        self._value = value


class PropertyMetadata(vmodl.DynamicData):
    @property
    def id(self) -> str: ...
    @id.setter
    def id(self, value: str):
        self._id = value
    @property
    def summary(self) -> pbm.ExtendedElementDescription: ...
    @summary.setter
    def summary(self, value: pbm.ExtendedElementDescription):
        self._summary = value
    @property
    def mandatory(self) -> bool: ...
    @mandatory.setter
    def mandatory(self, value: bool):
        self._mandatory = value
    @property
    def type(self) -> TypeInfo: ...
    @type.setter
    def type(self, value: TypeInfo):
        self._type = value
    @property
    def defaultValue(self) -> object: ...
    @defaultValue.setter
    def defaultValue(self, value: object):
        self._defaultValue = value
    @property
    def allowedValue(self) -> object: ...
    @allowedValue.setter
    def allowedValue(self, value: object):
        self._allowedValue = value
    @property
    def requirementsTypeHint(self) -> str: ...
    @requirementsTypeHint.setter
    def requirementsTypeHint(self, value: str):
        self._requirementsTypeHint = value


class TypeInfo(vmodl.DynamicData):
    @property
    def typeName(self) -> str: ...
    @typeName.setter
    def typeName(self, value: str):
        self._typeName = value