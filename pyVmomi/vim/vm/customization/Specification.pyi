# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.VmomiSupport import byte

from pyVmomi.vmodl.DynamicData import DynamicData

from pyVmomi.vim.vm.customization.AdapterMapping import AdapterMapping

from pyVmomi.vim.vm.customization.GlobalIPSettings import GlobalIPSettings

from pyVmomi.vim.vm.customization.IdentitySettings import IdentitySettings

from pyVmomi.vim.vm.customization.Options import Options

class Specification(DynamicData):
   options: Optional[Options] = None
   identity: IdentitySettings
   globalIPSettings: GlobalIPSettings
   nicSettingMap: list[AdapterMapping] = []
   encryptionKey: list[byte] = []
