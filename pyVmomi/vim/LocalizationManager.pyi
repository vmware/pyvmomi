# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from datetime import datetime

from typing import Optional

from pyVmomi.VmomiSupport import ManagedObject

from pyVmomi.vmodl import DynamicData

class LocalizationManager(ManagedObject):
   class MessageCatalog(DynamicData):
      moduleName: str
      catalogName: str
      locale: str
      catalogUri: str
      lastModified: Optional[datetime] = None
      md5sum: Optional[str] = None
      version: Optional[str] = None

   @property
   def catalog(self) -> list[MessageCatalog]: ...
