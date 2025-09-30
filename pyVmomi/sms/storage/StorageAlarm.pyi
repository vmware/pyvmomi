# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from datetime import datetime

from typing import Optional

from pyVmomi.VmomiSupport import long

from pyVmomi.vmodl.DynamicData import DynamicData

from pyVmomi.sms.storage.NameValuePair import NameValuePair

class StorageAlarm(DynamicData):
   alarmId: long
   alarmType: str
   containerId: Optional[str] = None
   objectId: Optional[str] = None
   objectType: str
   status: str
   alarmTimeStamp: datetime
   messageId: str
   parameterList: list[NameValuePair] = []
   alarmObject: Optional[object] = None
