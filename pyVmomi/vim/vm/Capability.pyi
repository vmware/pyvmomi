# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vmodl import DynamicData

class Capability(DynamicData):
   snapshotOperationsSupported: bool
   multipleSnapshotsSupported: bool
   snapshotConfigSupported: bool
   poweredOffSnapshotsSupported: bool
   memorySnapshotsSupported: bool
   revertToSnapshotSupported: bool
   quiescedSnapshotsSupported: bool
   disableSnapshotsSupported: bool
   lockSnapshotsSupported: bool
   consolePreferencesSupported: bool
   cpuFeatureMaskSupported: bool
   s1AcpiManagementSupported: bool
   settingScreenResolutionSupported: bool
   toolsAutoUpdateSupported: bool
   vmNpivWwnSupported: bool
   npivWwnOnNonRdmVmSupported: bool
   vmNpivWwnDisableSupported: bool
   vmNpivWwnUpdateSupported: bool
   swapPlacementSupported: bool
   toolsSyncTimeSupported: bool
   virtualMmuUsageSupported: bool
   diskSharesSupported: bool
   bootOptionsSupported: bool
   bootRetryOptionsSupported: bool
   settingVideoRamSizeSupported: bool
   settingDisplayTopologySupported: bool
   recordReplaySupported: bool
   changeTrackingSupported: bool
   multipleCoresPerSocketSupported: bool
   hostBasedReplicationSupported: bool
   guestAutoLockSupported: bool
   memoryReservationLockSupported: bool
   featureRequirementSupported: bool
   poweredOnMonitorTypeChangeSupported: bool
   seSparseDiskSupported: bool
   nestedHVSupported: bool
   vPMCSupported: bool
   secureBootSupported: Optional[bool] = None
   perVmEvcSupported: Optional[bool] = None
   virtualMmuUsageIgnored: Optional[bool] = None
   virtualExecUsageIgnored: Optional[bool] = None
   diskOnlySnapshotOnSuspendedVMSupported: Optional[bool] = None
   suspendToMemorySupported: Optional[bool] = None
   toolsSyncTimeAllowSupported: Optional[bool] = None
   sevSupported: Optional[bool] = None
   pmemFailoverSupported: Optional[bool] = None
   requireSgxAttestationSupported: Optional[bool] = None
   changeModeDisksSupported: Optional[bool] = None
   vendorDeviceGroupSupported: Optional[bool] = None
