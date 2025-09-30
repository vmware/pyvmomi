# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.VmomiSupport import long

from pyVmomi.vim.ResourcePool import ResourcePool

from pyVmomi.vmodl.DynamicData import DynamicData

from pyVmomi.vim.dvs.DistributedVirtualPortgroupInfo import DistributedVirtualPortgroupInfo

from pyVmomi.vim.dvs.DistributedVirtualSwitchInfo import DistributedVirtualSwitchInfo

from pyVmomi.vim.vm.CdromInfo import CdromInfo

from pyVmomi.vim.vm.DatastoreInfo import DatastoreInfo

from pyVmomi.vim.vm.DvxClassInfo import DvxClassInfo

from pyVmomi.vim.vm.DynamicPassthroughInfo import DynamicPassthroughInfo

from pyVmomi.vim.vm.FloppyInfo import FloppyInfo

from pyVmomi.vim.vm.IdeDiskDeviceInfo import IdeDiskDeviceInfo

from pyVmomi.vim.vm.LegacyNetworkSwitchInfo import LegacyNetworkSwitchInfo

from pyVmomi.vim.vm.NetworkInfo import NetworkInfo

from pyVmomi.vim.vm.OpaqueNetworkInfo import OpaqueNetworkInfo

from pyVmomi.vim.vm.ParallelInfo import ParallelInfo

from pyVmomi.vim.vm.PciPassthroughInfo import PciPassthroughInfo

from pyVmomi.vim.vm.PciSharedGpuPassthroughInfo import PciSharedGpuPassthroughInfo

from pyVmomi.vim.vm.PrecisionClockInfo import PrecisionClockInfo

from pyVmomi.vim.vm.ScsiDiskDeviceInfo import ScsiDiskDeviceInfo

from pyVmomi.vim.vm.ScsiPassthroughInfo import ScsiPassthroughInfo

from pyVmomi.vim.vm.SerialInfo import SerialInfo

from pyVmomi.vim.vm.SgxTargetInfo import SgxTargetInfo

from pyVmomi.vim.vm.SoundInfo import SoundInfo

from pyVmomi.vim.vm.SriovInfo import SriovInfo

from pyVmomi.vim.vm.SubnetInfo import SubnetInfo

from pyVmomi.vim.vm.UsbInfo import UsbInfo

from pyVmomi.vim.vm.VFlashModuleInfo import VFlashModuleInfo

from pyVmomi.vim.vm.VendorDeviceGroupInfo import VendorDeviceGroupInfo

from pyVmomi.vim.vm.VgpuDeviceInfo import VgpuDeviceInfo

from pyVmomi.vim.vm.VgpuProfileInfo import VgpuProfileInfo

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
   subnetInfo: list[SubnetInfo] = []
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
   sevSnpSupported: Optional[bool] = None
   tdxSupported: Optional[bool] = None
