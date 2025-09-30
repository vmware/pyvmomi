# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.VmomiSupport import ManagedObject

from pyVmomi.vim.HostSystem import HostSystem

from pyVmomi.vim.profile.host.HostSpecification import HostSpecification

from pyVmomi.vim.profile.host.HostSubSpecification import HostSubSpecification

class HostSpecificationManager(ManagedObject):
   def UpdateHostSpecification(self, host: HostSystem, hostSpec: HostSpecification) -> None: ...
   def UpdateHostSubSpecification(self, host: HostSystem, hostSubSpec: HostSubSpecification) -> None: ...
   def RetrieveHostSpecification(self, host: HostSystem, fromHost: bool) -> HostSpecification: ...
   def DeleteHostSubSpecification(self, host: HostSystem, subSpecName: str) -> None: ...
   def DeleteHostSpecification(self, host: HostSystem) -> None: ...
   def GetUpdatedHosts(self, startChangeID: Optional[str], endChangeID: Optional[str]) -> list[HostSystem]: ...
