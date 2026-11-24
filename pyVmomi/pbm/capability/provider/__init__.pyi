# Copyright (c) 2006-2026 Broadcom. All Rights Reserved.
# The term "Broadcom" refers to Broadcom Inc. and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

import typing as _typing
import pyVmomi.VmomiSupport
import pyVmomi.pbm
import pyVmomi.vmodl
import pyVmomi.pbm.capability



class CapabilityObjectMetadataPerCategory(pyVmomi.vmodl.DynamicData):
   """
   The `pyVmomi.pbm.capability.provider.CapabilityObjectMetadataPerCategory`
   data object defines capability metadata for a profile subcategory.
   
   Attributes:
       subCategory: Profile subcategory to which the capability metadata belongs.
           
           The subcategory is specified by the storage provider.
       capabilityMetadata: Capability metadata for this category
   """
   subCategory: str
   capabilityMetadata: list[pyVmomi.pbm.capability.CapabilityMetadata] = []


class CapabilityObjectSchema(pyVmomi.vmodl.DynamicData):
   """
   Capability Schema information
   
   Attributes:
       lineOfService: Service type for the schema.
           
           Do not use Category as each service needs to have its own schema version.
           
           If omitted, this schema specifies persistence capabilities.
       capabilityMetadataPerCategory: Capability metadata organized by category
       capabilityCategory: The category of the capabilities in this schema.
           
           See `pyVmomi.pbm.capability.provider.CapabilityObjectSchema.CapabilityCategory` for the list of supported types.
           If omitted this specifies `datastoreSpecific`
           unless the `pyVmomi.pbm.capability.provider.CapabilityObjectSchema.lineOfService` is of type `pyVmomi.pbm.capability.provider.VaioDataServiceInfo`.
           If `pyVmomi.pbm.capability.provider.CapabilityObjectSchema.lineOfService` is of type `pyVmomi.pbm.capability.provider.VaioDataServiceInfo`
           then this schema is of `common` type.
   """
   class VendorInfo(pyVmomi.vmodl.DynamicData):
      """
      Information about vendor/owner of the capability metadata schema
      
      Attributes:
          vendorUuid: Unique identifier for the vendor who owns the given capability
              schema definition
          info: Captures name and description information about the vendor/owner of
              the schema.
              - The `summary.label` property
                (`pyVmomi.pbm.ExtendedElementDescription.label`)
                contains vendor name information in server locale.
              - The `summary.summary` property
                (`pyVmomi.pbm.ExtendedElementDescription.summary`)
                contains vendor description string in server locale.
              - The `summary.messageCatalogKeyPrefix` property
                (`pyVmomi.pbm.ExtendedElementDescription.messageCatalogKeyPrefix`)
                contains unique prefix for the vendor information within given message
                catalog.
      """
      vendorUuid: str
      info: pyVmomi.pbm.ExtendedElementDescription

   class NamespaceInfo(pyVmomi.vmodl.DynamicData):
      """
      Name space information for the capability metadata schema.
      
      NOTE: Name spaces are required to be globally unique across resource types.
      A same vendor can register multiple name spaces for same resource type or
      for different resource type, but the schema namespace URL must be unique
      for each of these cases.
      A CapabilityMetadata object is uniquely identified based on the namespace
      it belongs to and it's unique identifier within that namespace.
      
      Attributes:
          version: Schema version
          namespace: Schema namespace.
      """
      version: str
      namespace: str
      info: _typing.Optional[pyVmomi.pbm.ExtendedElementDescription] = None

   class VendorResourceTypeInfo(pyVmomi.vmodl.DynamicData):
      """
      Attributes:
          resourceType: Resource type for which given vendor has registered given namespace
              along with capability metadata that belongs to the namespace.
              
              Must match one of the values for enum `pyVmomi.pbm.profile.ResourceTypeEnum`
          vendorNamespaceInfo: List of all vendorInfo <--> namespaceInfo tuples that are registered for
              given resource type
      """
      resourceType: str
      vendorNamespaceInfo: list[CapabilityObjectSchema.VendorNamespaceInfo] = []

   class VendorNamespaceInfo(pyVmomi.vmodl.DynamicData):
      vendorInfo: CapabilityObjectSchema.VendorInfo
      namespaceInfo: CapabilityObjectSchema.NamespaceInfo

   class CapabilityCategory(pyVmomi.VmomiSupport.Enum):
      """
      Capability category type constants.
      
      Attributes:
          common: Common and identical in all sub-profiles.
          datastoreSpecific: Part of a single sub-profile.
      """
      common: _typing.ClassVar['CapabilityObjectSchema.CapabilityCategory'] = 'common'
      datastoreSpecific: _typing.ClassVar['CapabilityObjectSchema.CapabilityCategory'] = 'datastoreSpecific'

   vendorInfo: CapabilityObjectSchema.VendorInfo
   namespaceInfo: CapabilityObjectSchema.NamespaceInfo
   lineOfService: _typing.Optional[LineOfServiceInfo] = None
   capabilityMetadataPerCategory: list[CapabilityObjectMetadataPerCategory] = []
   capabilityCategory: _typing.Optional[str] = None


