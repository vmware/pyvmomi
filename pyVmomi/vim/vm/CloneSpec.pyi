# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import ClassVar
from typing import Optional

from pyVmomi.VmomiSupport import Enum

from pyVmomi.vmodl.DynamicData import DynamicData

from pyVmomi.vim.vm.ConfigSpec import ConfigSpec

from pyVmomi.vim.vm.RelocateSpec import RelocateSpec

from pyVmomi.vim.vm.Snapshot import Snapshot

from pyVmomi.vim.vm.customization.Specification import Specification

class CloneSpec(DynamicData):
   class TpmProvisionPolicy(Enum):
      copy: ClassVar['TpmProvisionPolicy'] = 'copy'
      replace: ClassVar['TpmProvisionPolicy'] = 'replace'

   location: RelocateSpec
   template: bool
   config: Optional[ConfigSpec] = None
   customization: Optional[Specification] = None
   powerOn: bool
   snapshot: Optional[Snapshot] = None
   memory: Optional[bool] = None
   tpmProvisionPolicy: Optional[str] = None
