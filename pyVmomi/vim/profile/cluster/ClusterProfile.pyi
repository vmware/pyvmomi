# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import ClassVar
from typing import NoReturn
from typing import Optional

from pyVmomi.VmomiSupport import Enum

from pyVmomi.vim.profile import ComplianceProfile
from pyVmomi.vim.profile import Profile

class ClusterProfile(Profile):
   class ConfigInfo(Profile.ConfigInfo):
      complyProfile: Optional[ComplianceProfile] = None

   class CreateSpec(Profile.CreateSpec):
      pass

   class ConfigSpec(CreateSpec):
      pass

   class CompleteConfigSpec(ConfigSpec):
      complyProfile: Optional[ComplianceProfile] = None

   class ServiceType(Enum):
      DRS: ClassVar['ServiceType'] = 'DRS'
      HA: ClassVar['ServiceType'] = 'HA'
      DPM: ClassVar['ServiceType'] = 'DPM'
      FT: ClassVar['ServiceType'] = 'FT'

   class ConfigServiceCreateSpec(ConfigSpec):
      serviceType: list[str] = []

   def Update(self, config: ConfigSpec) -> NoReturn: ...
