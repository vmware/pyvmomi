# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vmodl import DynamicData

from pyVmomi.vim.host import VSANStretchedClusterHostCapability

class VSANStretchedClusterCapability(DynamicData):
   hostMoId: str
   connStatus: Optional[str] = None
   isSupported: Optional[bool] = None
   hostCapability: Optional[VSANStretchedClusterHostCapability] = None
