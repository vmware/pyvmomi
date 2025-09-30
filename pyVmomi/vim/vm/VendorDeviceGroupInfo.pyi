# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import ClassVar
from typing import Optional

from pyVmomi.VmomiSupport import Enum

from pyVmomi.vmodl.DynamicData import DynamicData

from pyVmomi.vim.vm.TargetInfo import TargetInfo

from pyVmomi.vim.vm.device.VirtualDevice import VirtualDevice

class VendorDeviceGroupInfo(TargetInfo):
   class ComponentDeviceInfo(DynamicData):
      class ComponentType(Enum):
         pciPassthru: ClassVar['ComponentType'] = 'pciPassthru'
         nvidiaVgpu: ClassVar['ComponentType'] = 'nvidiaVgpu'
         sriovNic: ClassVar['ComponentType'] = 'sriovNic'
         dvx: ClassVar['ComponentType'] = 'dvx'

      type: str
      vendorName: str
      deviceName: str
      isConfigurable: bool
      device: VirtualDevice

   deviceGroupName: str
   deviceGroupDescription: Optional[str] = None
   componentDeviceInfo: list[ComponentDeviceInfo] = []
