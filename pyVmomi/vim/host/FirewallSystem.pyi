# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import ClassVar
from typing import NoReturn
from typing import Optional

from pyVmomi.VmomiSupport import Enum

from pyVmomi.vim import ExtensibleManagedObject

from pyVmomi.vim.host import FirewallInfo
from pyVmomi.vim.host import Ruleset

class FirewallSystem(ExtensibleManagedObject):
   class ServiceName(Enum):
      vpxa: ClassVar['ServiceName'] = 'vpxa'

   class RuleSetId(Enum):
      faultTolerance: ClassVar['RuleSetId'] = 'faultTolerance'
      fdm: ClassVar['RuleSetId'] = 'fdm'
      updateManager: ClassVar['RuleSetId'] = 'updateManager'
      vpxHeartbeats: ClassVar['RuleSetId'] = 'vpxHeartbeats'

   @property
   def firewallInfo(self) -> Optional[FirewallInfo]: ...

   def UpdateDefaultPolicy(self, defaultPolicy: FirewallInfo.DefaultPolicy) -> NoReturn: ...
   def EnableRuleset(self, id: str) -> NoReturn: ...
   def DisableRuleset(self, id: str) -> NoReturn: ...
   def UpdateRuleset(self, id: str, spec: Ruleset.RulesetSpec) -> NoReturn: ...
   def Refresh(self) -> NoReturn: ...
