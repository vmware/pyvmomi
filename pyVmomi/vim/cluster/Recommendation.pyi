# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from datetime import datetime

from typing import ClassVar
from typing import Optional

from pyVmomi.VmomiSupport import Enum
from pyVmomi.VmomiSupport import ManagedObject

from pyVmomi.vmodl import DynamicData
from pyVmomi.vmodl import LocalizableMessage

from pyVmomi.vim.cluster import Action

class Recommendation(DynamicData):
   class RecommendationType(Enum):
      V1: ClassVar['RecommendationType'] = 'V1'

   class ReasonCode(Enum):
      fairnessCpuAvg: ClassVar['ReasonCode'] = 'fairnessCpuAvg'
      fairnessMemAvg: ClassVar['ReasonCode'] = 'fairnessMemAvg'
      jointAffin: ClassVar['ReasonCode'] = 'jointAffin'
      antiAffin: ClassVar['ReasonCode'] = 'antiAffin'
      hostMaint: ClassVar['ReasonCode'] = 'hostMaint'
      enterStandby: ClassVar['ReasonCode'] = 'enterStandby'
      reservationCpu: ClassVar['ReasonCode'] = 'reservationCpu'
      reservationMem: ClassVar['ReasonCode'] = 'reservationMem'
      powerOnVm: ClassVar['ReasonCode'] = 'powerOnVm'
      powerSaving: ClassVar['ReasonCode'] = 'powerSaving'
      increaseCapacity: ClassVar['ReasonCode'] = 'increaseCapacity'
      checkResource: ClassVar['ReasonCode'] = 'checkResource'
      unreservedCapacity: ClassVar['ReasonCode'] = 'unreservedCapacity'
      colocateCommunicatingVM: ClassVar['ReasonCode'] = 'colocateCommunicatingVM'
      balanceNetworkBandwidthUsage: ClassVar['ReasonCode'] = 'balanceNetworkBandwidthUsage'
      vmHostHardAffinity: ClassVar['ReasonCode'] = 'vmHostHardAffinity'
      vmHostSoftAffinity: ClassVar['ReasonCode'] = 'vmHostSoftAffinity'
      increaseAllocation: ClassVar['ReasonCode'] = 'increaseAllocation'
      balanceDatastoreSpaceUsage: ClassVar['ReasonCode'] = 'balanceDatastoreSpaceUsage'
      balanceDatastoreIOLoad: ClassVar['ReasonCode'] = 'balanceDatastoreIOLoad'
      balanceDatastoreIOPSReservation: ClassVar['ReasonCode'] = 'balanceDatastoreIOPSReservation'
      datastoreMaint: ClassVar['ReasonCode'] = 'datastoreMaint'
      virtualDiskJointAffin: ClassVar['ReasonCode'] = 'virtualDiskJointAffin'
      virtualDiskAntiAffin: ClassVar['ReasonCode'] = 'virtualDiskAntiAffin'
      datastoreSpaceOutage: ClassVar['ReasonCode'] = 'datastoreSpaceOutage'
      storagePlacement: ClassVar['ReasonCode'] = 'storagePlacement'
      iolbDisabledInternal: ClassVar['ReasonCode'] = 'iolbDisabledInternal'
      xvmotionPlacement: ClassVar['ReasonCode'] = 'xvmotionPlacement'
      networkBandwidthReservation: ClassVar['ReasonCode'] = 'networkBandwidthReservation'
      hostInDegradation: ClassVar['ReasonCode'] = 'hostInDegradation'
      hostExitDegradation: ClassVar['ReasonCode'] = 'hostExitDegradation'
      maxVmsConstraint: ClassVar['ReasonCode'] = 'maxVmsConstraint'
      ftConstraints: ClassVar['ReasonCode'] = 'ftConstraints'
      vmHostAffinityPolicy: ClassVar['ReasonCode'] = 'vmHostAffinityPolicy'
      vmHostAntiAffinityPolicy: ClassVar['ReasonCode'] = 'vmHostAntiAffinityPolicy'
      vmAntiAffinityPolicy: ClassVar['ReasonCode'] = 'vmAntiAffinityPolicy'
      balanceVsanUsage: ClassVar['ReasonCode'] = 'balanceVsanUsage'
      ahPlacementOptimization: ClassVar['ReasonCode'] = 'ahPlacementOptimization'
      vmxUpgrade: ClassVar['ReasonCode'] = 'vmxUpgrade'

   key: str
   type: str
   time: datetime
   rating: int
   reason: str
   reasonText: str
   warningText: Optional[str] = None
   warningDetails: Optional[LocalizableMessage] = None
   prerequisite: list[str] = []
   action: list[Action] = []
   target: Optional[ManagedObject] = None
