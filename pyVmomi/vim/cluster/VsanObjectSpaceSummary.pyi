# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import ClassVar
from typing import Optional

from pyVmomi.VmomiSupport import Enum
from pyVmomi.VmomiSupport import long

from pyVmomi.vmodl import DynamicData

class VsanObjectSpaceSummary(DynamicData):
   class VsanObjectTypeEnum(Enum):
      vmswap: ClassVar['VsanObjectTypeEnum'] = 'vmswap'
      vdisk: ClassVar['VsanObjectTypeEnum'] = 'vdisk'
      namespace: ClassVar['VsanObjectTypeEnum'] = 'namespace'
      vmem: ClassVar['VsanObjectTypeEnum'] = 'vmem'
      statsdb: ClassVar['VsanObjectTypeEnum'] = 'statsdb'
      iscsiTarget: ClassVar['VsanObjectTypeEnum'] = 'iscsiTarget'
      iscsiLun: ClassVar['VsanObjectTypeEnum'] = 'iscsiLun'
      other: ClassVar['VsanObjectTypeEnum'] = 'other'
      fileSystemOverhead: ClassVar['VsanObjectTypeEnum'] = 'fileSystemOverhead'
      dedupOverhead: ClassVar['VsanObjectTypeEnum'] = 'dedupOverhead'
      spaceUnderDedupConsideration: ClassVar['VsanObjectTypeEnum'] = 'spaceUnderDedupConsideration'
      checksumOverhead: ClassVar['VsanObjectTypeEnum'] = 'checksumOverhead'
      improvedVirtualDisk: ClassVar['VsanObjectTypeEnum'] = 'improvedVirtualDisk'
      transientSpace: ClassVar['VsanObjectTypeEnum'] = 'transientSpace'
      slackSpaceCapRequiredForHost: ClassVar['VsanObjectTypeEnum'] = 'slackSpaceCapRequiredForHost'
      resynPauseThresholdForHost: ClassVar['VsanObjectTypeEnum'] = 'resynPauseThresholdForHost'
      minSpaceRequiredForVsanOp: ClassVar['VsanObjectTypeEnum'] = 'minSpaceRequiredForVsanOp'
      hostRebuildCapacity: ClassVar['VsanObjectTypeEnum'] = 'hostRebuildCapacity'
      physicalTransientSpace: ClassVar['VsanObjectTypeEnum'] = 'physicalTransientSpace'
      haMetadataObject: ClassVar['VsanObjectTypeEnum'] = 'haMetadataObject'
      fileServiceRoot: ClassVar['VsanObjectTypeEnum'] = 'fileServiceRoot'
      attachedCnsVolBlock: ClassVar['VsanObjectTypeEnum'] = 'attachedCnsVolBlock'
      detachedCnsVolBlock: ClassVar['VsanObjectTypeEnum'] = 'detachedCnsVolBlock'
      attachedCnsVolFile: ClassVar['VsanObjectTypeEnum'] = 'attachedCnsVolFile'
      detachedCnsVolFile: ClassVar['VsanObjectTypeEnum'] = 'detachedCnsVolFile'
      cnsVolFile: ClassVar['VsanObjectTypeEnum'] = 'cnsVolFile'
      fileShare: ClassVar['VsanObjectTypeEnum'] = 'fileShare'
      extension: ClassVar['VsanObjectTypeEnum'] = 'extension'
      hbrDisk: ClassVar['VsanObjectTypeEnum'] = 'hbrDisk'
      hbrCfg: ClassVar['VsanObjectTypeEnum'] = 'hbrCfg'
      hbrPersist: ClassVar['VsanObjectTypeEnum'] = 'hbrPersist'
      traceobject: ClassVar['VsanObjectTypeEnum'] = 'traceobject'
      esaObjectOverhead: ClassVar['VsanObjectTypeEnum'] = 'esaObjectOverhead'
      dedupSharedUserData: ClassVar['VsanObjectTypeEnum'] = 'dedupSharedUserData'
      VsanObjectTypeEnum_Unknown: ClassVar['VsanObjectTypeEnum'] = 'VsanObjectTypeEnum_Unknown'

   objType: Optional[str] = None
   overheadB: Optional[long] = None
   temporaryOverheadB: Optional[long] = None
   primaryCapacityB: Optional[long] = None
   provisionCapacityB: Optional[long] = None
   reservedCapacityB: Optional[long] = None
   overReservedB: Optional[long] = None
   physicalUsedB: Optional[long] = None
   usedB: Optional[long] = None
   objTypeExt: Optional[str] = None
   objTypeExtDesc: Optional[str] = None
   snapshotUsedB: Optional[long] = None
