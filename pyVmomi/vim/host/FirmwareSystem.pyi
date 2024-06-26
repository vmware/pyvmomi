# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import NoReturn

from pyVmomi.VmomiSupport import ManagedObject

class FirmwareSystem(ManagedObject):
   def ResetToFactoryDefaults(self) -> NoReturn: ...
   def BackupConfiguration(self) -> str: ...
   def QueryConfigUploadURL(self) -> str: ...
   def RestoreConfiguration(self, force: bool) -> NoReturn: ...
