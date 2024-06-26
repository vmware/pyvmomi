# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.VmomiSupport import byte

from pyVmomi.vmodl import DynamicData

from pyVmomi.vim.vm.customization import AdapterMapping
from pyVmomi.vim.vm.customization import GlobalIPSettings
from pyVmomi.vim.vm.customization import IdentitySettings
from pyVmomi.vim.vm.customization import Options

class Specification(DynamicData):
   options: Optional[Options] = None
   identity: IdentitySettings
   globalIPSettings: GlobalIPSettings
   nicSettingMap: list[AdapterMapping] = []
   encryptionKey: list[byte] = []
