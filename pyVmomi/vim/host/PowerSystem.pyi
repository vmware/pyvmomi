# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import NoReturn

from pyVmomi.VmomiSupport import ManagedObject

from pyVmomi.vmodl import DynamicData

class PowerSystem(ManagedObject):
   class PowerPolicy(DynamicData):
      key: int
      name: str
      shortName: str
      description: str

   class Capability(DynamicData):
      availablePolicy: list[PowerPolicy] = []

   class Info(DynamicData):
      currentPolicy: PowerPolicy

   @property
   def capability(self) -> Capability: ...
   @property
   def info(self) -> Info: ...

   def ConfigurePolicy(self, key: int) -> NoReturn: ...
