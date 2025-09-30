# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.sms.storage.replication.DeviceId import DeviceId

class VirtualDiskMoId(DeviceId):
   vcUuid: Optional[str] = None
   vmMoid: str
   diskKey: str
