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
        INSPECTION = "inspection"
        COMPRESSION = "compression"
        ENCRYPTION = "encryption"
        REPLICATION = "replication"
        CACHING = "caching"
        PERSISTENCE = "persistence"
        DATA_PROVIDER = "data_provider"
        DATASTORE_IO_CONTROL = "datastore_io_control"
        DATA_PROTECTION = "data_protection"


class PersistenceBasedDataServiceInfo(LineOfServiceInfo):
    @property
    def compatiblePersistenceSchemaNamespace(self) -> List[str]: ...


class VaioDataServiceInfo(LineOfServiceInfo): ...