# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.VmomiSupport import ManagedObject

from pyVmomi.vim import ManagedEntity

from pyVmomi.vim.profile import PolicyMetadata
from pyVmomi.vim.profile import Profile

class ProfileManager(ManagedObject):
   @property
   def profile(self) -> list[Profile]: ...

   def CreateProfile(self, createSpec: Profile.CreateSpec) -> Profile: ...
   def QueryPolicyMetadata(self, policyName: list[str], profile: Optional[Profile]) -> list[PolicyMetadata]: ...
   def FindAssociatedProfile(self, entity: ManagedEntity) -> list[Profile]: ...
