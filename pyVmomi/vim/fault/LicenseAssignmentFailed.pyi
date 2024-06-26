# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import ClassVar
from typing import Optional

from pyVmomi.VmomiSupport import Enum

from pyVmomi.vmodl import RuntimeFault

class LicenseAssignmentFailed(RuntimeFault):
   class Reason(Enum):
      keyEntityMismatch: ClassVar['Reason'] = 'keyEntityMismatch'
      downgradeDisallowed: ClassVar['Reason'] = 'downgradeDisallowed'
      inventoryNotManageableByVirtualCenter: ClassVar['Reason'] = 'inventoryNotManageableByVirtualCenter'
      hostsUnmanageableByVirtualCenterWithoutLicenseServer: ClassVar['Reason'] = 'hostsUnmanageableByVirtualCenterWithoutLicenseServer'

   reason: Optional[str] = None
