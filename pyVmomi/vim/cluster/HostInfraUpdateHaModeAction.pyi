# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import ClassVar

from pyVmomi.VmomiSupport import Enum

from pyVmomi.vim.cluster import Action

class HostInfraUpdateHaModeAction(Action):
   class OperationType(Enum):
      enterQuarantine: ClassVar['OperationType'] = 'enterQuarantine'
      exitQuarantine: ClassVar['OperationType'] = 'exitQuarantine'
      enterMaintenance: ClassVar['OperationType'] = 'enterMaintenance'

   operationType: str
