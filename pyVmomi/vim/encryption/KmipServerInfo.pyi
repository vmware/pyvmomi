# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vmodl import DynamicData

class KmipServerInfo(DynamicData):
   name: str
   address: str
   port: int
   proxyAddress: Optional[str] = None
   proxyPort: Optional[int] = None
   reconnect: Optional[int] = None
   protocol: Optional[str] = None
   nbio: Optional[int] = None
   timeout: Optional[int] = None
   userName: Optional[str] = None
