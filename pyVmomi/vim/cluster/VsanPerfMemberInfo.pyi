# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vmodl.DynamicData import DynamicData

from pyVmomi.vim.cluster.VsanUnicastAddressInfo import VsanUnicastAddressInfo

from pyVmomi.vim.vm.CertThumbprint import CertThumbprint

class VsanPerfMemberInfo(DynamicData):
   thumbprint: str
   thumbprintList: list[CertThumbprint] = []
   memberUuid: Optional[str] = None
   isSupportUnicast: Optional[bool] = None
   unicastAddressInfos: list[VsanUnicastAddressInfo] = []
   hostname: Optional[str] = None
