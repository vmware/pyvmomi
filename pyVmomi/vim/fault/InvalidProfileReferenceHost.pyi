# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import ClassVar
from typing import Optional

from pyVmomi.VmomiSupport import Enum

from pyVmomi.vim import HostSystem

from pyVmomi.vmodl import RuntimeFault

from pyVmomi.vim.profile import Profile

class InvalidProfileReferenceHost(RuntimeFault):
   class Reason(Enum):
      incompatibleVersion: ClassVar['Reason'] = 'incompatibleVersion'
      missingReferenceHost: ClassVar['Reason'] = 'missingReferenceHost'

   reason: Optional[str] = None
   host: Optional[HostSystem] = None
   profile: Optional[Profile] = None
   profileName: Optional[str] = None
