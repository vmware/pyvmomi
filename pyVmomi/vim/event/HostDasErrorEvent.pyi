# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import ClassVar
from typing import Optional

from pyVmomi.VmomiSupport import Enum

from pyVmomi.vim.event import HostEvent

class HostDasErrorEvent(HostEvent):
   class HostDasErrorReason(Enum):
      configFailed: ClassVar['HostDasErrorReason'] = 'configFailed'
      timeout: ClassVar['HostDasErrorReason'] = 'timeout'
      communicationInitFailed: ClassVar['HostDasErrorReason'] = 'communicationInitFailed'
      healthCheckScriptFailed: ClassVar['HostDasErrorReason'] = 'healthCheckScriptFailed'
      agentFailed: ClassVar['HostDasErrorReason'] = 'agentFailed'
      agentShutdown: ClassVar['HostDasErrorReason'] = 'agentShutdown'
      isolationAddressUnpingable: ClassVar['HostDasErrorReason'] = 'isolationAddressUnpingable'
      other: ClassVar['HostDasErrorReason'] = 'other'

   message: Optional[str] = None
   reason: Optional[str] = None
