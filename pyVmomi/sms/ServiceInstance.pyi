# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from pyVmomi.VmomiSupport import ManagedObject

from pyVmomi.sms.AboutInfo import AboutInfo

from pyVmomi.sms.StorageManager import StorageManager

from pyVmomi.sms.auth.SessionManager import SessionManager

class ServiceInstance(ManagedObject):
   def QueryStorageManager(self) -> StorageManager: ...
   def QuerySessionManager(self) -> SessionManager: ...
   def QueryAboutInfo(self) -> AboutInfo: ...
