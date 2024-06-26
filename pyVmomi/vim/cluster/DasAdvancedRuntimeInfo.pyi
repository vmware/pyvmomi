# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vim import Datastore
from pyVmomi.vim import HostSystem

from pyVmomi.vmodl import DynamicData

from pyVmomi.vim.cluster import DasHostInfo

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
