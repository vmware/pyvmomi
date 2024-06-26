# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import ClassVar
from typing import Optional

from pyVmomi.VmomiSupport import Enum

from pyVmomi.vim.vm import GuestQuiesceSpec

class WindowsQuiesceSpec(GuestQuiesceSpec):
   class VssBackupContext(Enum):
      ctx_auto: ClassVar['VssBackupContext'] = 'ctx_auto'
      ctx_backup: ClassVar['VssBackupContext'] = 'ctx_backup'
      ctx_file_share_backup: ClassVar['VssBackupContext'] = 'ctx_file_share_backup'

   vssBackupType: Optional[int] = None
   vssBootableSystemState: Optional[bool] = None
   vssPartialFileSupport: Optional[bool] = None
   vssBackupContext: Optional[str] = None
