# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import ClassVar

from pyVmomi.VmomiSupport import Enum

from pyVmomi.vmodl import DynamicData

class NvmeTransportParameters(DynamicData):
   class NvmeAddressFamily(Enum):
      ipv4: ClassVar['NvmeAddressFamily'] = 'ipv4'
      ipv6: ClassVar['NvmeAddressFamily'] = 'ipv6'
      infiniBand: ClassVar['NvmeAddressFamily'] = 'infiniBand'
      fc: ClassVar['NvmeAddressFamily'] = 'fc'
      loopback: ClassVar['NvmeAddressFamily'] = 'loopback'
      unknown: ClassVar['NvmeAddressFamily'] = 'unknown'
