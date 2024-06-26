# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vim import KeyValue

from pyVmomi.vmodl import DynamicData

class DhcpConfigSpec(DynamicData):
   class DhcpOptionsSpec(DynamicData):
      enable: Optional[bool] = None
      config: list[KeyValue] = []
      operation: str

   ipv6: Optional[DhcpOptionsSpec] = None
   ipv4: Optional[DhcpOptionsSpec] = None
