# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import ClassVar
from typing import Optional

from pyVmomi.VmomiSupport import Enum

from pyVmomi.vmodl.DynamicData import DynamicData

from pyVmomi.vim.encryption.CryptoSpec import CryptoSpec

from pyVmomi.vim.vm.BaseIndependentFilterSpec import BaseIndependentFilterSpec

from pyVmomi.vim.vm.ProfileSpec import ProfileSpec

from pyVmomi.vim.vm.device.VirtualDevice import VirtualDevice

class VirtualDeviceSpec(DynamicData):
   class Operation(Enum):
      add: ClassVar['Operation'] = 'add'
      remove: ClassVar['Operation'] = 'remove'
      edit: ClassVar['Operation'] = 'edit'

   class FileOperation(Enum):
      create: ClassVar['FileOperation'] = 'create'
      destroy: ClassVar['FileOperation'] = 'destroy'
      replace: ClassVar['FileOperation'] = 'replace'

   class BackingSpec(DynamicData):
      parent: Optional[BackingSpec] = None
      crypto: Optional[CryptoSpec] = None

   class ChangeMode(Enum):
      fail: ClassVar['ChangeMode'] = 'fail'
      skip: ClassVar['ChangeMode'] = 'skip'

   operation: Optional[Operation] = None
   fileOperation: Optional[FileOperation] = None
   device: VirtualDevice
   profile: list[ProfileSpec] = []
   backing: Optional[BackingSpec] = None
   filterSpec: list[BaseIndependentFilterSpec] = []
   changeMode: Optional[str] = None
