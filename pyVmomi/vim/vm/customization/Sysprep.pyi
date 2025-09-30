# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vim.vm.customization.GuiRunOnce import GuiRunOnce

from pyVmomi.vim.vm.customization.GuiUnattended import GuiUnattended

from pyVmomi.vim.vm.customization.Identification import Identification

from pyVmomi.vim.vm.customization.IdentitySettings import IdentitySettings

from pyVmomi.vim.vm.customization.LicenseFilePrintData import LicenseFilePrintData

from pyVmomi.vim.vm.customization.UserData import UserData

class Sysprep(IdentitySettings):
   guiUnattended: GuiUnattended
   userData: UserData
   guiRunOnce: Optional[GuiRunOnce] = None
   identification: Identification
   licenseFilePrintData: Optional[LicenseFilePrintData] = None
