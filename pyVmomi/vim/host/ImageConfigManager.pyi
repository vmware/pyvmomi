# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from datetime import datetime

from typing import ClassVar
from typing import Optional

from pyVmomi.VmomiSupport import Enum
from pyVmomi.VmomiSupport import ManagedObject

from pyVmomi.vmodl.DynamicData import DynamicData

from pyVmomi.vim.host.SoftwarePackage import SoftwarePackage

class ImageConfigManager(ManagedObject):
   class AcceptanceLevel(Enum):
      vmware_certified: ClassVar['AcceptanceLevel'] = 'vmware_certified'
      vmware_accepted: ClassVar['AcceptanceLevel'] = 'vmware_accepted'
      partner: ClassVar['AcceptanceLevel'] = 'partner'
      community: ClassVar['AcceptanceLevel'] = 'community'

   class ImageProfileSummary(DynamicData):
      name: str
      vendor: str

   def QueryHostAcceptanceLevel(self) -> str: ...
   def QueryHostImageProfile(self) -> ImageProfileSummary: ...
   def UpdateAcceptanceLevel(self, newAcceptanceLevel: str) -> None: ...
   def FetchSoftwarePackages(self) -> list[SoftwarePackage]: ...
   def InstallDate(self) -> datetime: ...
