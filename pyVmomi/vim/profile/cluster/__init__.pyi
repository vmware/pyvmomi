from typing import List
from enum import Enum
from pyVmomi import vim
from pyVmomi.VmomiSupport import NoneType


class ClusterProfile(vim.profile.Profile):
    def Update(self, config: ClusterProfile.ConfigSpec) -> NoneType: ...


    class CompleteConfigSpec(ClusterProfile.ConfigSpec):
        @property
        def complyProfile(self) -> vim.profile.ComplianceProfile: ...
        @complyProfile.setter
        def complyProfile(self, value: vim.profile.ComplianceProfile):
            self._complyProfile = value


    class ConfigInfo(vim.profile.Profile.ConfigInfo):
        @property
        def complyProfile(self) -> vim.profile.ComplianceProfile: ...
        @complyProfile.setter
        def complyProfile(self, value: vim.profile.ComplianceProfile):
            self._complyProfile = value


    class ConfigServiceCreateSpec(ClusterProfile.ConfigSpec):
        @property
        def serviceType(self) -> List[str]: ...
        @serviceType.setter
        def serviceType(self, value: List[str]):
            self._serviceType = value


    class ConfigSpec(ClusterProfile.CreateSpec): ...


    class CreateSpec(vim.profile.Profile.CreateSpec): ...


    class ServiceType(Enum):
        DRS = "DRS"
        HA = "HA"
        DPM = "DPM"
        FT = "FT"


class ProfileManager(vim.profile.ProfileManager): ...