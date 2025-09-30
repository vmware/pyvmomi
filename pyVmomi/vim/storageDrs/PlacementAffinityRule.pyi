# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import ClassVar
from typing import Optional

from pyVmomi.VmomiSupport import Enum

from pyVmomi.vim.VirtualMachine import VirtualMachine

from pyVmomi.vmodl.DynamicData import DynamicData

class PlacementAffinityRule(DynamicData):
   class RuleType(Enum):
      affinity: ClassVar['RuleType'] = 'affinity'
      antiAffinity: ClassVar['RuleType'] = 'antiAffinity'
      softAffinity: ClassVar['RuleType'] = 'softAffinity'
      softAntiAffinity: ClassVar['RuleType'] = 'softAntiAffinity'

   class RuleScope(Enum):
      cluster: ClassVar['RuleScope'] = 'cluster'
      host: ClassVar['RuleScope'] = 'host'
      storagePod: ClassVar['RuleScope'] = 'storagePod'
      datastore: ClassVar['RuleScope'] = 'datastore'

   ruleType: str
   ruleScope: str
   vms: list[VirtualMachine] = []
   keys: list[str] = []
