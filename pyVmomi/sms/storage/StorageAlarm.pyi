# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from datetime import datetime

from typing import Optional

from pyVmomi.VmomiSupport import long

from pyVmomi.vmodl import DynamicData

from pyVmomi.sms.storage import NameValuePair

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
