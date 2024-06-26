# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vmodl import DynamicData

class VasaStorageArray(DynamicData):
   class DiscoverySvcInfo(DynamicData):
      portType: str
      svcNqn: str
      ipInfo: Optional[DiscoveryIpTransport] = None
      fcInfo: Optional[DiscoveryFcTransport] = None

   class DiscoveryFcTransport(DynamicData):
      nodeWwn: str
      portWwn: str

   class DiscoveryIpTransport(DynamicData):
      ipAddress: str
      portNumber: Optional[str] = None

   name: str
   uuid: str
   vendorId: str
   modelId: str
   discoverySvcInfo: list[DiscoverySvcInfo] = []
