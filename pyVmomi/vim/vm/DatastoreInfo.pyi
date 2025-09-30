# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.VmomiSupport import long

from pyVmomi.vim.Datastore import Datastore

from pyVmomi.vim.vm.TargetInfo import TargetInfo

class DatastoreInfo(TargetInfo):
   datastore: Datastore.Summary
   capability: Datastore.Capability
   maxFileSize: long
   maxVirtualDiskCapacity: Optional[long] = None
   maxPhysicalRDMFileSize: Optional[long] = None
   maxVirtualRDMFileSize: Optional[long] = None
   mode: str
   vStorageSupport: Optional[str] = None
   supportedVDiskFormats: list[str] = []
