# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from datetime import datetime

from typing import Optional

from pyVmomi.VmomiSupport import long

from pyVmomi.vim import Datastore

from pyVmomi.vmodl import DynamicData

class StorageInfo(DynamicData):
   class UsageOnDatastore(DynamicData):
      datastore: Datastore
      committed: long
      uncommitted: long
      unshared: long

   perDatastoreUsage: list[UsageOnDatastore] = []
   timestamp: datetime
