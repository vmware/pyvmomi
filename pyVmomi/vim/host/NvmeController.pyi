# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vmodl import DynamicData

from pyVmomi.vim.host import HostBusAdapter
from pyVmomi.vim.host import NvmeNamespace

class NvmeController(DynamicData):
   key: str
   controllerNumber: int
   subnqn: str
   name: str
   associatedAdapter: HostBusAdapter
   transportType: str
   fusedOperationSupported: bool
   numberOfQueues: int
   queueSize: int
   attachedNamespace: list[NvmeNamespace] = []
   vendorId: Optional[str] = None
   model: Optional[str] = None
   serialNumber: Optional[str] = None
   firmwareVersion: Optional[str] = None
