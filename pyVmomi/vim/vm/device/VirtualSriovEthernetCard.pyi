# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vim.vm.device import VirtualDevice
from pyVmomi.vim.vm.device import VirtualEthernetCard
from pyVmomi.vim.vm.device import VirtualPCIPassthrough

class VirtualSriovEthernetCard(VirtualEthernetCard):
   class SriovBackingInfo(VirtualDevice.BackingInfo):
      physicalFunctionBacking: Optional[VirtualPCIPassthrough.DeviceBackingInfo] = None
      virtualFunctionBacking: Optional[VirtualPCIPassthrough.DeviceBackingInfo] = None
      virtualFunctionIndex: Optional[int] = None

   allowGuestOSMtuChange: Optional[bool] = None
   sriovBacking: Optional[SriovBackingInfo] = None
   dvxBackingInfo: Optional[VirtualPCIPassthrough.DvxBackingInfo] = None
