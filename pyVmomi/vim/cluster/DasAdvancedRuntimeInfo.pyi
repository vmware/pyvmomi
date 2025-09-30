# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vim.Datastore import Datastore

from pyVmomi.vim.HostSystem import HostSystem

from pyVmomi.vmodl.DynamicData import DynamicData

from pyVmomi.vim.cluster.DasHostInfo import DasHostInfo

class DasAdvancedRuntimeInfo(DynamicData):
   class VmcpCapabilityInfo(DynamicData):
      storageAPDSupported: bool
      storagePDLSupported: bool

   class HeartbeatDatastoreInfo(DynamicData):
      datastore: Datastore
      hosts: list[HostSystem] = []

   dasHostInfo: Optional[DasHostInfo] = None
   vmcpSupported: Optional[VmcpCapabilityInfo] = None
   heartbeatDatastoreInfo: list[HeartbeatDatastoreInfo] = []
