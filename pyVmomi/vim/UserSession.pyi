# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from datetime import datetime

from pyVmomi.VmomiSupport import long

from pyVmomi.vmodl import DynamicData

class UserSession(DynamicData):
   key: str
   userName: str
   fullName: str
   loginTime: datetime
   lastActiveTime: datetime
   locale: str
   messageLocale: str
   extensionSession: bool
   ipAddress: str
   userAgent: str
   callCount: long
