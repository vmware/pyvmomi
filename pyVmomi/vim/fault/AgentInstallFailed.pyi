# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import ClassVar
from typing import Optional

from pyVmomi.VmomiSupport import Enum

from pyVmomi.vim.fault import HostConnectFault

class AgentInstallFailed(HostConnectFault):
   class Reason(Enum):
      NotEnoughSpaceOnDevice: ClassVar['Reason'] = 'NotEnoughSpaceOnDevice'
      PrepareToUpgradeFailed: ClassVar['Reason'] = 'PrepareToUpgradeFailed'
      AgentNotRunning: ClassVar['Reason'] = 'AgentNotRunning'
      AgentNotReachable: ClassVar['Reason'] = 'AgentNotReachable'
      InstallTimedout: ClassVar['Reason'] = 'InstallTimedout'
      SignatureVerificationFailed: ClassVar['Reason'] = 'SignatureVerificationFailed'
      AgentUploadFailed: ClassVar['Reason'] = 'AgentUploadFailed'
      AgentUploadTimedout: ClassVar['Reason'] = 'AgentUploadTimedout'
      UnknownInstallerError: ClassVar['Reason'] = 'UnknownInstallerError'

   reason: Optional[str] = None
   statusCode: Optional[int] = None
   installerOutput: Optional[str] = None
