from pyVmomi import vmodl


class ConfigInfo(vmodl.DynamicData):
    @property
    def enabled(self) -> bool: ...
    @enabled.setter
    def enabled(self, value: bool):
        self._enabled = value
    @property
    def defaultConfig(self) -> ConfigInfo.HostDefaultInfo: ...
    @defaultConfig.setter
    def defaultConfig(self, value: ConfigInfo.HostDefaultInfo):
        self._defaultConfig = value
    @property
    def vsanEsaEnabled(self) -> bool: ...
    @vsanEsaEnabled.setter
    def vsanEsaEnabled(self, value: bool):
        self._vsanEsaEnabled = value


    class HostDefaultInfo(vmodl.DynamicData):
        @property
        def uuid(self) -> str: ...
        @uuid.setter
        def uuid(self, value: str):
            self._uuid = value
        @property
        def autoClaimStorage(self) -> bool: ...
        @autoClaimStorage.setter
        def autoClaimStorage(self, value: bool):
            self._autoClaimStorage = value
        @property
        def checksumEnabled(self) -> bool: ...
        @checksumEnabled.setter
        def checksumEnabled(self, value: bool):
            self._checksumEnabled = value