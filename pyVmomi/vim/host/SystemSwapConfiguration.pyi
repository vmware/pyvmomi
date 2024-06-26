# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vmodl import DynamicData

class SystemSwapConfiguration(DynamicData):
   class SystemSwapOption(DynamicData):
      key: int

   class DisabledOption(SystemSwapOption):
      pass

   class HostCacheOption(SystemSwapOption):
      pass

   class HostLocalSwapOption(SystemSwapOption):
      pass

   class DatastoreOption(SystemSwapOption):
      datastore: str

   option: list[SystemSwapOption] = []
