# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vmodl import DynamicData

class DhcpService(DynamicData):
   class Specification(DynamicData):
      virtualSwitch: str
      defaultLeaseDuration: int
      leaseBeginIp: str
      leaseEndIp: str
      maxLeaseDuration: int
      unlimitedLease: bool
      ipSubnetAddr: str
      ipSubnetMask: str

   class Config(DynamicData):
      changeOperation: Optional[str] = None
      key: str
      spec: Specification

   key: str
   spec: Specification
