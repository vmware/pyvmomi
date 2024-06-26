# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vmodl import DynamicData

from pyVmomi.vim.cluster import VsanUnicastAddressInfo

from pyVmomi.vim.vm import CertThumbprint

class VsanPerfMemberInfo(DynamicData):
   thumbprint: str
   thumbprintList: list[CertThumbprint] = []
   memberUuid: Optional[str] = None
   isSupportUnicast: Optional[bool] = None
   unicastAddressInfos: list[VsanUnicastAddressInfo] = []
   hostname: Optional[str] = None
