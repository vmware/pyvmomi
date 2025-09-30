# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from pyVmomi.VmomiSupport import ManagedObject

from pyVmomi.vim.host.AuthenticationManagerInfo import AuthenticationManagerInfo

from pyVmomi.vim.host.AuthenticationStore import AuthenticationStore

class AuthenticationManager(ManagedObject):
   @property
   def info(self) -> AuthenticationManagerInfo: ...
   @property
   def supportedStore(self) -> list[AuthenticationStore]: ...
