# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vmodl.DynamicData import DynamicData

from pyVmomi.vim.host.HostBusAdapter import HostBusAdapter

from pyVmomi.vim.host.NvmeController import NvmeController

class NvmeTopology(DynamicData):
   class Interface(DynamicData):
      key: str
      adapter: HostBusAdapter
      connectedController: list[NvmeController] = []

   adapter: list[Interface] = []
