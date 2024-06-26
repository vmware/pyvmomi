# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import ClassVar
from typing import Optional

from pyVmomi.VmomiSupport import Enum

from pyVmomi.vim import HostSystem

from pyVmomi.vmodl import DynamicData

class ProtocolEndpoint(DynamicData):
   class PEType(Enum):
      block: ClassVar['PEType'] = 'block'
      nas: ClassVar['PEType'] = 'nas'

   class ProtocolEndpointType(Enum):
      scsi: ClassVar['ProtocolEndpointType'] = 'scsi'
      nfs: ClassVar['ProtocolEndpointType'] = 'nfs'
      nfs4x: ClassVar['ProtocolEndpointType'] = 'nfs4x'

   peType: str
   type: Optional[str] = None
   uuid: str
   hostKey: list[HostSystem] = []
   storageArray: Optional[str] = None
   nfsServer: Optional[str] = None
   nfsDir: Optional[str] = None
   nfsServerScope: Optional[str] = None
   nfsServerMajor: Optional[str] = None
   nfsServerAuthType: Optional[str] = None
   nfsServerUser: Optional[str] = None
   deviceId: Optional[str] = None
   usedByStretchedContainer: Optional[bool] = None
