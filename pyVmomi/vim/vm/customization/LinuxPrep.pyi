# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vim.vm.customization import IdentitySettings
from pyVmomi.vim.vm.customization import NameGenerator

class LinuxPrep(IdentitySettings):
   hostName: NameGenerator
   domain: str
   timeZone: Optional[str] = None
   hwClockUTC: Optional[bool] = None
   scriptText: Optional[str] = None
   compatibleCustomizationMethod: Optional[str] = None
