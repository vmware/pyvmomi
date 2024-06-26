# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import ClassVar
from typing import Optional

from pyVmomi.VmomiSupport import Enum

from pyVmomi.vim.event import HostEvent

class HostDisconnectedEvent(HostEvent):
   class ReasonCode(Enum):
      sslThumbprintVerifyFailed: ClassVar['ReasonCode'] = 'sslThumbprintVerifyFailed'
      licenseExpired: ClassVar['ReasonCode'] = 'licenseExpired'
      agentUpgrade: ClassVar['ReasonCode'] = 'agentUpgrade'
      userRequest: ClassVar['ReasonCode'] = 'userRequest'
      insufficientLicenses: ClassVar['ReasonCode'] = 'insufficientLicenses'
      agentOutOfDate: ClassVar['ReasonCode'] = 'agentOutOfDate'
      passwordDecryptFailure: ClassVar['ReasonCode'] = 'passwordDecryptFailure'
      unknown: ClassVar['ReasonCode'] = 'unknown'
      vcVRAMCapacityExceeded: ClassVar['ReasonCode'] = 'vcVRAMCapacityExceeded'

   reason: Optional[str] = None
