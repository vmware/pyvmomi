# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.VmomiSupport import short

from pyVmomi.vmodl import DynamicData

from pyVmomi.vim.option import OptionValue

from pyVmomi.vim.vm.device import VirtualDevice

class VirtualPCIPassthrough(VirtualDevice):
   class DeviceBackingInfo(VirtualDevice.DeviceBackingInfo):
      id: str
      deviceId: str
      systemId: str
      vendorId: short

   class AllowedDevice(DynamicData):
      vendorId: int
      deviceId: int
      subVendorId: Optional[int] = None
      subDeviceId: Optional[int] = None
      revisionId: Optional[short] = None

   class DynamicBackingInfo(VirtualDevice.DeviceBackingInfo):
      allowedDevice: list[AllowedDevice] = []
      customLabel: Optional[str] = None
      assignedId: Optional[str] = None

   class PluginBackingInfo(VirtualDevice.BackingInfo):
      pass

   class VmiopBackingInfo(PluginBackingInfo):
      vgpu: Optional[str] = None
      vgpuMigrateDataSizeMB: Optional[int] = None
      migrateSupported: Optional[bool] = None
      enhancedMigrateCapability: Optional[bool] = None

   class DvxBackingInfo(VirtualDevice.BackingInfo):
      deviceClass: Optional[str] = None
      configParams: list[OptionValue] = []
