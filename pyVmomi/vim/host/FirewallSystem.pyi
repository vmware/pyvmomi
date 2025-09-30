# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import ClassVar
from typing import Optional

from pyVmomi.VmomiSupport import Enum

from pyVmomi.vim.ExtensibleManagedObject import ExtensibleManagedObject

from pyVmomi.vim.host.FirewallInfo import FirewallInfo

from pyVmomi.vim.host.Ruleset import Ruleset

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

   def UpdateDefaultPolicy(self, defaultPolicy: FirewallInfo.DefaultPolicy) -> None: ...
   def EnableRuleset(self, id: str) -> None: ...
   def DisableRuleset(self, id: str) -> None: ...
   def UpdateRuleset(self, id: str, spec: Ruleset.RulesetSpec) -> None: ...
   def Refresh(self) -> None: ...
