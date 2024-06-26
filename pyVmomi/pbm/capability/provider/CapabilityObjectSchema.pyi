# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.pbm import ExtendedElementDescription

from pyVmomi.vmodl import DynamicData

from pyVmomi.pbm.capability.provider import CapabilityObjectMetadataPerCategory
from pyVmomi.pbm.capability.provider import LineOfServiceInfo

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

   vendorInfo: VendorInfo
   namespaceInfo: NamespaceInfo
   lineOfService: Optional[LineOfServiceInfo] = None
   capabilityMetadataPerCategory: list[CapabilityObjectMetadataPerCategory] = []
