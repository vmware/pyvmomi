# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.VmomiSupport import long

from pyVmomi.vim import KeyValue

from pyVmomi.vmodl import DynamicData
from pyVmomi.vmodl import MethodFault

from pyVmomi.vim.host import VsanHclDiskInfo
from pyVmomi.vim.host import VsanHostCimProviderInfo
from pyVmomi.vim.host import VsanVcgDeviceInfo

from pyVmomi.vim.vsan import VsanHclDriverInfo

class VsanHclControllerInfo(DynamicData):
   deviceName: str
   deviceDisplayName: Optional[str] = None
   driverName: Optional[str] = None
   driverVersion: Optional[str] = None
   vendorId: Optional[long] = None
   deviceId: Optional[long] = None
   subVendorId: Optional[long] = None
   subDeviceId: Optional[long] = None
   extraInfo: list[KeyValue] = []
   deviceOnHcl: Optional[bool] = None
   releaseSupported: Optional[bool] = None
   releasesOnHcl: list[str] = []
   driverVersionsOnHcl: list[str] = []
   driverVersionSupported: Optional[bool] = None
   fwVersionSupported: Optional[bool] = None
   fwVersionOnHcl: list[str] = []
   cacheConfigSupported: Optional[bool] = None
   cacheConfigOnHcl: list[str] = []
   raidConfigSupported: Optional[bool] = None
   raidConfigOnHcl: list[str] = []
   fwVersion: Optional[str] = None
   raidConfig: Optional[str] = None
   cacheConfig: Optional[str] = None
   cimProviderInfo: Optional[VsanHostCimProviderInfo] = None
   usedByVsan: Optional[bool] = None
   disks: list[VsanHclDiskInfo] = []
   issues: list[MethodFault] = []
   remediableIssues: list[str] = []
   driversOnHcl: list[VsanHclDriverInfo] = []
   fwAuxVersion: Optional[str] = None
   queueDepth: Optional[long] = None
   queueDepthOnHcl: Optional[long] = None
   queueDepthSupported: Optional[bool] = None
   diskMode: Optional[str] = None
   diskModeOnHcl: list[str] = []
   diskModeSupported: Optional[bool] = None
   toolName: Optional[str] = None
   toolVersion: Optional[str] = None
   productId: Optional[str] = None
   diskCapacity: Optional[long] = None
   vcgEntryInfo: list[VsanVcgDeviceInfo] = []
   controllerType: Optional[str] = None
   userSelectedVcgId: Optional[int] = None
   vsanCompatibility: list[str] = []
