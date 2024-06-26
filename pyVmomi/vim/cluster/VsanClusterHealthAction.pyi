# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import ClassVar
from typing import Optional

from pyVmomi.VmomiSupport import Enum

from pyVmomi.vim import KeyValue

from pyVmomi.vmodl import DynamicData
from pyVmomi.vmodl import LocalizableMessage

class VsanClusterHealthAction(DynamicData):
   class VsanClusterHealthActionIdEnum(Enum):
      RepairClusterObjectsAction: ClassVar['VsanClusterHealthActionIdEnum'] = 'RepairClusterObjectsAction'
      UploadHclDb: ClassVar['VsanClusterHealthActionIdEnum'] = 'UploadHclDb'
      UpdateHclDbFromInternet: ClassVar['VsanClusterHealthActionIdEnum'] = 'UpdateHclDbFromInternet'
      EnableHealthService: ClassVar['VsanClusterHealthActionIdEnum'] = 'EnableHealthService'
      DiskBalance: ClassVar['VsanClusterHealthActionIdEnum'] = 'DiskBalance'
      StopDiskBalance: ClassVar['VsanClusterHealthActionIdEnum'] = 'StopDiskBalance'
      RemediateDedup: ClassVar['VsanClusterHealthActionIdEnum'] = 'RemediateDedup'
      UpgradeVsanDiskFormat: ClassVar['VsanClusterHealthActionIdEnum'] = 'UpgradeVsanDiskFormat'
      CreateDVS: ClassVar['VsanClusterHealthActionIdEnum'] = 'CreateDVS'
      ConfigureHA: ClassVar['VsanClusterHealthActionIdEnum'] = 'ConfigureHA'
      ConfigureDRS: ClassVar['VsanClusterHealthActionIdEnum'] = 'ConfigureDRS'
      ConfigureVSAN: ClassVar['VsanClusterHealthActionIdEnum'] = 'ConfigureVSAN'
      ClaimVSANDisks: ClassVar['VsanClusterHealthActionIdEnum'] = 'ClaimVSANDisks'
      ClusterUpgrade: ClassVar['VsanClusterHealthActionIdEnum'] = 'ClusterUpgrade'
      CreateVMKnic: ClassVar['VsanClusterHealthActionIdEnum'] = 'CreateVMKnic'
      CreateVMKnicWithVMotion: ClassVar['VsanClusterHealthActionIdEnum'] = 'CreateVMKnicWithVMotion'
      RunBurnInTest: ClassVar['VsanClusterHealthActionIdEnum'] = 'RunBurnInTest'
      EnableIscsiTargetService: ClassVar['VsanClusterHealthActionIdEnum'] = 'EnableIscsiTargetService'
      EnablePerformanceServiceAction: ClassVar['VsanClusterHealthActionIdEnum'] = 'EnablePerformanceServiceAction'
      RemediateClusterConfig: ClassVar['VsanClusterHealthActionIdEnum'] = 'RemediateClusterConfig'
      EnableCeip: ClassVar['VsanClusterHealthActionIdEnum'] = 'EnableCeip'
      LoginVumIsoDepot: ClassVar['VsanClusterHealthActionIdEnum'] = 'LoginVumIsoDepot'
      PurgeInaccessSwapObjs: ClassVar['VsanClusterHealthActionIdEnum'] = 'PurgeInaccessSwapObjs'
      UploadReleaseCatalog: ClassVar['VsanClusterHealthActionIdEnum'] = 'UploadReleaseCatalog'
      ConfigureAutomaticRebalance: ClassVar['VsanClusterHealthActionIdEnum'] = 'ConfigureAutomaticRebalance'
      RemediateFileService: ClassVar['VsanClusterHealthActionIdEnum'] = 'RemediateFileService'
      RelayoutVsanObjects: ClassVar['VsanClusterHealthActionIdEnum'] = 'RelayoutVsanObjects'
      RemediateFileServiceImbalance: ClassVar['VsanClusterHealthActionIdEnum'] = 'RemediateFileServiceImbalance'
      SelectNvme: ClassVar['VsanClusterHealthActionIdEnum'] = 'SelectNvme'
      CreateFileServiceDomain: ClassVar['VsanClusterHealthActionIdEnum'] = 'CreateFileServiceDomain'
      RemediateIscsiLunsRuntimeStatus: ClassVar['VsanClusterHealthActionIdEnum'] = 'RemediateIscsiLunsRuntimeStatus'
      ShallowRekey: ClassVar['VsanClusterHealthActionIdEnum'] = 'ShallowRekey'
      VsanClusterHealthActionIdEnum_Unknown: ClassVar['VsanClusterHealthActionIdEnum'] = 'VsanClusterHealthActionIdEnum_Unknown'

   actionId: str
   actionLabel: LocalizableMessage
   actionDescription: LocalizableMessage
   enabled: bool
   parameters: list[KeyValue] = []
