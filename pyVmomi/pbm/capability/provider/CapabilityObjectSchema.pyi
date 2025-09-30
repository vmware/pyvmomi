# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import ClassVar
from typing import Optional

from pyVmomi.VmomiSupport import Enum

from pyVmomi.pbm.ExtendedElementDescription import ExtendedElementDescription

from pyVmomi.vmodl.DynamicData import DynamicData

from pyVmomi.pbm.capability.provider.CapabilityObjectMetadataPerCategory import CapabilityObjectMetadataPerCategory

from pyVmomi.pbm.capability.provider.LineOfServiceInfo import LineOfServiceInfo

class CapabilityObjectSchema(DynamicData):
   class VendorInfo(DynamicData):
      vendorUuid: str
      info: ExtendedElementDescription

   class NamespaceInfo(DynamicData):
      version: str
      namespace: str
      info: Optional[ExtendedElementDescription] = None

   class VendorResourceTypeInfo(DynamicData):
      resourceType: str
      vendorNamespaceInfo: list[VendorNamespaceInfo] = []

   class VendorNamespaceInfo(DynamicData):
      vendorInfo: VendorInfo
      namespaceInfo: NamespaceInfo

   class CapabilityCategory(Enum):
      common: ClassVar['CapabilityCategory'] = 'common'
      datastoreSpecific: ClassVar['CapabilityCategory'] = 'datastoreSpecific'

   vendorInfo: VendorInfo
   namespaceInfo: NamespaceInfo
   lineOfService: Optional[LineOfServiceInfo] = None
   capabilityMetadataPerCategory: list[CapabilityObjectMetadataPerCategory] = []
   capabilityCategory: Optional[str] = None
