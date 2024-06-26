# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import ClassVar
from typing import Optional

from pyVmomi.VmomiSupport import Enum

from pyVmomi.vmodl import DynamicData

from pyVmomi.vim.vm import ConfigSpec
from pyVmomi.vim.vm import RelocateSpec
from pyVmomi.vim.vm import Snapshot

from pyVmomi.vim.vm.customization import Specification

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
