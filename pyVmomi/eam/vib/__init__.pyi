from typing import List
from pyVmomi import eam, vmodl
from datetime import datetime


class VibInfo(vmodl.DynamicData):
    @property
    def id(self) -> str: ...
    @id.setter
    def id(self, value: str):
        self._id = value
    @property
    def name(self) -> str: ...
    @name.setter
    def name(self, value: str):
        self._name = value
    @property
    def version(self) -> str: ...
    @version.setter
    def version(self, value: str):
        self._version = value
    @property
    def vendor(self) -> str: ...
    @vendor.setter
    def vendor(self, value: str):
        self._vendor = value
    @property
    def summary(self) -> str: ...
    @summary.setter
    def summary(self, value: str):
        self._summary = value
    @property
    def softwareTags(self) -> VibInfo.SoftwareTags: ...
    @softwareTags.setter
    def softwareTags(self, value: VibInfo.SoftwareTags):
        self._softwareTags = value
    @property
    def releaseDate(self) -> datetime: ...
    @releaseDate.setter
    def releaseDate(self, value: datetime):
        self._releaseDate = value


    class SoftwareTags(vmodl.DynamicData):
        @property
        def tags(self) -> List[str]: ...
        @tags.setter
        def tags(self, value: List[str]):
            self._tags = value


class VibServices():


    class AnyCertificate(VibServices.SslTrust): ...


    class PinnedPemCertificate(VibServices.SslTrust):
        @property
        def sslCertificate(self) -> str: ...
        @sslCertificate.setter
        def sslCertificate(self, value: str):
            self._sslCertificate = value


    class SslTrust(vmodl.DynamicData): ...