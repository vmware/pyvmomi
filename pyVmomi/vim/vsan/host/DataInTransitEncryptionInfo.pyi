# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vmodl import DynamicData

class DataInTransitEncryptionInfo(DynamicData):
   enabled: Optional[bool] = None
   rekeyInterval: Optional[int] = None
   transitionState: Optional[str] = None
