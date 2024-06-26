# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import ClassVar
from typing import Optional

from pyVmomi.VmomiSupport import Enum

from pyVmomi.vmodl import DynamicData

class EntityReference(DynamicData):
   class EntityType(Enum):
      datacenter: ClassVar['EntityType'] = 'datacenter'
      resourcePool: ClassVar['EntityType'] = 'resourcePool'
      storagePod: ClassVar['EntityType'] = 'storagePod'
      cluster: ClassVar['EntityType'] = 'cluster'
      vm: ClassVar['EntityType'] = 'vm'
      datastore: ClassVar['EntityType'] = 'datastore'
      host: ClassVar['EntityType'] = 'host'
      vmFile: ClassVar['EntityType'] = 'vmFile'
      scsiPath: ClassVar['EntityType'] = 'scsiPath'
      scsiTarget: ClassVar['EntityType'] = 'scsiTarget'
      scsiVolume: ClassVar['EntityType'] = 'scsiVolume'
      scsiAdapter: ClassVar['EntityType'] = 'scsiAdapter'
      nasMount: ClassVar['EntityType'] = 'nasMount'

   id: str
   type: Optional[EntityType] = None
