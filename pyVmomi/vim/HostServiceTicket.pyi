# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vmodl import DynamicData

class HostServiceTicket(DynamicData):
   host: Optional[str] = None
   port: Optional[int] = None
   sslThumbprint: Optional[str] = None
   service: str
   serviceVersion: str
   sessionId: str
