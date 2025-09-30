# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import ClassVar
from typing import Optional

from pyVmomi.VmomiSupport import Enum
from pyVmomi.VmomiSupport import ManagedObject
from pyVmomi.VmomiSupport import long

from pyVmomi.vim.Datastore import Datastore

from pyVmomi.vim.HostSystem import HostSystem

from pyVmomi.vim.ImportSpec import ImportSpec

from pyVmomi.vim.KeyValue import KeyValue

from pyVmomi.vim.ManagedEntity import ManagedEntity

from pyVmomi.vim.Network import Network

from pyVmomi.vim.OvfConsumer import OvfConsumer

from pyVmomi.vim.ResourceConfigSpec import ResourceConfigSpec

from pyVmomi.vim.ResourcePool import ResourcePool

from pyVmomi.vmodl.DynamicData import DynamicData

from pyVmomi.vmodl.LocalizableMessage import LocalizableMessage

from pyVmomi.vmodl.MethodFault import MethodFault

from pyVmomi.vim.vApp.ProductInfo import ProductInfo

from pyVmomi.vim.vApp.PropertyInfo import PropertyInfo

from pyVmomi.vim.vm.Snapshot import Snapshot

class OvfManager(ManagedObject):
   class OvfOptionInfo(DynamicData):
      option: str
      description: LocalizableMessage

   class DeploymentOption(DynamicData):
      key: str
      label: str
      description: str

   class CommonParams(DynamicData):
      locale: str
      deploymentOption: str
      msgBundle: list[KeyValue] = []
      importOption: list[str] = []

   class ValidateHostParams(CommonParams):
      pass

   class ValidateHostResult(DynamicData):
      downloadSize: Optional[long] = None
      flatDeploymentSize: Optional[long] = None
      sparseDeploymentSize: Optional[long] = None
      error: list[MethodFault] = []
      warning: list[MethodFault] = []
      supportedDiskProvisioning: list[str] = []

   class ParseDescriptorParams(CommonParams):
      pass

   class ParseDescriptorResult(DynamicData):
      eula: list[str] = []
      network: list[NetworkInfo] = []
      ipAllocationScheme: list[str] = []
      ipProtocols: list[str] = []
      property: list[PropertyInfo] = []
      productInfo: Optional[ProductInfo] = None
      annotation: str
      approximateDownloadSize: Optional[long] = None
      approximateFlatDeploymentSize: Optional[long] = None
      approximateSparseDeploymentSize: Optional[long] = None
      defaultEntityName: str
      virtualApp: bool
      deploymentOption: list[DeploymentOption] = []
      defaultDeploymentOption: str
      entityName: list[KeyValue] = []
      annotatedOst: Optional[OvfConsumer.OstNode] = None
      error: list[MethodFault] = []
      warning: list[MethodFault] = []

   class NetworkInfo(DynamicData):
      name: str
      description: str

   class CreateImportSpecParams(CommonParams):
      class DiskProvisioningType(Enum):
         monolithicSparse: ClassVar['DiskProvisioningType'] = 'monolithicSparse'
         monolithicFlat: ClassVar['DiskProvisioningType'] = 'monolithicFlat'
         twoGbMaxExtentSparse: ClassVar['DiskProvisioningType'] = 'twoGbMaxExtentSparse'
         twoGbMaxExtentFlat: ClassVar['DiskProvisioningType'] = 'twoGbMaxExtentFlat'
         thin: ClassVar['DiskProvisioningType'] = 'thin'
         thick: ClassVar['DiskProvisioningType'] = 'thick'
         seSparse: ClassVar['DiskProvisioningType'] = 'seSparse'
         eagerZeroedThick: ClassVar['DiskProvisioningType'] = 'eagerZeroedThick'
         sparse: ClassVar['DiskProvisioningType'] = 'sparse'
         flat: ClassVar['DiskProvisioningType'] = 'flat'

      entityName: str
      hostSystem: Optional[HostSystem] = None
      networkMapping: list[NetworkMapping] = []
      ipAllocationPolicy: Optional[str] = None
      ipProtocol: Optional[str] = None
      propertyMapping: list[KeyValue] = []
      resourceMapping: list[ResourceMap] = []
      diskProvisioning: Optional[str] = None
      instantiationOst: Optional[OvfConsumer.OstNode] = None

   class ResourceMap(DynamicData):
      source: str
      parent: Optional[ResourcePool] = None
      resourceSpec: Optional[ResourceConfigSpec] = None
      datastore: Optional[Datastore] = None

   class NetworkMapping(DynamicData):
      name: str
      network: Network

   class DatastoreMapping(DynamicData):
      diskId: str
      datastore: Datastore

   class StorageProfileMapping(DynamicData):
      diskId: str
      storageProfileId: str

   class CreateImportSpecResult(DynamicData):
      importSpec: Optional[ImportSpec] = None
      fileItem: list[FileItem] = []
      warning: list[MethodFault] = []
      error: list[MethodFault] = []

   class FileItem(DynamicData):
      deviceId: str
      path: str
      compressionMethod: Optional[str] = None
      chunkSize: Optional[long] = None
      size: Optional[long] = None
      cimType: int
      create: bool

   class CreateDescriptorParams(DynamicData):
      ovfFiles: list[OvfFile] = []
      name: Optional[str] = None
      description: Optional[str] = None
      includeImageFiles: Optional[bool] = None
      exportOption: list[str] = []
      snapshot: Optional[Snapshot] = None

   class CreateDescriptorResult(DynamicData):
      ovfDescriptor: str
      error: list[MethodFault] = []
      warning: list[MethodFault] = []
      includeImageFiles: Optional[bool] = None

   class OvfFile(DynamicData):
      deviceId: str
      path: str
      compressionMethod: Optional[str] = None
      chunkSize: Optional[long] = None
      size: long
      capacity: Optional[long] = None
      populatedSize: Optional[long] = None

   class OvfImportParams(CreateImportSpecParams):
      pushMode: Optional[bool] = None
      signatureRequired: Optional[bool] = None
      skipManifestCheck: Optional[bool] = None
      powerOn: Optional[bool] = None
      customHttpHeaders: list[KeyValue] = []
      sourceCertificate: Optional[str] = None
      datastoreMappings: list[DatastoreMapping] = []
      vmProfile: Optional[str] = None
      diskProfiles: list[StorageProfileMapping] = []

   @property
   def ovfImportOption(self) -> list[OvfOptionInfo]: ...
   @property
   def ovfExportOption(self) -> list[OvfOptionInfo]: ...

   def ValidateHost(self, ovfDescriptor: str, host: HostSystem, vhp: ValidateHostParams) -> ValidateHostResult: ...
   def ParseDescriptor(self, ovfDescriptor: str, pdp: ParseDescriptorParams) -> ParseDescriptorResult: ...
   def CreateImportSpec(self, ovfDescriptor: str, resourcePool: ResourcePool, datastore: Datastore, cisp: CreateImportSpecParams) -> CreateImportSpecResult: ...
   def CreateDescriptor(self, obj: ManagedEntity, cdp: CreateDescriptorParams) -> CreateDescriptorResult: ...
