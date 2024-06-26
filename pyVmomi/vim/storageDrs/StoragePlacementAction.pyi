# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vim import Datastore
from pyVmomi.vim import VirtualMachine

from pyVmomi.vim.cluster import Action

from pyVmomi.vim.vm import RelocateSpec

class StoragePlacementAction(Action):
   vm: Optional[VirtualMachine] = None
   relocateSpec: RelocateSpec
   destination: Datastore
   spaceUtilBefore: Optional[float] = None
   spaceDemandBefore: Optional[float] = None
   spaceUtilAfter: Optional[float] = None
   spaceDemandAfter: Optional[float] = None
   ioLatencyBefore: Optional[float] = None
