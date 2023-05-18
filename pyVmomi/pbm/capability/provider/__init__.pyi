from typing import List
from enum import Enum
from pyVmomi import pbm, vmodl


class CapabilityObjectMetadataPerCategory(vmodl.DynamicData):
    @property
    def subCategory(self) -> str: ...
    @property
    def capabilityMetadata(self) -> List[pbm.capability.CapabilityMetadata]: ...


class CapabilityObjectSchema(vmodl.DynamicData):
    @property
    def vendorInfo(self) -> CapabilityObjectSchema.VendorInfo: ...
    @property
    def namespaceInfo(self) -> CapabilityObjectSchema.NamespaceInfo: ...
    @property
    def lineOfService(self) -> LineOfServiceInfo: ...
    @property
    def capabilityMetadataPerCategory(self) -> List[CapabilityObjectMetadataPerCategory]: ...


    class NamespaceInfo(vmodl.DynamicData):
        @property
        def version(self) -> str: ...
        @property
        def namespace(self) -> str: ...
        @property
        def info(self) -> pbm.ExtendedElementDescription: ...


    class VendorInfo(vmodl.DynamicData):
        @property
        def vendorUuid(self) -> str: ...
        @property
        def info(self) -> pbm.ExtendedElementDescription: ...


    class VendorNamespaceInfo(vmodl.DynamicData):
        @property
        def vendorInfo(self) -> CapabilityObjectSchema.VendorInfo: ...
        @property
        def namespaceInfo(self) -> CapabilityObjectSchema.NamespaceInfo: ...


    class VendorResourceTypeInfo(vmodl.DynamicData):
        @property
        def resourceType(self) -> str: ...
        @property
        def vendorNamespaceInfo(self) -> List[CapabilityObjectSchema.VendorNamespaceInfo]: ...


class LineOfServiceInfo(vmodl.DynamicData):
    @property
    def lineOfService(self) -> str: ...
    @property
    def name(self) -> pbm.ExtendedElementDescription: ...
    @property
    def description(self) -> pbm.ExtendedElementDescription: ...


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


class PersistenceBasedDataServiceInfo(LineOfServiceInfo):
    @property
    def compatiblePersistenceSchemaNamespace(self) -> List[str]: ...


class VaioDataServiceInfo(LineOfServiceInfo): ...