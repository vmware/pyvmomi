# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import ClassVar
from typing import Optional

from pyVmomi.VmomiSupport import Enum
from pyVmomi.VmomiSupport import long

from pyVmomi.vmodl import DynamicData

from pyVmomi.vim.host import SgxRegistrationInfo

class SgxInfo(DynamicData):
   class SgxStates(Enum):
      notPresent: ClassVar['SgxStates'] = 'notPresent'
      disabledBIOS: ClassVar['SgxStates'] = 'disabledBIOS'
      disabledCFW101: ClassVar['SgxStates'] = 'disabledCFW101'
      disabledCPUMismatch: ClassVar['SgxStates'] = 'disabledCPUMismatch'
      disabledNoFLC: ClassVar['SgxStates'] = 'disabledNoFLC'
      disabledNUMAUnsup: ClassVar['SgxStates'] = 'disabledNUMAUnsup'
      disabledMaxEPCRegs: ClassVar['SgxStates'] = 'disabledMaxEPCRegs'
      enabled: ClassVar['SgxStates'] = 'enabled'

   class FlcModes(Enum):
      off: ClassVar['FlcModes'] = 'off'
      locked: ClassVar['FlcModes'] = 'locked'
      unlocked: ClassVar['FlcModes'] = 'unlocked'

   sgxState: str
   totalEpcMemory: long
   flcMode: str
   lePubKeyHash: Optional[str] = None
   registrationInfo: Optional[SgxRegistrationInfo] = None
