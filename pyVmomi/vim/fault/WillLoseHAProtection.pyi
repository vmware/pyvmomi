# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import ClassVar

from pyVmomi.VmomiSupport import Enum

from pyVmomi.vim.fault.MigrationFault import MigrationFault

class WillLoseHAProtection(MigrationFault):
   class Resolution(Enum):
      svmotion: ClassVar['Resolution'] = 'svmotion'
      relocate: ClassVar['Resolution'] = 'relocate'

   resolution: str
