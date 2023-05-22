from typing import List
from pyVmomi import eam, vim


class CannotConfigureSolutions(PMIssue):
    @property
    def cr(self) -> vim.ComputeResource: ...
    @cr.setter
    def cr(self, value: vim.ComputeResource):
        self._cr = value
    @property
    def solutionsToModify(self) -> List[str]: ...
    @solutionsToModify.setter
    def solutionsToModify(self, value: List[str]):
        self._solutionsToModify = value
    @property
    def solutionsToRemove(self) -> List[str]: ...
    @solutionsToRemove.setter
    def solutionsToRemove(self, value: List[str]):
        self._solutionsToRemove = value


class CannotUploadDepot(DepotIssue):
    @property
    def localDepotUrl(self) -> str: ...
    @localDepotUrl.setter
    def localDepotUrl(self, value: str):
        self._localDepotUrl = value


class DepotIssue(PMIssue):
    @property
    def remoteDepotUrl(self) -> str: ...
    @remoteDepotUrl.setter
    def remoteDepotUrl(self, value: str):
        self._remoteDepotUrl = value


class InaccessibleDepot(DepotIssue): ...


class InvalidDepot(DepotIssue): ...


class PMIssue(eam.issue.AgencyIssue): ...


class PMUnavailable(PMIssue): ...