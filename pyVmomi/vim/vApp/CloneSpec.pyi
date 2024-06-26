# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import ClassVar
from typing import Optional

from pyVmomi.VmomiSupport import Enum

from pyVmomi.vim import Datastore
from pyVmomi.vim import Folder
from pyVmomi.vim import HostSystem
from pyVmomi.vim import KeyValue
from pyVmomi.vim import ManagedEntity
from pyVmomi.vim import Network
from pyVmomi.vim import ResourceConfigSpec
from pyVmomi.vim import ResourcePool

from pyVmomi.vmodl import DynamicData

class CloneSpec(DynamicData):
   class NetworkMappingPair(DynamicData):
      source: Network
      destination: Network

   class ResourceMap(DynamicData):
      source: ManagedEntity
      parent: Optional[ResourcePool] = None
      resourceSpec: Optional[ResourceConfigSpec] = None
      location: Optional[Datastore] = None

   class ProvisioningType(Enum):
      sameAsSource: ClassVar['ProvisioningType'] = 'sameAsSource'
      thin: ClassVar['ProvisioningType'] = 'thin'
      thick: ClassVar['ProvisioningType'] = 'thick'

   location: Datastore
   host: Optional[HostSystem] = None
   resourceSpec: Optional[ResourceConfigSpec] = None
   vmFolder: Optional[Folder] = None
   networkMapping: list[NetworkMappingPair] = []
   property: list[KeyValue] = []
   resourceMapping: list[ResourceMap] = []
   provisioning: Optional[str] = None
