# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import ClassVar
from typing import Optional

from pyVmomi.VmomiSupport import Enum

from pyVmomi.vim.vm.customization.Options import Options

class WinOptions(Options):
   class SysprepRebootOption(Enum):
      reboot: ClassVar['SysprepRebootOption'] = 'reboot'
      noreboot: ClassVar['SysprepRebootOption'] = 'noreboot'
      shutdown: ClassVar['SysprepRebootOption'] = 'shutdown'

   changeSID: bool
   deleteAccounts: bool
   reboot: Optional[SysprepRebootOption] = None
