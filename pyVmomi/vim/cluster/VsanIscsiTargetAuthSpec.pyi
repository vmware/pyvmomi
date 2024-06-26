# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import ClassVar
from typing import Optional

from pyVmomi.VmomiSupport import Enum

from pyVmomi.vmodl import DynamicData

class VsanIscsiTargetAuthSpec(DynamicData):
   class VsanIscsiTargetAuthType(Enum):
      NoAuth: ClassVar['VsanIscsiTargetAuthType'] = 'NoAuth'
      CHAP: ClassVar['VsanIscsiTargetAuthType'] = 'CHAP'
      CHAP_Mutual: ClassVar['VsanIscsiTargetAuthType'] = 'CHAP_Mutual'
      VsanIscsiTargetAuthType_Unknown: ClassVar['VsanIscsiTargetAuthType'] = 'VsanIscsiTargetAuthType_Unknown'

   authType: Optional[str] = None
   userNameAttachToTarget: Optional[str] = None
   userSecretAttachToTarget: Optional[str] = None
   userNameAttachToInitiator: Optional[str] = None
   userSecretAttachToInitiator: Optional[str] = None
