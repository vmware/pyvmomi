# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vmodl.DynamicData import DynamicData

from pyVmomi.vim.cluster.VsanClusterHealthResultKeyValuePair import VsanClusterHealthResultKeyValuePair

from pyVmomi.vim.cluster.VsanClusterTelemetryProxyConfig import VsanClusterTelemetryProxyConfig

class VsanClusterHealthConfigs(DynamicData):
   enableVsanTelemetry: Optional[bool] = None
   vsanTelemetryInterval: Optional[int] = None
   vsanTelemetryProxy: Optional[VsanClusterTelemetryProxyConfig] = None
   configs: list[VsanClusterHealthResultKeyValuePair] = []
