# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import NoReturn
from typing import Optional

from pyVmomi.VmomiSupport import ManagedObject

from pyVmomi.vim import VirtualMachine

from pyVmomi.vmodl import DynamicData

from pyVmomi.vim.vm.guest import GuestAuthentication

class AliasManager(ManagedObject):
   class GuestAuthSubject(DynamicData):
      pass

   class GuestAuthAnySubject(GuestAuthSubject):
      pass

   class GuestAuthNamedSubject(GuestAuthSubject):
      name: str

   class GuestAuthAliasInfo(DynamicData):
      subject: GuestAuthSubject
      comment: str

   class GuestAliases(DynamicData):
      base64Cert: str
      aliases: list[GuestAuthAliasInfo] = []

   class GuestMappedAliases(DynamicData):
      base64Cert: str
      username: str
      subjects: list[GuestAuthSubject] = []

   def AddAlias(self, vm: VirtualMachine, auth: GuestAuthentication, username: str, mapCert: bool, base64Cert: str, aliasInfo: GuestAuthAliasInfo) -> NoReturn: ...
   def RemoveAlias(self, vm: VirtualMachine, auth: GuestAuthentication, username: str, base64Cert: str, subject: GuestAuthSubject) -> NoReturn: ...
   def RemoveAliasByCert(self, vm: VirtualMachine, auth: GuestAuthentication, username: str, base64Cert: str) -> NoReturn: ...
   def ListAliases(self, vm: VirtualMachine, auth: GuestAuthentication, username: str) -> list[GuestAliases]: ...
   def ListMappedAliases(self, vm: VirtualMachine, auth: GuestAuthentication) -> list[GuestMappedAliases]: ...
