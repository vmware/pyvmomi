# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vim.vm.device.VirtualDevice import VirtualDevice

from pyVmomi.vim.vm.device.VirtualEthernetCard import VirtualEthernetCard

from pyVmomi.vim.vm.device.VirtualPCIPassthrough import VirtualPCIPassthrough

class VirtualSriovEthernetCard(VirtualEthernetCard):
   class SriovBackingInfo(VirtualDevice.BackingInfo):
      physicalFunctionBacking: Optional[VirtualPCIPassthrough.DeviceBackingInfo] = None
      virtualFunctionBacking: Optional[VirtualPCIPassthrough.DeviceBackingInfo] = None
      virtualFunctionIndex: Optional[int] = None

   allowGuestOSMtuChange: Optional[bool] = None
   sriovBacking: Optional[SriovBackingInfo] = None
   dvxBackingInfo: Optional[VirtualPCIPassthrough.DvxBackingInfo] = None
