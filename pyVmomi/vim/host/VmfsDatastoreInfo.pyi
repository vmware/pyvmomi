# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.VmomiSupport import long

from pyVmomi.vim.Datastore import Datastore

from pyVmomi.vim.host.VmfsVolume import VmfsVolume

class VmfsDatastoreInfo(Datastore.Info):
   maxPhysicalRDMFileSize: long
   maxVirtualRDMFileSize: long
   vmfs: Optional[VmfsVolume] = None
