# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vim import Network

from pyVmomi.vmodl import DynamicData

from pyVmomi.vim.option import OptionValue

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
