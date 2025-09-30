# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vmodl.DynamicData import DynamicData

from pyVmomi.vim.host.HostBusAdapter import HostBusAdapter

from pyVmomi.vim.host.MultipathInfo import MultipathInfo

from pyVmomi.vim.host.NvmeTopology import NvmeTopology

from pyVmomi.vim.host.PlugStoreTopology import PlugStoreTopology

from pyVmomi.vim.host.ScsiLun import ScsiLun

from pyVmomi.vim.host.ScsiTopology import ScsiTopology

class StorageDeviceInfo(DynamicData):
   hostBusAdapter: list[HostBusAdapter] = []
   scsiLun: list[ScsiLun] = []
   scsiTopology: Optional[ScsiTopology] = None
   nvmeTopology: Optional[NvmeTopology] = None
   multipathInfo: Optional[MultipathInfo] = None
   plugStoreTopology: Optional[PlugStoreTopology] = None
   softwareInternetScsiEnabled: bool
