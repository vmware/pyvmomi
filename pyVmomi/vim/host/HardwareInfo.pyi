# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.VmomiSupport import long

from pyVmomi.vmodl import DynamicData

from pyVmomi.vim.host import BIOSInfo
from pyVmomi.vim.host import CpuIdInfo
from pyVmomi.vim.host import CpuInfo
from pyVmomi.vim.host import CpuPackage
from pyVmomi.vim.host import CpuPowerManagementInfo
from pyVmomi.vim.host import DvxClass
from pyVmomi.vim.host import MemoryTierInfo
from pyVmomi.vim.host import NumaInfo
from pyVmomi.vim.host import PciDevice
from pyVmomi.vim.host import PersistentMemoryInfo
from pyVmomi.vim.host import ReliableMemoryInfo
from pyVmomi.vim.host import SevInfo
from pyVmomi.vim.host import SgxInfo
from pyVmomi.vim.host import SystemInfo

class HardwareInfo(DynamicData):
   systemInfo: SystemInfo
   cpuPowerManagementInfo: Optional[CpuPowerManagementInfo] = None
   cpuInfo: CpuInfo
   cpuPkg: list[CpuPackage] = []
   memorySize: long
   numaInfo: Optional[NumaInfo] = None
   smcPresent: bool
   pciDevice: list[PciDevice] = []
   dvxClasses: list[DvxClass] = []
   cpuFeature: list[CpuIdInfo] = []
   biosInfo: Optional[BIOSInfo] = None
   reliableMemoryInfo: Optional[ReliableMemoryInfo] = None
   persistentMemoryInfo: Optional[PersistentMemoryInfo] = None
   sgxInfo: Optional[SgxInfo] = None
   sevInfo: Optional[SevInfo] = None
   memoryTieringType: Optional[str] = None
   memoryTierInfo: list[MemoryTierInfo] = []
