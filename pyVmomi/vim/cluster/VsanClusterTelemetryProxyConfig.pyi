# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vmodl import DynamicData

class VsanClusterTelemetryProxyConfig(DynamicData):
   host: Optional[str] = None
   port: Optional[int] = None
   user: Optional[str] = None
   password: Optional[str] = None
   autoDiscovered: Optional[bool] = None
