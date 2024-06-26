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

class TpmAttestationInfo(DynamicData):
   class AcceptanceStatus(Enum):
      notAccepted: ClassVar['AcceptanceStatus'] = 'notAccepted'
      accepted: ClassVar['AcceptanceStatus'] = 'accepted'

   time: datetime
   status: AcceptanceStatus
   message: Optional[LocalizableMessage] = None
