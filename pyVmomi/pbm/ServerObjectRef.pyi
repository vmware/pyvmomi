# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import ClassVar
from typing import Optional

from pyVmomi.VmomiSupport import Enum

from pyVmomi.vmodl import DynamicData

class ServerObjectRef(DynamicData):
   class VvolType(Enum):
      Config: ClassVar['VvolType'] = 'Config'
      Data: ClassVar['VvolType'] = 'Data'
      Swap: ClassVar['VvolType'] = 'Swap'

   class ObjectType(Enum):
      virtualMachine: ClassVar['ObjectType'] = 'virtualMachine'
      virtualMachineAndDisks: ClassVar['ObjectType'] = 'virtualMachineAndDisks'
      virtualDiskId: ClassVar['ObjectType'] = 'virtualDiskId'
      virtualDiskUUID: ClassVar['ObjectType'] = 'virtualDiskUUID'
      datastore: ClassVar['ObjectType'] = 'datastore'
      vsanObjectId: ClassVar['ObjectType'] = 'vsanObjectId'
      fileShareId: ClassVar['ObjectType'] = 'fileShareId'
      host: ClassVar['ObjectType'] = 'host'
      cluster: ClassVar['ObjectType'] = 'cluster'
      unknown: ClassVar['ObjectType'] = 'unknown'

   objectType: str
   key: str
   serverUuid: Optional[str] = None
