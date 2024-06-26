# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import ClassVar
from typing import Optional

from pyVmomi.VmomiSupport import Enum

from pyVmomi.vmodl import DynamicData

class VmComponentProtectionSettings(DynamicData):
   class StorageVmReaction(Enum):
      disabled: ClassVar['StorageVmReaction'] = 'disabled'
      warning: ClassVar['StorageVmReaction'] = 'warning'
      restartConservative: ClassVar['StorageVmReaction'] = 'restartConservative'
      restartAggressive: ClassVar['StorageVmReaction'] = 'restartAggressive'
      clusterDefault: ClassVar['StorageVmReaction'] = 'clusterDefault'

   class VmReactionOnAPDCleared(Enum):
      none: ClassVar['VmReactionOnAPDCleared'] = 'none'
      reset: ClassVar['VmReactionOnAPDCleared'] = 'reset'
      useClusterDefault: ClassVar['VmReactionOnAPDCleared'] = 'useClusterDefault'

   vmStorageProtectionForAPD: Optional[str] = None
   enableAPDTimeoutForHosts: Optional[bool] = None
   vmTerminateDelayForAPDSec: Optional[int] = None
   vmReactionOnAPDCleared: Optional[str] = None
   vmStorageProtectionForPDL: Optional[str] = None
