# Copyright (c) 2006-2026 Broadcom. All Rights Reserved.
# The term "Broadcom" refers to Broadcom Inc. and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

import typing as _typing
import pyVmomi.VmomiSupport
import pyVmomi.pbm
import pyVmomi.vmodl
import pyVmomi.pbm.capability



class CapabilityObjectMetadataPerCategory(pyVmomi.vmodl.DynamicData):
   subCategory: str
   capabilityMetadata: list[pyVmomi.pbm.capability.CapabilityMetadata] = []


class CapabilityObjectSchema(pyVmomi.vmodl.DynamicData):
   class VendorInfo(pyVmomi.vmodl.DynamicData):
      vendorUuid: str
      info: pyVmomi.pbm.ExtendedElementDescription

   class NamespaceInfo(pyVmomi.vmodl.DynamicData):
      version: str
      namespace: str
      info: _typing.Optional[pyVmomi.pbm.ExtendedElementDescription] = None

   class VendorResourceTypeInfo(pyVmomi.vmodl.DynamicData):
      resourceType: str
      vendorNamespaceInfo: list[VendorNamespaceInfo] = []

   class VendorNamespaceInfo(pyVmomi.vmodl.DynamicData):
      vendorInfo: VendorInfo
      namespaceInfo: NamespaceInfo

   class CapabilityCategory(pyVmomi.VmomiSupport.Enum):
      common: _typing.ClassVar['CapabilityCategory'] = 'common'
      datastoreSpecific: _typing.ClassVar['CapabilityCategory'] = 'datastoreSpecific'

   vendorInfo: VendorInfo
   namespaceInfo: NamespaceInfo
   lineOfService: _typing.Optional[LineOfServiceInfo] = None
   capabilityMetadataPerCategory: list[CapabilityObjectMetadataPerCategory] = []
   capabilityCategory: _typing.Optional[str] = None


class LineOfServiceInfo(pyVmomi.vmodl.DynamicData):
   class LineOfServiceEnum(pyVmomi.VmomiSupport.Enum):
      INSPECTION: _typing.ClassVar['LineOfServiceEnum'] = 'INSPECTION'
      COMPRESSION: _typing.ClassVar['LineOfServiceEnum'] = 'COMPRESSION'
      ENCRYPTION: _typing.ClassVar['LineOfServiceEnum'] = 'ENCRYPTION'
      REPLICATION: _typing.ClassVar['LineOfServiceEnum'] = 'REPLICATION'
      CACHING: _typing.ClassVar['LineOfServiceEnum'] = 'CACHING'
      PERSISTENCE: _typing.ClassVar['LineOfServiceEnum'] = 'PERSISTENCE'
      DATA_PROVIDER: _typing.ClassVar['LineOfServiceEnum'] = 'DATA_PROVIDER'
      DATASTORE_IO_CONTROL: _typing.ClassVar['LineOfServiceEnum'] = 'DATASTORE_IO_CONTROL'
      DATA_PROTECTION: _typing.ClassVar['LineOfServiceEnum'] = 'DATA_PROTECTION'
      STRETCHED_CLUSTER: _typing.ClassVar['LineOfServiceEnum'] = 'STRETCHED_CLUSTER'

   lineOfService: str
   name: pyVmomi.pbm.ExtendedElementDescription
   description: _typing.Optional[pyVmomi.pbm.ExtendedElementDescription] = None


class PersistenceBasedDataServiceInfo(LineOfServiceInfo):
   compatiblePersistenceSchemaNamespace: list[str] = []

class VaioDataServiceInfo(LineOfServiceInfo):
   pass
