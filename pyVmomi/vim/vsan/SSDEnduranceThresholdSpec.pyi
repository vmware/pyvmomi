# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vmodl import DynamicData

class SSDEnduranceThresholdSpec(DynamicData):
   clustername: str
   clusternameop: Optional[str] = None
   hostname: Optional[str] = None
   hostnameop: Optional[str] = None
   diskname: Optional[str] = None
   disknameop: Optional[str] = None
   diskvendorname: Optional[str] = None
   diskvendorop: Optional[str] = None
   ssdEndurancePtg: float
   severity: str
