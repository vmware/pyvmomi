# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import ClassVar
from typing import Optional

from pyVmomi.VmomiSupport import Enum

from pyVmomi.vim import Network

from pyVmomi.vim.fault import VmConfigFault

class CannotUseNetwork(VmConfigFault):
   class Reason(Enum):
      NetworkReservationNotSupported: ClassVar['Reason'] = 'NetworkReservationNotSupported'
      MismatchedNetworkPolicies: ClassVar['Reason'] = 'MismatchedNetworkPolicies'
      MismatchedDvsVersionOrVendor: ClassVar['Reason'] = 'MismatchedDvsVersionOrVendor'
      VMotionToUnsupportedNetworkType: ClassVar['Reason'] = 'VMotionToUnsupportedNetworkType'
      NetworkUnderMaintenance: ClassVar['Reason'] = 'NetworkUnderMaintenance'
      MismatchedEnsMode: ClassVar['Reason'] = 'MismatchedEnsMode'
      MismatchedRealTimeDvs: ClassVar['Reason'] = 'MismatchedRealTimeDvs'

   device: str
   backing: str
   connected: bool
   reason: str
   network: Optional[Network] = None
