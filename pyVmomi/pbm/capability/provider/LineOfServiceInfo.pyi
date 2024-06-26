# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import ClassVar
from typing import Optional

from pyVmomi.VmomiSupport import Enum

from pyVmomi.pbm import ExtendedElementDescription

from pyVmomi.vmodl import DynamicData

class LineOfServiceInfo(DynamicData):
   class LineOfServiceEnum(Enum):
      INSPECTION: ClassVar['LineOfServiceEnum'] = 'INSPECTION'
      COMPRESSION: ClassVar['LineOfServiceEnum'] = 'COMPRESSION'
      ENCRYPTION: ClassVar['LineOfServiceEnum'] = 'ENCRYPTION'
      REPLICATION: ClassVar['LineOfServiceEnum'] = 'REPLICATION'
      CACHING: ClassVar['LineOfServiceEnum'] = 'CACHING'
      PERSISTENCE: ClassVar['LineOfServiceEnum'] = 'PERSISTENCE'
      DATA_PROVIDER: ClassVar['LineOfServiceEnum'] = 'DATA_PROVIDER'
      DATASTORE_IO_CONTROL: ClassVar['LineOfServiceEnum'] = 'DATASTORE_IO_CONTROL'
      DATA_PROTECTION: ClassVar['LineOfServiceEnum'] = 'DATA_PROTECTION'
      STRETCHED_CLUSTER: ClassVar['LineOfServiceEnum'] = 'STRETCHED_CLUSTER'

   lineOfService: str
   name: ExtendedElementDescription
   description: Optional[ExtendedElementDescription] = None
