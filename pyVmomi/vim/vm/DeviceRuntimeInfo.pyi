# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import ClassVar
from typing import Optional

from pyVmomi.VmomiSupport import Enum

from pyVmomi.vmodl import DynamicData

from pyVmomi.vim.vm import FeatureRequirement

class DeviceRuntimeInfo(DynamicData):
   class DeviceRuntimeState(DynamicData):
      pass

   class VirtualEthernetCardRuntimeState(DeviceRuntimeState):
      class VmDirectPathGen2InactiveReasonVm(Enum):
         vmNptIncompatibleGuest: ClassVar['VmDirectPathGen2InactiveReasonVm'] = 'vmNptIncompatibleGuest'
         vmNptIncompatibleGuestDriver: ClassVar['VmDirectPathGen2InactiveReasonVm'] = 'vmNptIncompatibleGuestDriver'
         vmNptIncompatibleAdapterType: ClassVar['VmDirectPathGen2InactiveReasonVm'] = 'vmNptIncompatibleAdapterType'
         vmNptDisabledOrDisconnectedAdapter: ClassVar['VmDirectPathGen2InactiveReasonVm'] = 'vmNptDisabledOrDisconnectedAdapter'
         vmNptIncompatibleAdapterFeatures: ClassVar['VmDirectPathGen2InactiveReasonVm'] = 'vmNptIncompatibleAdapterFeatures'
         vmNptIncompatibleBackingType: ClassVar['VmDirectPathGen2InactiveReasonVm'] = 'vmNptIncompatibleBackingType'
         vmNptInsufficientMemoryReservation: ClassVar['VmDirectPathGen2InactiveReasonVm'] = 'vmNptInsufficientMemoryReservation'
         vmNptFaultToleranceOrRecordReplayConfigured: ClassVar['VmDirectPathGen2InactiveReasonVm'] = 'vmNptFaultToleranceOrRecordReplayConfigured'
         vmNptConflictingIOChainConfigured: ClassVar['VmDirectPathGen2InactiveReasonVm'] = 'vmNptConflictingIOChainConfigured'
         vmNptMonitorBlocks: ClassVar['VmDirectPathGen2InactiveReasonVm'] = 'vmNptMonitorBlocks'
         vmNptConflictingOperationInProgress: ClassVar['VmDirectPathGen2InactiveReasonVm'] = 'vmNptConflictingOperationInProgress'
         vmNptRuntimeError: ClassVar['VmDirectPathGen2InactiveReasonVm'] = 'vmNptRuntimeError'
         vmNptOutOfIntrVector: ClassVar['VmDirectPathGen2InactiveReasonVm'] = 'vmNptOutOfIntrVector'
         vmNptVMCIActive: ClassVar['VmDirectPathGen2InactiveReasonVm'] = 'vmNptVMCIActive'

      class VmDirectPathGen2InactiveReasonOther(Enum):
         vmNptIncompatibleHost: ClassVar['VmDirectPathGen2InactiveReasonOther'] = 'vmNptIncompatibleHost'
         vmNptIncompatibleNetwork: ClassVar['VmDirectPathGen2InactiveReasonOther'] = 'vmNptIncompatibleNetwork'

      vmDirectPathGen2Active: Optional[bool] = None
      vmDirectPathGen2InactiveReasonVm: list[str] = []
      vmDirectPathGen2InactiveReasonOther: list[str] = []
      vmDirectPathGen2InactiveReasonExtended: Optional[str] = None
      uptv2Active: Optional[bool] = None
      uptv2InactiveReasonVm: list[str] = []
      uptv2InactiveReasonOther: list[str] = []
      reservationStatus: Optional[str] = None
      attachmentStatus: Optional[str] = None
      featureRequirement: list[FeatureRequirement] = []

   runtimeState: DeviceRuntimeState
   key: int
