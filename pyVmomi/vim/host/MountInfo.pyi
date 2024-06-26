# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import ClassVar
from typing import Optional

from pyVmomi.VmomiSupport import Enum

from pyVmomi.vmodl import DynamicData

class MountInfo(DynamicData):
   class AccessMode(Enum):
      readWrite: ClassVar['AccessMode'] = 'readWrite'
      readOnly: ClassVar['AccessMode'] = 'readOnly'

   class InaccessibleReason(Enum):
      AllPathsDown_Start: ClassVar['InaccessibleReason'] = 'AllPathsDown_Start'
      AllPathsDown_Timeout: ClassVar['InaccessibleReason'] = 'AllPathsDown_Timeout'
      PermanentDeviceLoss: ClassVar['InaccessibleReason'] = 'PermanentDeviceLoss'

   class MountFailedReason(Enum):
      CONNECT_FAILURE: ClassVar['MountFailedReason'] = 'CONNECT_FAILURE'
      MOUNT_NOT_SUPPORTED: ClassVar['MountFailedReason'] = 'MOUNT_NOT_SUPPORTED'
      NFS_NOT_SUPPORTED: ClassVar['MountFailedReason'] = 'NFS_NOT_SUPPORTED'
      MOUNT_DENIED: ClassVar['MountFailedReason'] = 'MOUNT_DENIED'
      MOUNT_NOT_DIR: ClassVar['MountFailedReason'] = 'MOUNT_NOT_DIR'
      VOLUME_LIMIT_EXCEEDED: ClassVar['MountFailedReason'] = 'VOLUME_LIMIT_EXCEEDED'
      CONN_LIMIT_EXCEEDED: ClassVar['MountFailedReason'] = 'CONN_LIMIT_EXCEEDED'
      MOUNT_EXISTS: ClassVar['MountFailedReason'] = 'MOUNT_EXISTS'
      OTHERS: ClassVar['MountFailedReason'] = 'OTHERS'

   path: Optional[str] = None
   accessMode: str
   mounted: Optional[bool] = None
   accessible: Optional[bool] = None
   inaccessibleReason: Optional[str] = None
   vmknicName: Optional[str] = None
   vmknicActive: Optional[bool] = None
   mountFailedReason: Optional[str] = None
   numTcpConnections: Optional[int] = None
