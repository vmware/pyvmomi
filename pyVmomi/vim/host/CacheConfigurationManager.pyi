# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.VmomiSupport import ManagedObject
from pyVmomi.VmomiSupport import long

from pyVmomi.vim import Datastore
from pyVmomi.vim import Task

from pyVmomi.vmodl import DynamicData

class CacheConfigurationManager(ManagedObject):
   class CacheConfigurationSpec(DynamicData):
      datastore: Datastore
      swapSize: long

   class CacheConfigurationInfo(DynamicData):
      key: Datastore
      swapSize: long

   @property
   def cacheConfigurationInfo(self) -> list[CacheConfigurationInfo]: ...

   def ConfigureCache(self, spec: CacheConfigurationSpec) -> Task: ...
