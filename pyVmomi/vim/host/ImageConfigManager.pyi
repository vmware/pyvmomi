# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from datetime import datetime

from typing import ClassVar
from typing import NoReturn
from typing import Optional

from pyVmomi.VmomiSupport import Enum
from pyVmomi.VmomiSupport import ManagedObject

from pyVmomi.vmodl import DynamicData

from pyVmomi.vim.host import SoftwarePackage

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
   def UpdateAcceptanceLevel(self, newAcceptanceLevel: str) -> NoReturn: ...
   def FetchSoftwarePackages(self) -> list[SoftwarePackage]: ...
   def InstallDate(self) -> datetime: ...
