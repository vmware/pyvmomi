# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vim import OpaqueNetwork

from pyVmomi.vmodl import DynamicData

from pyVmomi.vim.option import OptionValue

class OpaqueNetworkInfo(DynamicData):
   opaqueNetworkId: str
   opaqueNetworkName: str
   opaqueNetworkType: str
   pnicZone: list[str] = []
   capability: Optional[OpaqueNetwork.Capability] = None
   extraConfig: list[OptionValue] = []
