# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import ClassVar
from typing import Optional

from pyVmomi.VmomiSupport import Enum
from pyVmomi.VmomiSupport import ManagedObject

from pyVmomi.vmodl import DynamicData

class Action(DynamicData):
   class ActionType(Enum):
      MigrationV1: ClassVar['ActionType'] = 'MigrationV1'
      VmPowerV1: ClassVar['ActionType'] = 'VmPowerV1'
      HostPowerV1: ClassVar['ActionType'] = 'HostPowerV1'
      IncreaseLimitV1: ClassVar['ActionType'] = 'IncreaseLimitV1'
      IncreaseSizeV1: ClassVar['ActionType'] = 'IncreaseSizeV1'
      IncreaseSharesV1: ClassVar['ActionType'] = 'IncreaseSharesV1'
      IncreaseReservationV1: ClassVar['ActionType'] = 'IncreaseReservationV1'
      DecreaseOthersReservationV1: ClassVar['ActionType'] = 'DecreaseOthersReservationV1'
      IncreaseClusterCapacityV1: ClassVar['ActionType'] = 'IncreaseClusterCapacityV1'
      DecreaseMigrationThresholdV1: ClassVar['ActionType'] = 'DecreaseMigrationThresholdV1'
      HostMaintenanceV1: ClassVar['ActionType'] = 'HostMaintenanceV1'
      StorageMigrationV1: ClassVar['ActionType'] = 'StorageMigrationV1'
      StoragePlacementV1: ClassVar['ActionType'] = 'StoragePlacementV1'
      PlacementV1: ClassVar['ActionType'] = 'PlacementV1'
      HostInfraUpdateHaV1: ClassVar['ActionType'] = 'HostInfraUpdateHaV1'

   type: str
   target: Optional[ManagedObject] = None
