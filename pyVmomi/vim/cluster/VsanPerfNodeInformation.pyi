# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vmodl.DynamicData import DynamicData

from pyVmomi.vmodl.MethodFault import MethodFault

from pyVmomi.vim.cluster.VsanPerfMasterInformation import VsanPerfMasterInformation

class VsanPerfNodeInformation(DynamicData):
   version: str
   hostname: Optional[str] = None
   error: Optional[MethodFault] = None
   isCmmdsMaster: bool
   isStatsMaster: bool
   vsanMasterUuid: Optional[str] = None
   vsanNodeUuid: Optional[str] = None
   masterInfo: Optional[VsanPerfMasterInformation] = None
   diagnosticMode: Optional[bool] = None
