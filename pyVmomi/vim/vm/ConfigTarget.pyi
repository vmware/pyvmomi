# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.VmomiSupport import long

from pyVmomi.vim import ResourcePool

from pyVmomi.vmodl import DynamicData

from pyVmomi.vim.dvs import DistributedVirtualPortgroupInfo
from pyVmomi.vim.dvs import DistributedVirtualSwitchInfo

from pyVmomi.vim.vm import CdromInfo
from pyVmomi.vim.vm import DatastoreInfo
from pyVmomi.vim.vm import DvxClassInfo
from pyVmomi.vim.vm import DynamicPassthroughInfo
from pyVmomi.vim.vm import FloppyInfo
from pyVmomi.vim.vm import IdeDiskDeviceInfo
from pyVmomi.vim.vm import LegacyNetworkSwitchInfo
from pyVmomi.vim.vm import NetworkInfo
from pyVmomi.vim.vm import OpaqueNetworkInfo
from pyVmomi.vim.vm import ParallelInfo
from pyVmomi.vim.vm import PciPassthroughInfo
from pyVmomi.vim.vm import PciSharedGpuPassthroughInfo
from pyVmomi.vim.vm import PrecisionClockInfo
from pyVmomi.vim.vm import ScsiDiskDeviceInfo
from pyVmomi.vim.vm import ScsiPassthroughInfo
from pyVmomi.vim.vm import SerialInfo
from pyVmomi.vim.vm import SgxTargetInfo
from pyVmomi.vim.vm import SoundInfo
from pyVmomi.vim.vm import SriovInfo
from pyVmomi.vim.vm import UsbInfo
from pyVmomi.vim.vm import VFlashModuleInfo
from pyVmomi.vim.vm import VendorDeviceGroupInfo
from pyVmomi.vim.vm import VgpuDeviceInfo
from pyVmomi.vim.vm import VgpuProfileInfo

class ConfigTarget(DynamicData):
   numCpus: int
   numCpuCores: int
   numNumaNodes: int
   maxCpusPerHost: Optional[int] = None
   smcPresent: bool
   datastore: list[DatastoreInfo] = []
   network: list[NetworkInfo] = []
   opaqueNetwork: list[OpaqueNetworkInfo] = []
   distributedVirtualPortgroup: list[DistributedVirtualPortgroupInfo] = []
   distributedVirtualSwitch: list[DistributedVirtualSwitchInfo] = []
   cdRom: list[CdromInfo] = []
   serial: list[SerialInfo] = []
   parallel: list[ParallelInfo] = []
   sound: list[SoundInfo] = []
   usb: list[UsbInfo] = []
   floppy: list[FloppyInfo] = []
   legacyNetworkInfo: list[LegacyNetworkSwitchInfo] = []
   scsiPassthrough: list[ScsiPassthroughInfo] = []
   scsiDisk: list[ScsiDiskDeviceInfo] = []
   ideDisk: list[IdeDiskDeviceInfo] = []
   maxMemMBOptimalPerf: int
   supportedMaxMemMB: Optional[int] = None
   resourcePool: Optional[ResourcePool.RuntimeInfo] = None
   autoVmotion: Optional[bool] = None
   pciPassthrough: list[PciPassthroughInfo] = []
   sriov: list[SriovInfo] = []
   vFlashModule: list[VFlashModuleInfo] = []
   sharedGpuPassthroughTypes: list[PciSharedGpuPassthroughInfo] = []
   availablePersistentMemoryReservationMB: Optional[long] = None
   dynamicPassthrough: list[DynamicPassthroughInfo] = []
   sgxTargetInfo: Optional[SgxTargetInfo] = None
   precisionClockInfo: list[PrecisionClockInfo] = []
   sevSupported: Optional[bool] = None
   vgpuDeviceInfo: list[VgpuDeviceInfo] = []
   vgpuProfileInfo: list[VgpuProfileInfo] = []
   vendorDeviceGroupInfo: list[VendorDeviceGroupInfo] = []
   maxSimultaneousThreads: Optional[int] = None
   dvxClassInfo: list[DvxClassInfo] = []
