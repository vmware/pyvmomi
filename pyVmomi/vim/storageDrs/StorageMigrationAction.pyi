# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.VmomiSupport import long

from pyVmomi.vim import Datastore
from pyVmomi.vim import VirtualMachine

from pyVmomi.vim.cluster import Action

from pyVmomi.vim.vm import RelocateSpec

class StorageMigrationAction(Action):
   vm: VirtualMachine
   relocateSpec: RelocateSpec
   source: Datastore
   destination: Datastore
   sizeTransferred: long
   spaceUtilSrcBefore: Optional[float] = None
   spaceUtilDstBefore: Optional[float] = None
   spaceUtilSrcAfter: Optional[float] = None
   spaceUtilDstAfter: Optional[float] = None
   ioLatencySrcBefore: Optional[float] = None
   ioLatencyDstBefore: Optional[float] = None
