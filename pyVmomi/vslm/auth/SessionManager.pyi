# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import NoReturn

from pyVmomi.VmomiSupport import ManagedObject

class SessionManager(ManagedObject):
   def LoginByToken(self, delegatedTokenXml: str) -> NoReturn: ...
   def Logout(self) -> NoReturn: ...
