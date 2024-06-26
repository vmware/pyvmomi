# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from datetime import datetime

from typing import ClassVar
from typing import Optional

from pyVmomi.VmomiSupport import Enum

from pyVmomi.vmodl import DynamicData
from pyVmomi.vmodl import LocalizableMessage

class TrustAuthorityAttestationInfo(DynamicData):
   class AttestationStatus(Enum):
      attested: ClassVar['AttestationStatus'] = 'attested'
      notAttested: ClassVar['AttestationStatus'] = 'notAttested'
      unknown: ClassVar['AttestationStatus'] = 'unknown'

   attestationStatus: str
   serviceId: Optional[str] = None
   attestedAt: Optional[datetime] = None
   attestedUntil: Optional[datetime] = None
   messages: list[LocalizableMessage] = []
