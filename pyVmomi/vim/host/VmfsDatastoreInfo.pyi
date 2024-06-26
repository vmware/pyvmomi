# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.VmomiSupport import long

from pyVmomi.vim import Datastore

from pyVmomi.vim.host import VmfsVolume

class VmfsDatastoreInfo(Datastore.Info):
   maxPhysicalRDMFileSize: long
   maxVirtualRDMFileSize: long
   vmfs: Optional[VmfsVolume] = None
