# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.VmomiSupport import ManagedObject

from pyVmomi.vmodl import DynamicData

class ServiceManager(ManagedObject):
   class ServiceInfo(DynamicData):
      serviceName: str
      location: list[str] = []
      service: ManagedObject
      description: str

   @property
   def service(self) -> list[ServiceInfo]: ...

   def QueryServiceList(self, serviceName: Optional[str], location: list[str]) -> list[ServiceInfo]: ...
