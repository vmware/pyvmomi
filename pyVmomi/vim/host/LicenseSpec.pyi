# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vim import LicenseManager

from pyVmomi.vmodl import DynamicData

class LicenseSpec(DynamicData):
   source: Optional[LicenseManager.LicenseSource] = None
   editionKey: Optional[str] = None
   disabledFeatureKey: list[str] = []
   enabledFeatureKey: list[str] = []
