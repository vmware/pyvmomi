# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vmodl import DynamicData

from pyVmomi.vim.host import HostBusAdapter
from pyVmomi.vim.host import MultipathInfo
from pyVmomi.vim.host import NvmeTopology
from pyVmomi.vim.host import PlugStoreTopology
from pyVmomi.vim.host import ScsiLun
from pyVmomi.vim.host import ScsiTopology

class StorageDeviceInfo(DynamicData):
   hostBusAdapter: list[HostBusAdapter] = []
   scsiLun: list[ScsiLun] = []
   scsiTopology: Optional[ScsiTopology] = None
   nvmeTopology: Optional[NvmeTopology] = None
   multipathInfo: Optional[MultipathInfo] = None
   plugStoreTopology: Optional[PlugStoreTopology] = None
   softwareInternetScsiEnabled: bool
