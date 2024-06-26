# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vmodl import DynamicData

class VsanNicRdmaInfo(DynamicData):
   rdmaCapable: Optional[bool] = None
   rdmaProtocolCapable: Optional[str] = None
   dcbEnabled: Optional[bool] = None
   dcbMode: Optional[str] = None
   pfcEnabled: Optional[bool] = None
   pfcConfig: Optional[str] = None
