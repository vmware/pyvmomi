from typing import List
from enum import Enum
from pyVmomi import pbm, vmodl
from datetime import datetime
from pyVmomi.VmomiSupport import ManagedObject, long


class ComplianceManager(ManagedObject):
    def CheckCompliance(self, entities: List[pbm.ServerObjectRef], profile: pbm.profile.ProfileId) -> List[ComplianceResult]: ...
    def FetchComplianceResult(self, entities: List[pbm.ServerObjectRef], profile: pbm.profile.ProfileId) -> List[ComplianceResult]: ...
    def CheckRollupCompliance(self, entity: List[pbm.ServerObjectRef]) -> List[RollupComplianceResult]: ...
    def FetchRollupComplianceResult(self, entity: List[pbm.ServerObjectRef]) -> List[RollupComplianceResult]: ...
    def QueryByRollupComplianceStatus(self, status: str) -> List[pbm.ServerObjectRef]: ...


class ComplianceResult(vmodl.DynamicData):
    @property
    def checkTime(self) -> datetime: ...
    @property
    def entity(self) -> pbm.ServerObjectRef: ...
    @property
    def profile(self) -> pbm.profile.ProfileId: ...
    @property
    def complianceTaskStatus(self) -> str: ...
    @property
    def complianceStatus(self) -> str: ...
    @property
    def mismatch(self) -> bool: ...
    @property
    def violatedPolicies(self) -> List[PolicyStatus]: ...
    @property
    def errorCause(self) -> List[vmodl.MethodFault]: ...
    @property
    def operationalStatus(self) -> OperationalStatus: ...
    @property
    def info(self) -> pbm.ExtendedElementDescription: ...


    class ComplianceStatus(Enum):
        compliant = "compliant"
        nonCompliant = "nonCompliant"
        unknown = "unknown"
        notApplicable = "notApplicable"
        outOfDate = "outOfDate"


    class ComplianceTaskStatus(Enum):
        inProgress = "inProgress"
        success = "success"
        failed = "failed"


class FetchEntityHealthStatusSpec(vmodl.DynamicData):
    @property
    def objectRef(self) -> pbm.ServerObjectRef: ...
    @property
    def backingId(self) -> str: ...


class OperationalStatus(vmodl.DynamicData):
    @property
    def healthy(self) -> bool: ...
    @property
    def operationETA(self) -> datetime: ...
    @property
    def operationProgress(self) -> long: ...
    @property
    def transitional(self) -> bool: ...


class PolicyStatus(vmodl.DynamicData):
    @property
    def expectedValue(self) -> pbm.capability.CapabilityInstance: ...
    @property
    def currentValue(self) -> pbm.capability.CapabilityInstance: ...


class RollupComplianceResult(vmodl.DynamicData):
    @property
    def oldestCheckTime(self) -> datetime: ...
    @property
    def entity(self) -> pbm.ServerObjectRef: ...
    @property
    def overallComplianceStatus(self) -> str: ...
    @property
    def overallComplianceTaskStatus(self) -> str: ...
    @property
    def result(self) -> List[ComplianceResult]: ...
    @property
    def errorCause(self) -> List[vmodl.MethodFault]: ...
    @property
    def profileMismatch(self) -> bool: ...


class EntityHealthStatus():


    class HealthStatus(Enum):
        red = "red"
        yellow = "yellow"
        green = "green"
        unknown = "unknown"