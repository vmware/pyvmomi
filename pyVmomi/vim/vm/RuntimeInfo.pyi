# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from datetime import datetime

from typing import Optional

from pyVmomi.VmomiSupport import long

from pyVmomi.vim import HostSystem
from pyVmomi.vim import VirtualMachine

from pyVmomi.vmodl import DynamicData

from pyVmomi.vim.host import FeatureMask

from pyVmomi.vim.vm import DeviceRuntimeInfo
from pyVmomi.vim.vm import FeatureRequirement
from pyVmomi.vim.vm import QuestionInfo

class RuntimeInfo(DynamicData):
   class DasProtectionState(DynamicData):
      dasProtected: bool

   device: list[DeviceRuntimeInfo] = []
   host: Optional[HostSystem] = None
   connectionState: VirtualMachine.ConnectionState
   powerState: VirtualMachine.PowerState
   vmFailoverInProgress: Optional[bool] = None
   faultToleranceState: VirtualMachine.FaultToleranceState
   dasVmProtection: Optional[DasProtectionState] = None
   toolsInstallerMounted: bool
   suspendTime: Optional[datetime] = None
   bootTime: Optional[datetime] = None
   suspendInterval: Optional[long] = None
   question: Optional[QuestionInfo] = None
   memoryOverhead: Optional[long] = None
   maxCpuUsage: Optional[int] = None
   maxMemoryUsage: Optional[int] = None
   numMksConnections: int
   recordReplayState: VirtualMachine.RecordReplayState
   cleanPowerOff: Optional[bool] = None
   needSecondaryReason: Optional[str] = None
   onlineStandby: bool
   minRequiredEVCModeKey: Optional[str] = None
   consolidationNeeded: bool
   offlineFeatureRequirement: list[FeatureRequirement] = []
   featureRequirement: list[FeatureRequirement] = []
   featureMask: list[FeatureMask] = []
   vFlashCacheAllocation: Optional[long] = None
   paused: Optional[bool] = None
   snapshotInBackground: Optional[bool] = None
   quiescedForkParent: Optional[bool] = None
   instantCloneFrozen: Optional[bool] = None
   cryptoState: Optional[str] = None
   suspendedToMemory: Optional[bool] = None
   opNotificationTimeout: Optional[long] = None
   iommuActive: Optional[bool] = None
