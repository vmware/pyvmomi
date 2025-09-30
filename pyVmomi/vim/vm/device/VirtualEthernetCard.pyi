# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.VmomiSupport import long

from pyVmomi.vim.Network import Network

from pyVmomi.vim.SharesInfo import SharesInfo

from pyVmomi.vmodl.DynamicData import DynamicData

from pyVmomi.vim.dvs.PortConnection import PortConnection

from pyVmomi.vim.vm.device.VirtualDevice import VirtualDevice

class VirtualEthernetCard(VirtualDevice):
   class NetworkBackingInfo(VirtualDevice.DeviceBackingInfo):
      network: Optional[Network] = None
      inPassthroughMode: Optional[bool] = None

   class LegacyNetworkBackingInfo(VirtualDevice.DeviceBackingInfo):
      pass

   class DistributedVirtualPortBackingInfo(VirtualDevice.BackingInfo):
      port: PortConnection

   class OpaqueNetworkBackingInfo(VirtualDevice.BackingInfo):
      opaqueNetworkId: str
      opaqueNetworkType: str

   class ResourceAllocation(DynamicData):
      reservation: Optional[long] = None
      share: SharesInfo
      limit: Optional[long] = None

   addressType: Optional[str] = None
   macAddress: Optional[str] = None
   wakeOnLanEnabled: Optional[bool] = None
   resourceAllocation: Optional[ResourceAllocation] = None
   externalId: Optional[str] = None
   uptCompatibilityEnabled: Optional[bool] = None
   subnetId: Optional[str] = None
