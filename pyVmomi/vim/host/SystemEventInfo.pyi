# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from pyVmomi.VmomiSupport import long

from pyVmomi.vmodl.DynamicData import DynamicData

class SystemEventInfo(DynamicData):
   recordId: long
   when: str
   selType: long
   message: str
   sensorNumber: long
