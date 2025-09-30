# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vim.fault.OvfSystemFault import OvfSystemFault

class OvfUnsupportedDeviceBackingInfo(OvfSystemFault):
   elementName: Optional[str] = None
   instanceId: Optional[str] = None
   deviceName: str
   backingName: Optional[str] = None
