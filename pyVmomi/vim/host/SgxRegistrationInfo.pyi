# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from datetime import datetime

from typing import ClassVar
from typing import Optional

from pyVmomi.VmomiSupport import Enum

from pyVmomi.vmodl import DynamicData

class SgxRegistrationInfo(DynamicData):
   class RegistrationStatus(Enum):
      notApplicable: ClassVar['RegistrationStatus'] = 'notApplicable'
      incomplete: ClassVar['RegistrationStatus'] = 'incomplete'
      complete: ClassVar['RegistrationStatus'] = 'complete'

   class RegistrationType(Enum):
      manifest: ClassVar['RegistrationType'] = 'manifest'
      addPackage: ClassVar['RegistrationType'] = 'addPackage'

   status: Optional[str] = None
   biosError: Optional[int] = None
   registrationUrl: Optional[str] = None
   type: Optional[str] = None
   ppid: Optional[str] = None
   lastRegisteredTime: Optional[datetime] = None
