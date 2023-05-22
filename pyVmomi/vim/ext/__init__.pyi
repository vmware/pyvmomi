from typing import List
from pyVmomi import vim, vmodl


class ExtendedProductInfo(vmodl.DynamicData):
    @property
    def companyUrl(self) -> str: ...
    @companyUrl.setter
    def companyUrl(self, value: str):
        self._companyUrl = value
    @property
    def productUrl(self) -> str: ...
    @productUrl.setter
    def productUrl(self, value: str):
        self._productUrl = value
    @property
    def managementUrl(self) -> str: ...
    @managementUrl.setter
    def managementUrl(self, value: str):
        self._managementUrl = value
    @property
    def self(self) -> vim.ManagedEntity: ...
    @self.setter
    def self(self, value: vim.ManagedEntity):
        self._self = value


class ManagedByInfo(vmodl.DynamicData):
    @property
    def extensionKey(self) -> str: ...
    @extensionKey.setter
    def extensionKey(self, value: str):
        self._extensionKey = value
    @property
    def type(self) -> str: ...
    @type.setter
    def type(self, value: str):
        self._type = value


class ManagedEntityInfo(vmodl.DynamicData):
    @property
    def type(self) -> str: ...
    @type.setter
    def type(self, value: str):
        self._type = value
    @property
    def smallIconUrl(self) -> str: ...
    @smallIconUrl.setter
    def smallIconUrl(self, value: str):
        self._smallIconUrl = value
    @property
    def iconUrl(self) -> str: ...
    @iconUrl.setter
    def iconUrl(self, value: str):
        self._iconUrl = value
    @property
    def description(self) -> str: ...
    @description.setter
    def description(self, value: str):
        self._description = value


class SolutionManagerInfo(vmodl.DynamicData):
    @property
    def tab(self) -> List[SolutionManagerInfo.TabInfo]: ...
    @tab.setter
    def tab(self, value: List[SolutionManagerInfo.TabInfo]):
        self._tab = value
    @property
    def smallIconUrl(self) -> str: ...
    @smallIconUrl.setter
    def smallIconUrl(self, value: str):
        self._smallIconUrl = value


    class TabInfo(vmodl.DynamicData):
        @property
        def label(self) -> str: ...
        @label.setter
        def label(self, value: str):
            self._label = value
        @property
        def url(self) -> str: ...
        @url.setter
        def url(self, value: str):
            self._url = value