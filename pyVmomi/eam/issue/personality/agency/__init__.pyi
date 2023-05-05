from typing import List
from pyVmomi import eam, vim


class CannotConfigureSolutions(PMIssue):
    @property
    def cr(self) -> vim.ComputeResource: ...
    @property
    def solutionsToModify(self) -> List[str]: ...
    @property
    def solutionsToRemove(self) -> List[str]: ...


class CannotUploadDepot(DepotIssue):
    @property
    def localDepotUrl(self) -> str: ...


class DepotIssue(PMIssue):
    @property
    def remoteDepotUrl(self) -> str: ...


class InaccessibleDepot(DepotIssue): ...


class InvalidDepot(DepotIssue): ...


class PMIssue(eam.issue.AgencyIssue): ...


class PMUnavailable(PMIssue): ...