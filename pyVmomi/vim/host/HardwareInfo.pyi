# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.VmomiSupport import long

from pyVmomi.vmodl.DynamicData import DynamicData

from pyVmomi.vim.host.BIOSInfo import BIOSInfo

from pyVmomi.vim.host.CpuIdInfo import CpuIdInfo

from pyVmomi.vim.host.CpuInfo import CpuInfo

from pyVmomi.vim.host.CpuPackage import CpuPackage

from pyVmomi.vim.host.CpuPowerManagementInfo import CpuPowerManagementInfo

from pyVmomi.vim.host.DvxClass import DvxClass

from pyVmomi.vim.host.MemoryTierInfo import MemoryTierInfo

from pyVmomi.vim.host.NumaInfo import NumaInfo

from pyVmomi.vim.host.PciDevice import PciDevice

from pyVmomi.vim.host.PersistentMemoryInfo import PersistentMemoryInfo

from pyVmomi.vim.host.ReliableMemoryInfo import ReliableMemoryInfo

from pyVmomi.vim.host.SevInfo import SevInfo

from pyVmomi.vim.host.SgxInfo import SgxInfo

from pyVmomi.vim.host.SystemInfo import SystemInfo

from pyVmomi.vim.host.TdxInfo import TdxInfo

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
   tdxInfo: Optional[TdxInfo] = None
