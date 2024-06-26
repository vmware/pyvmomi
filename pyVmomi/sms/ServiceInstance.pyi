# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from pyVmomi.VmomiSupport import ManagedObject

from pyVmomi.sms import AboutInfo
from pyVmomi.sms import StorageManager

from pyVmomi.sms.auth import SessionManager

class ServiceInstance(ManagedObject):
   def QueryStorageManager(self) -> StorageManager: ...
   def QuerySessionManager(self) -> SessionManager: ...
   def QueryAboutInfo(self) -> AboutInfo: ...
