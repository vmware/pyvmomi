# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.VmomiSupport import PropertyPath

from pyVmomi.vim import ResourceConfigOption

from pyVmomi.vmodl import DynamicData

from pyVmomi.vim.option import BoolOption
from pyVmomi.vim.option import IntOption
from pyVmomi.vim.option import LongOption

from pyVmomi.vim.vm.device import VirtualDeviceOption

class VirtualHardwareOption(DynamicData):
   hwVersion: int
   virtualDeviceOption: list[VirtualDeviceOption] = []
   deviceListReadonly: bool
   numCPU: list[int] = []
   numCoresPerSocket: IntOption
   autoCoresPerSocket: Optional[BoolOption] = None
   numCpuReadonly: bool
   memoryMB: LongOption
   numPCIControllers: IntOption
   numIDEControllers: IntOption
   numUSBControllers: IntOption
   numUSBXHCIControllers: IntOption
   numSIOControllers: IntOption
   numPS2Controllers: IntOption
   licensingLimit: list[PropertyPath] = []
   numSupportedWwnPorts: Optional[IntOption] = None
   numSupportedWwnNodes: Optional[IntOption] = None
   resourceConfigOption: ResourceConfigOption
   numNVDIMMControllers: Optional[IntOption] = None
   numTPMDevices: Optional[IntOption] = None
   numWDTDevices: Optional[IntOption] = None
   numPrecisionClockDevices: Optional[IntOption] = None
   epcMemoryMB: Optional[LongOption] = None
   acpiHostBridgesFirmware: list[str] = []
   numCpuSimultaneousThreads: Optional[IntOption] = None
   numNumaNodes: Optional[IntOption] = None
   numDeviceGroups: Optional[IntOption] = None
   deviceGroupTypes: list[type] = []
