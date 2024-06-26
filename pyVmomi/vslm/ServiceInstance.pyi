# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from pyVmomi.VmomiSupport import ManagedObject

from pyVmomi.vslm import ServiceInstanceContent

class ServiceInstance(ManagedObject):
   @property
   def content(self) -> ServiceInstanceContent: ...

   def RetrieveContent(self) -> ServiceInstanceContent: ...
