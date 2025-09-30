# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vim.Network import Network

from pyVmomi.vmodl.DynamicData import DynamicData

from pyVmomi.vim.option.OptionValue import OptionValue

class OpaqueNetwork(Network):
   class Summary(Network.Summary):
      opaqueNetworkId: str
      opaqueNetworkType: str

   class Capability(DynamicData):
      networkReservationSupported: bool

   @property
   def capability(self) -> Optional[Capability]: ...
   @property
   def extraConfig(self) -> list[OptionValue]: ...