class LineOfServiceInfo(pyVmomi.vmodl.DynamicData):
   """
   Describes Line of Service of a capability provider.
   
   Attributes:
       lineOfService: `pyVmomi.pbm.capability.provider.LineOfServiceInfo.LineOfServiceEnum` - must be one of the values
           for enum `pyVmomi.pbm.capability.provider.LineOfServiceInfo.LineOfServiceEnum`.
       name: Name of the service - for informational
           purposes only.
       description: Description of the service - for informational
           purposes only.
   """
   class LineOfServiceEnum(pyVmomi.VmomiSupport.Enum):
      """Denotes the line of service of a schema."""
      INSPECTION: _typing.ClassVar['LineOfServiceInfo.LineOfServiceEnum'] = 'INSPECTION'
      COMPRESSION: _typing.ClassVar['LineOfServiceInfo.LineOfServiceEnum'] = 'COMPRESSION'
      ENCRYPTION: _typing.ClassVar['LineOfServiceInfo.LineOfServiceEnum'] = 'ENCRYPTION'
      REPLICATION: _typing.ClassVar['LineOfServiceInfo.LineOfServiceEnum'] = 'REPLICATION'
      CACHING: _typing.ClassVar['LineOfServiceInfo.LineOfServiceEnum'] = 'CACHING'
      PERSISTENCE: _typing.ClassVar['LineOfServiceInfo.LineOfServiceEnum'] = 'PERSISTENCE'
      DATA_PROVIDER: _typing.ClassVar['LineOfServiceInfo.LineOfServiceEnum'] = 'DATA_PROVIDER'
      DATASTORE_IO_CONTROL: _typing.ClassVar['LineOfServiceInfo.LineOfServiceEnum'] = 'DATASTORE_IO_CONTROL'
      DATA_PROTECTION: _typing.ClassVar['LineOfServiceInfo.LineOfServiceEnum'] = 'DATA_PROTECTION'
      STRETCHED_CLUSTER: _typing.ClassVar['LineOfServiceInfo.LineOfServiceEnum'] = 'STRETCHED_CLUSTER'

   lineOfService: str
   name: pyVmomi.pbm.ExtendedElementDescription
   description: _typing.Optional[pyVmomi.pbm.ExtendedElementDescription] = None


class PersistenceBasedDataServiceInfo(LineOfServiceInfo):
   """
   Describes the data services provided by the storage arrays.
   
   In addition to storing bits, some VASA providers may also want to separate
   their capabilities into lines of service to let vSphere manage finer grain
   policies. For example an array may support replication natively, and may
   want vSphere policies to be defined for the replication aspect separately
   and compose them with persistence related policies.
   
   Attributes:
       compatiblePersistenceSchemaNamespace: This property should be set with compatible schema namespaces exposed by
           the vendor provider.
           
           If not specified, vSphere assumes all Data Service
           provider schemas are compatible with all persistence provider namespaces
           advertised by the VASA provider.
   """
   compatiblePersistenceSchemaNamespace: list[str] = []

class VaioDataServiceInfo(LineOfServiceInfo):
   """
   Information about a supported data service provided using
   vSphere APIs for IO Filtering (VAIO) data service provider.
   """
   pass
