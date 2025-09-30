# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vim.OpaqueNetwork import OpaqueNetwork

from pyVmomi.vmodl.DynamicData import DynamicData

from pyVmomi.vim.option.OptionValue import OptionValue

class OpaqueNetworkInfo(DynamicData):
   opaqueNetworkId: str
   opaqueNetworkName: str
   opaqueNetworkType: str
   pnicZone: list[str] = []
   capability: Optional[OpaqueNetwork.Capability] = None
   extraConfig: list[OptionValue] = []
