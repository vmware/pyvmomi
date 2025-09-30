# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vim.Datastore import Datastore

from pyVmomi.vmodl.DynamicData import DynamicData

from pyVmomi.vim.vm.device.VirtualDevice import VirtualDevice

class FaultToleranceVMConfigSpec(DynamicData):
   class FaultToleranceDiskSpec(DynamicData):
      disk: VirtualDevice
      datastore: Datastore

   vmConfig: Optional[Datastore] = None
   disks: list[FaultToleranceDiskSpec] = []
