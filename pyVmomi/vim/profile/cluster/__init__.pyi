# Copyright (c) 2006-2026 Broadcom. All Rights Reserved.
# The term "Broadcom" refers to Broadcom Inc. and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

import typing as _typing
import pyVmomi.VmomiSupport
import pyVmomi.vim.profile



class ClusterProfile(pyVmomi.vim.profile.Profile):
   class ConfigInfo(pyVmomi.vim.profile.Profile.ConfigInfo):
      complyProfile: _typing.Optional[pyVmomi.vim.profile.ComplianceProfile] = None

   class CreateSpec(pyVmomi.vim.profile.Profile.CreateSpec):
      pass

   class ConfigSpec(CreateSpec):
      pass

   class CompleteConfigSpec(ConfigSpec):
      complyProfile: _typing.Optional[pyVmomi.vim.profile.ComplianceProfile] = None

   class ServiceType(pyVmomi.VmomiSupport.Enum):
      DRS: _typing.ClassVar['ServiceType'] = 'DRS'
      HA: _typing.ClassVar['ServiceType'] = 'HA'
      DPM: _typing.ClassVar['ServiceType'] = 'DPM'
      FT: _typing.ClassVar['ServiceType'] = 'FT'

   class ConfigServiceCreateSpec(ConfigSpec):
      serviceType: list[str] = []

   def Update(self, config: ConfigSpec) -> None: ...


class ProfileManager(pyVmomi.vim.profile.ProfileManager):
   pass
