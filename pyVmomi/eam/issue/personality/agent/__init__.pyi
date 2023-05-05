from pyVmomi import eam


class AwaitingPMRemediation(PMIssue): ...


class BlockedByAgencyOperation(PMIssue): ...


class PMIssue(eam.issue.AgentIssue): ...