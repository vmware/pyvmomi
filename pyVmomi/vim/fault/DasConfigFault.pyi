# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import ClassVar
from typing import Optional

from pyVmomi.VmomiSupport import Enum

from pyVmomi.vim.event import Event

from pyVmomi.vim.fault import VimFault

class DasConfigFault(VimFault):
   class DasConfigFaultReason(Enum):
      HostNetworkMisconfiguration: ClassVar['DasConfigFaultReason'] = 'HostNetworkMisconfiguration'
      HostMisconfiguration: ClassVar['DasConfigFaultReason'] = 'HostMisconfiguration'
      InsufficientPrivileges: ClassVar['DasConfigFaultReason'] = 'InsufficientPrivileges'
      NoPrimaryAgentAvailable: ClassVar['DasConfigFaultReason'] = 'NoPrimaryAgentAvailable'
      Other: ClassVar['DasConfigFaultReason'] = 'Other'
      NoDatastoresConfigured: ClassVar['DasConfigFaultReason'] = 'NoDatastoresConfigured'
      CreateConfigVvolFailed: ClassVar['DasConfigFaultReason'] = 'CreateConfigVvolFailed'
      VSanNotSupportedOnHost: ClassVar['DasConfigFaultReason'] = 'VSanNotSupportedOnHost'
      DasNetworkMisconfiguration: ClassVar['DasConfigFaultReason'] = 'DasNetworkMisconfiguration'
      SetDesiredImageSpecFailed: ClassVar['DasConfigFaultReason'] = 'SetDesiredImageSpecFailed'
      ApplyHAVibsOnClusterFailed: ClassVar['DasConfigFaultReason'] = 'ApplyHAVibsOnClusterFailed'

   reason: Optional[str] = None
   output: Optional[str] = None
   event: list[Event] = []
