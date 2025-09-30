# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vim.Datastore import Datastore

from pyVmomi.vmodl.DynamicData import DynamicData

from pyVmomi.sms.storage.BackingStoragePool import BackingStoragePool

class DatastoreBackingPoolMapping(DynamicData):
   datastore: list[Datastore] = []
   backingStoragePool: list[BackingStoragePool] = []
