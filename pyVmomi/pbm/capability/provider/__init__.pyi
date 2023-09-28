from typing import List
from enum import Enum
from pyVmomi import pbm, vmodl


class CapabilityObjectMetadataPerCategory(vmodl.DynamicData):
    @property
    def subCategory(self) -> str: ...
    @subCategory.setter
    def subCategory(self, value: str):
        self._subCategory = value
    @property
    def capabilityMetadata(self) -> List[pbm.capability.CapabilityMetadata]: ...
    @capabilityMetadata.setter
    def capabilityMetadata(self, value: List[pbm.capability.CapabilityMetadata]):
        self._capabilityMetadata = value


class CapabilityObjectSchema(vmodl.DynamicData):
    @property
    def vendorInfo(self) -> CapabilityObjectSchema.VendorInfo: ...
    @vendorInfo.setter
    def vendorInfo(self, value: CapabilityObjectSchema.VendorInfo):
        self._vendorInfo = value
    @property
    def namespaceInfo(self) -> CapabilityObjectSchema.NamespaceInfo: ...
    @namespaceInfo.setter
    def namespaceInfo(self, value: CapabilityObjectSchema.NamespaceInfo):
        self._namespaceInfo = value
    @property
    def lineOfService(self) -> LineOfServiceInfo: ...
    @lineOfService.setter
    def lineOfService(self, value: LineOfServiceInfo):
        self._lineOfService = value
    @property
    def capabilityMetadataPerCategory(self) -> List[CapabilityObjectMetadataPerCategory]: ...
    @capabilityMetadataPerCategory.setter
    def capabilityMetadataPerCategory(self, value: List[CapabilityObjectMetadataPerCategory]):
        self._capabilityMetadataPerCategory = value


    class NamespaceInfo(vmodl.DynamicData):
        @property
        def version(self) -> str: ...
        @version.setter
        def version(self, value: str):
            self._version = value
        @property
        def namespace(self) -> str: ...
        @namespace.setter
        def namespace(self, value: str):
            self._namespace = value
        @property
        def info(self) -> pbm.ExtendedElementDescription: ...
        @info.setter
        def info(self, value: pbm.ExtendedElementDescription):
            self._info = value


    class VendorInfo(vmodl.DynamicData):
        @property
        def vendorUuid(self) -> str: ...
        @vendorUuid.setter
        def vendorUuid(self, value: str):
            self._vendorUuid = value
        @property
        def info(self) -> pbm.ExtendedElementDescription: ...
        @info.setter
        def info(self, value: pbm.ExtendedElementDescription):
            self._info = value


    class VendorNamespaceInfo(vmodl.DynamicData):
        @property
        def vendorInfo(self) -> CapabilityObjectSchema.VendorInfo: ...
        @vendorInfo.setter
        def vendorInfo(self, value: CapabilityObjectSchema.VendorInfo):
            self._vendorInfo = value
        @property
        def namespaceInfo(self) -> CapabilityObjectSchema.NamespaceInfo: ...
        @namespaceInfo.setter
        def namespaceInfo(self, value: CapabilityObjectSchema.NamespaceInfo):
            self._namespaceInfo = value


    class VendorResourceTypeInfo(vmodl.DynamicData):
        @property
        def resourceType(self) -> str: ...
        @resourceType.setter
        def resourceType(self, value: str):
            self._resourceType = value
        @property
        def vendorNamespaceInfo(self) -> List[CapabilityObjectSchema.VendorNamespaceInfo]: ...
        @vendorNamespaceInfo.setter
        def vendorNamespaceInfo(self, value: List[CapabilityObjectSchema.VendorNamespaceInfo]):
            self._vendorNamespaceInfo = value


class LineOfServiceInfo(vmodl.DynamicData):
    @property
    def lineOfService(self) -> str: ...
    @lineOfService.setter
    def lineOfService(self, value: str):
        self._lineOfService = value
    @property
    def name(self) -> pbm.ExtendedElementDescription: ...
    @name.setter
    def name(self, value: pbm.ExtendedElementDescription):
        self._name = value
    @property
    def description(self) -> pbm.ExtendedElementDescription: ...
    @description.setter
    def description(self, value: pbm.ExtendedElementDescription):
        self._description = value


    class LineOfServiceEnum(Enum):
        INSPECTION = "INSPECTION"
        COMPRESSION = "COMPRESSION"
        ENCRYPTION = "ENCRYPTION"
        REPLICATION = "REPLICATION"
        CACHING = "CACHING"
        PERSISTENCE = "PERSISTENCE"
        DATA_PROVIDER = "DATA_PROVIDER"
        DATASTORE_IO_CONTROL = "DATASTORE_IO_CONTROL"
        DATA_PROTECTION = "DATA_PROTECTION"
        STRETCHED_CLUSTER = "STRETCHED_CLUSTER"


class PersistenceBasedDataServiceInfo(LineOfServiceInfo):
    @property
    def compatiblePersistenceSchemaNamespace(self) -> List[str]: ...
    @compatiblePersistenceSchemaNamespace.setter
    def compatiblePersistenceSchemaNamespace(self, value: List[str]):
        self._compatiblePersistenceSchemaNamespace = value


class VaioDataServiceInfo(LineOfServiceInfo): ...