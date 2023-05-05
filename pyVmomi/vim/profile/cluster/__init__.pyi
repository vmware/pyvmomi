from typing import List
from enum import Enum
from pyVmomi import vim
from pyVmomi.VmomiSupport import NoneType


class ClusterProfile(vim.profile.Profile):
    def Update(self, config: ClusterProfile.ConfigSpec) -> NoneType: ...


    class CompleteConfigSpec(ClusterProfile.ConfigSpec):
        @property
        def complyProfile(self) -> vim.profile.ComplianceProfile: ...


    class ConfigInfo(vim.profile.Profile.ConfigInfo):
        @property
        def complyProfile(self) -> vim.profile.ComplianceProfile: ...


    class ConfigServiceCreateSpec(ClusterProfile.ConfigSpec):
        @property
        def serviceType(self) -> List[str]: ...


    class ConfigSpec(ClusterProfile.CreateSpec): ...


    class CreateSpec(vim.profile.Profile.CreateSpec): ...


    class ServiceType(Enum):
        DRS = "drs"
        HA = "ha"
        DPM = "dpm"
        FT = "ft"


class ProfileManager(vim.profile.ProfileManager): ...