# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vmodl import DynamicData

from pyVmomi.vim.cluster import VsanPerfGraph

class VsanPerfEntityType(DynamicData):
   name: str
   id: str
   graphs: list[VsanPerfGraph] = []
   description: Optional[str] = None
   advancedGraphs: list[VsanPerfGraph] = []
   verboseGraphs: list[VsanPerfGraph] = []
