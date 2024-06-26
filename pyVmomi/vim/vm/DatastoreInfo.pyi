# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.VmomiSupport import long

from pyVmomi.vim import Datastore

from pyVmomi.vim.vm import TargetInfo

class DatastoreInfo(TargetInfo):
   datastore: Datastore.Summary
   capability: Datastore.Capability
   maxFileSize: long
   maxVirtualDiskCapacity: Optional[long] = None
   maxPhysicalRDMFileSize: Optional[long] = None
   maxVirtualRDMFileSize: Optional[long] = None
   mode: str
   vStorageSupport: Optional[str] = None
