# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import ClassVar
from typing import Optional

from pyVmomi.VmomiSupport import Enum

from pyVmomi.vmodl import DynamicData

class VsanObjectHealth(DynamicData):
   class VsanObjectHealthState(Enum):
      inaccessible: ClassVar['VsanObjectHealthState'] = 'inaccessible'
      reducedavailabilitywithnorebuild: ClassVar['VsanObjectHealthState'] = 'reducedavailabilitywithnorebuild'
      reducedavailabilitywithnorebuilddelaytimer: ClassVar['VsanObjectHealthState'] = 'reducedavailabilitywithnorebuilddelaytimer'
      reducedavailabilitywithactiverebuild: ClassVar['VsanObjectHealthState'] = 'reducedavailabilitywithactiverebuild'
      datamove: ClassVar['VsanObjectHealthState'] = 'datamove'
      nonavailabilityrelatedreconfig: ClassVar['VsanObjectHealthState'] = 'nonavailabilityrelatedreconfig'
      nonavailabilityrelatedincompliance: ClassVar['VsanObjectHealthState'] = 'nonavailabilityrelatedincompliance'
      healthy: ClassVar['VsanObjectHealthState'] = 'healthy'
      reducedavailabilitywithpolicypending: ClassVar['VsanObjectHealthState'] = 'reducedavailabilitywithpolicypending'
      reducedavailabilitywithpolicypendingfailed: ClassVar['VsanObjectHealthState'] = 'reducedavailabilitywithpolicypendingfailed'
      reducedavailabilitywithpausedrebuild: ClassVar['VsanObjectHealthState'] = 'reducedavailabilitywithpausedrebuild'
      nonavailabilityrelatedincompliancewithpolicypending: ClassVar['VsanObjectHealthState'] = 'nonavailabilityrelatedincompliancewithpolicypending'
      nonavailabilityrelatedincompliancewithpolicypendingfailed: ClassVar['VsanObjectHealthState'] = 'nonavailabilityrelatedincompliancewithpolicypendingfailed'
      nonavailabilityrelatedincompliancewithpausedrebuild: ClassVar['VsanObjectHealthState'] = 'nonavailabilityrelatedincompliancewithpausedrebuild'
      remoteAccessible: ClassVar['VsanObjectHealthState'] = 'remoteAccessible'
      VsanObjectHealthState_Unknown: ClassVar['VsanObjectHealthState'] = 'VsanObjectHealthState_Unknown'

   numObjects: int
   health: Optional[str] = None
   objUuids: list[str] = []
   vsanClusterUuid: Optional[str] = None
