# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vmodl import DynamicData

class IpRouteConfigInfo(DynamicData):
   class Gateway(DynamicData):
      ipAddress: Optional[str] = None
      device: Optional[str] = None

   class IpRoute(DynamicData):
      network: str
      prefixLength: int
      gateway: Gateway

   ipRoute: list[IpRoute] = []
