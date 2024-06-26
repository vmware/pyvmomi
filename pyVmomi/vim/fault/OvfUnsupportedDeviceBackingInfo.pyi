# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vim.fault import OvfSystemFault

class OvfUnsupportedDeviceBackingInfo(OvfSystemFault):
   elementName: Optional[str] = None
   instanceId: Optional[str] = None
   deviceName: str
   backingName: Optional[str] = None
