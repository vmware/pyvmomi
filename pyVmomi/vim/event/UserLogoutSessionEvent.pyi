# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from datetime import datetime

from typing import Optional

from pyVmomi.VmomiSupport import long

from pyVmomi.vim.event import SessionEvent

class UserLogoutSessionEvent(SessionEvent):
   ipAddress: Optional[str] = None
   userAgent: Optional[str] = None
   callCount: Optional[long] = None
   sessionId: Optional[str] = None
   loginTime: Optional[datetime] = None
