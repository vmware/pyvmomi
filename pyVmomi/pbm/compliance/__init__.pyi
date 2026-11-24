# Copyright (c) 2006-2026 Broadcom. All Rights Reserved.
# The term "Broadcom" refers to Broadcom Inc. and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

import datetime as _datetime
import typing as _typing
import pyVmomi.VmomiSupport
import pyVmomi.pbm
import pyVmomi.vmodl
import pyVmomi.pbm.capability
import pyVmomi.pbm.profile



class ComplianceManager(pyVmomi.VmomiSupport.ManagedObject):
   def CheckCompliance(self, entities: list[pyVmomi.pbm.ServerObjectRef], profile: _typing.Optional[pyVmomi.pbm.profile.ProfileId]) -> list[ComplianceResult]: ...
   def FetchComplianceResult(self, entities: list[pyVmomi.pbm.ServerObjectRef], profile: _typing.Optional[pyVmomi.pbm.profile.ProfileId]) -> list[ComplianceResult]: ...
   def CheckRollupCompliance(self, entity: list[pyVmomi.pbm.ServerObjectRef]) -> list[RollupComplianceResult]: ...
   def FetchRollupComplianceResult(self, entity: list[pyVmomi.pbm.ServerObjectRef]) -> list[RollupComplianceResult]: ...
   def QueryByRollupComplianceStatus(self, status: str) -> list[pyVmomi.pbm.ServerObjectRef]: ...


class ComplianceResult(pyVmomi.vmodl.DynamicData):
   class ComplianceStatus(pyVmomi.VmomiSupport.Enum):
      compliant: _typing.ClassVar['ComplianceStatus'] = 'compliant'
      nonCompliant: _typing.ClassVar['ComplianceStatus'] = 'nonCompliant'
      unknown: _typing.ClassVar['ComplianceStatus'] = 'unknown'
      notApplicable: _typing.ClassVar['ComplianceStatus'] = 'notApplicable'
      outOfDate: _typing.ClassVar['ComplianceStatus'] = 'outOfDate'

   class ComplianceTaskStatus(pyVmomi.VmomiSupport.Enum):
      inProgress: _typing.ClassVar['ComplianceTaskStatus'] = 'inProgress'
      success: _typing.ClassVar['ComplianceTaskStatus'] = 'success'
      failed: _typing.ClassVar['ComplianceTaskStatus'] = 'failed'

   checkTime: _datetime.datetime
   entity: pyVmomi.pbm.ServerObjectRef
   profile: _typing.Optional[pyVmomi.pbm.profile.ProfileId] = None
   complianceTaskStatus: _typing.Optional[str] = None
   complianceStatus: str
   mismatch: bool
   violatedPolicies: list[PolicyStatus] = []
   errorCause: list[pyVmomi.vmodl.MethodFault] = []
   operationalStatus: _typing.Optional[OperationalStatus] = None
   info: _typing.Optional[pyVmomi.pbm.ExtendedElementDescription] = None


class FetchEntityHealthStatusSpec(pyVmomi.vmodl.DynamicData):
   objectRef: pyVmomi.pbm.ServerObjectRef
   backingId: _typing.Optional[str] = None


class OperationalStatus(pyVmomi.vmodl.DynamicData):
   healthy: _typing.Optional[bool] = None
   operationETA: _typing.Optional[_datetime.datetime] = None
   operationProgress: _typing.Optional[pyVmomi.VmomiSupport.long] = None
   transitional: _typing.Optional[bool] = None


class PolicyStatus(pyVmomi.vmodl.DynamicData):
   expectedValue: pyVmomi.pbm.capability.CapabilityInstance
   currentValue: _typing.Optional[pyVmomi.pbm.capability.CapabilityInstance] = None


class RollupComplianceResult(pyVmomi.vmodl.DynamicData):
   oldestCheckTime: _datetime.datetime
   entity: pyVmomi.pbm.ServerObjectRef
   overallComplianceStatus: str
   overallComplianceTaskStatus: _typing.Optional[str] = None
   result: list[ComplianceResult] = []
   errorCause: list[pyVmomi.vmodl.MethodFault] = []
   profileMismatch: bool
