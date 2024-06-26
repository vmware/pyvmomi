# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import NoReturn
from typing import Optional

from pyVmomi.VmomiSupport import ManagedObject

from pyVmomi.vim import HostSystem

from pyVmomi.vim.profile.host import HostSpecification
from pyVmomi.vim.profile.host import HostSubSpecification

class HostSpecificationManager(ManagedObject):
   def UpdateHostSpecification(self, host: HostSystem, hostSpec: HostSpecification) -> NoReturn: ...
   def UpdateHostSubSpecification(self, host: HostSystem, hostSubSpec: HostSubSpecification) -> NoReturn: ...
   def RetrieveHostSpecification(self, host: HostSystem, fromHost: bool) -> HostSpecification: ...
   def DeleteHostSubSpecification(self, host: HostSystem, subSpecName: str) -> NoReturn: ...
   def DeleteHostSpecification(self, host: HostSystem) -> NoReturn: ...
   def GetUpdatedHosts(self, startChangeID: Optional[str], endChangeID: Optional[str]) -> list[HostSystem]: ...
