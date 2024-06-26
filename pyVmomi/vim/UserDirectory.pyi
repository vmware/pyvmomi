# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.VmomiSupport import ManagedObject

from pyVmomi.vim import UserSearchResult

class UserDirectory(ManagedObject):
   @property
   def domainList(self) -> list[str]: ...

   def RetrieveUserGroups(self, domain: Optional[str], searchStr: str, belongsToGroup: Optional[str], belongsToUser: Optional[str], exactMatch: bool, findUsers: bool, findGroups: bool) -> list[UserSearchResult]: ...
