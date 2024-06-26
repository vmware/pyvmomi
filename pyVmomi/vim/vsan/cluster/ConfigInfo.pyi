# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vmodl import DynamicData

class ConfigInfo(DynamicData):
   class HostDefaultInfo(DynamicData):
      uuid: Optional[str] = None
      autoClaimStorage: Optional[bool] = None
      checksumEnabled: Optional[bool] = None

   enabled: Optional[bool] = None
   defaultConfig: Optional[HostDefaultInfo] = None
   vsanEsaEnabled: Optional[bool] = None
