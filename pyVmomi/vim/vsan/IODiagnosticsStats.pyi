# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from datetime import datetime

from typing import Optional

from pyVmomi.vmodl.DynamicData import DynamicData

from pyVmomi.vim.vsan.ObjectIOStats import ObjectIOStats

class IODiagnosticsStats(DynamicData):
   objectsIOStats: list[ObjectIOStats] = []
   startTime: datetime
   endTime: datetime
