# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vim.Datastore import Datastore

from pyVmomi.vim.VirtualMachine import VirtualMachine

from pyVmomi.vim.cluster.Action import Action

from pyVmomi.vim.vm.RelocateSpec import RelocateSpec

class StoragePlacementAction(Action):
   vm: Optional[VirtualMachine] = None
   relocateSpec: RelocateSpec
   destination: Datastore
   spaceUtilBefore: Optional[float] = None
   spaceDemandBefore: Optional[float] = None
   spaceUtilAfter: Optional[float] = None
   spaceDemandAfter: Optional[float] = None
   ioLatencyBefore: Optional[float] = None
