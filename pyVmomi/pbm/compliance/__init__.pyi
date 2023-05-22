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
    @checkTime.setter
    def checkTime(self, value: datetime):
        self._checkTime = value
    @property
    def entity(self) -> pbm.ServerObjectRef: ...
    @entity.setter
    def entity(self, value: pbm.ServerObjectRef):
        self._entity = value
    @property
    def profile(self) -> pbm.profile.ProfileId: ...
    @profile.setter
    def profile(self, value: pbm.profile.ProfileId):
        self._profile = value
    @property
    def complianceTaskStatus(self) -> str: ...
    @complianceTaskStatus.setter
    def complianceTaskStatus(self, value: str):
        self._complianceTaskStatus = value
    @property
    def complianceStatus(self) -> str: ...
    @complianceStatus.setter
    def complianceStatus(self, value: str):
        self._complianceStatus = value
    @property
    def mismatch(self) -> bool: ...
    @mismatch.setter
    def mismatch(self, value: bool):
        self._mismatch = value
    @property
    def violatedPolicies(self) -> List[PolicyStatus]: ...
    @violatedPolicies.setter
    def violatedPolicies(self, value: List[PolicyStatus]):
        self._violatedPolicies = value
    @property
    def errorCause(self) -> List[vmodl.MethodFault]: ...
    @errorCause.setter
    def errorCause(self, value: List[vmodl.MethodFault]):
        self._errorCause = value
    @property
    def operationalStatus(self) -> OperationalStatus: ...
    @operationalStatus.setter
    def operationalStatus(self, value: OperationalStatus):
        self._operationalStatus = value
    @property
    def info(self) -> pbm.ExtendedElementDescription: ...
    @info.setter
    def info(self, value: pbm.ExtendedElementDescription):
        self._info = value


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
    @objectRef.setter
    def objectRef(self, value: pbm.ServerObjectRef):
        self._objectRef = value
    @property
    def backingId(self) -> str: ...
    @backingId.setter
    def backingId(self, value: str):
        self._backingId = value


class OperationalStatus(vmodl.DynamicData):
    @property
    def healthy(self) -> bool: ...
    @healthy.setter
    def healthy(self, value: bool):
        self._healthy = value
    @property
    def operationETA(self) -> datetime: ...
    @operationETA.setter
    def operationETA(self, value: datetime):
        self._operationETA = value
    @property
    def operationProgress(self) -> long: ...
    @operationProgress.setter
    def operationProgress(self, value: long):
        self._operationProgress = value
    @property
    def transitional(self) -> bool: ...
    @transitional.setter
    def transitional(self, value: bool):
        self._transitional = value


class PolicyStatus(vmodl.DynamicData):
    @property
    def expectedValue(self) -> pbm.capability.CapabilityInstance: ...
    @expectedValue.setter
    def expectedValue(self, value: pbm.capability.CapabilityInstance):
        self._expectedValue = value
    @property
    def currentValue(self) -> pbm.capability.CapabilityInstance: ...
    @currentValue.setter
    def currentValue(self, value: pbm.capability.CapabilityInstance):
        self._currentValue = value


class RollupComplianceResult(vmodl.DynamicData):
    @property
    def oldestCheckTime(self) -> datetime: ...
    @oldestCheckTime.setter
    def oldestCheckTime(self, value: datetime):
        self._oldestCheckTime = value
    @property
    def entity(self) -> pbm.ServerObjectRef: ...
    @entity.setter
    def entity(self, value: pbm.ServerObjectRef):
        self._entity = value
    @property
    def overallComplianceStatus(self) -> str: ...
    @overallComplianceStatus.setter
    def overallComplianceStatus(self, value: str):
        self._overallComplianceStatus = value
    @property
    def overallComplianceTaskStatus(self) -> str: ...
    @overallComplianceTaskStatus.setter
    def overallComplianceTaskStatus(self, value: str):
        self._overallComplianceTaskStatus = value
    @property
    def result(self) -> List[ComplianceResult]: ...
    @result.setter
    def result(self, value: List[ComplianceResult]):
        self._result = value
    @property
    def errorCause(self) -> List[vmodl.MethodFault]: ...
    @errorCause.setter
    def errorCause(self, value: List[vmodl.MethodFault]):
        self._errorCause = value
    @property
    def profileMismatch(self) -> bool: ...
    @profileMismatch.setter
    def profileMismatch(self, value: bool):
        self._profileMismatch = value


class EntityHealthStatus():


    class HealthStatus(Enum):
        red = "red"
        yellow = "yellow"
        green = "green"
        unknown = "unknown"