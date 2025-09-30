# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vmodl.DynamicData import DynamicData

class PciPassthruInfo(DynamicData):
   id: str
   dependentDevice: str
   passthruEnabled: bool
   passthruCapable: bool
   passthruActive: bool
   hardwareLabel: Optional[str] = None
