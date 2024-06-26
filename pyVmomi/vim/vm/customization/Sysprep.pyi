# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vim.vm.customization import GuiRunOnce
from pyVmomi.vim.vm.customization import GuiUnattended
from pyVmomi.vim.vm.customization import Identification
from pyVmomi.vim.vm.customization import IdentitySettings
from pyVmomi.vim.vm.customization import LicenseFilePrintData
from pyVmomi.vim.vm.customization import UserData

class Sysprep(IdentitySettings):
   guiUnattended: GuiUnattended
   userData: UserData
   guiRunOnce: Optional[GuiRunOnce] = None
   identification: Identification
   licenseFilePrintData: Optional[LicenseFilePrintData] = None
