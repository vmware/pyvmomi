# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import ClassVar
from typing import Optional

from pyVmomi.VmomiSupport import Enum

from pyVmomi.vim.Datastore import Datastore

from pyVmomi.vmodl.DynamicData import DynamicData

from pyVmomi.vim.cluster.DasAdmissionControlPolicy import DasAdmissionControlPolicy

from pyVmomi.vim.cluster.DasVmSettings import DasVmSettings

from pyVmomi.vim.option.OptionValue import OptionValue

class DasConfigInfo(DynamicData):
   class ServiceState(Enum):
      disabled: ClassVar['ServiceState'] = 'disabled'
      enabled: ClassVar['ServiceState'] = 'enabled'

   class VmMonitoringState(Enum):
      vmMonitoringDisabled: ClassVar['VmMonitoringState'] = 'vmMonitoringDisabled'
      vmMonitoringOnly: ClassVar['VmMonitoringState'] = 'vmMonitoringOnly'
      vmAndAppMonitoring: ClassVar['VmMonitoringState'] = 'vmAndAppMonitoring'

   class HBDatastoreCandidate(Enum):
      userSelectedDs: ClassVar['HBDatastoreCandidate'] = 'userSelectedDs'
      allFeasibleDs: ClassVar['HBDatastoreCandidate'] = 'allFeasibleDs'
      allFeasibleDsWithUserPreference: ClassVar['HBDatastoreCandidate'] = 'allFeasibleDsWithUserPreference'

   enabled: Optional[bool] = None
   vmMonitoring: Optional[str] = None
   hostMonitoring: Optional[str] = None
   vmComponentProtecting: Optional[str] = None
   failoverLevel: Optional[int] = None
   admissionControlPolicy: Optional[DasAdmissionControlPolicy] = None
   admissionControlEnabled: Optional[bool] = None
   defaultVmSettings: Optional[DasVmSettings] = None
   option: list[OptionValue] = []
   heartbeatDatastore: list[Datastore] = []
   hBDatastoreCandidatePolicy: Optional[str] = None
