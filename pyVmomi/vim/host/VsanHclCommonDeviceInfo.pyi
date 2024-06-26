# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.VmomiSupport import long

from pyVmomi.vim import KeyValue

from pyVmomi.vmodl import DynamicData

from pyVmomi.vim.vsan import VsanHclDriverInfo

class VsanHclCommonDeviceInfo(DynamicData):
   deviceName: str
   displayName: Optional[str] = None
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
   fwVersion: Optional[str] = None
   driversOnHcl: list[VsanHclDriverInfo] = []
