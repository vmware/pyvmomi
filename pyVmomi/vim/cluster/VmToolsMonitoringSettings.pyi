# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vmodl import DynamicData

class VmToolsMonitoringSettings(DynamicData):
   enabled: Optional[bool] = None
   vmMonitoring: Optional[str] = None
   clusterSettings: Optional[bool] = None
   failureInterval: Optional[int] = None
   minUpTime: Optional[int] = None
   maxFailures: Optional[int] = None
   maxFailureWindow: Optional[int] = None
