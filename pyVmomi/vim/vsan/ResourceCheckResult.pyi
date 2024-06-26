# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from datetime import datetime

from typing import Optional

from pyVmomi.VmomiSupport import long

from pyVmomi.vmodl import LocalizableMessage

from pyVmomi.vim.cluster import VsanClusterHealthSummary

from pyVmomi.vim.vsan import EntityResourceCheckDetails
from pyVmomi.vim.vsan import FaultDomainResourceCheckResult
from pyVmomi.vim.vsan import VsanHealthThreshold

class ResourceCheckResult(EntityResourceCheckDetails):
   timestamp: datetime
   status: str
   messages: list[LocalizableMessage] = []
   faultDomains: list[FaultDomainResourceCheckResult] = []
   dataToMove: Optional[long] = None
   nonCompliantObjects: list[str] = []
   inaccessibleObjects: list[str] = []
   capacityThreshold: Optional[VsanHealthThreshold] = None
   health: Optional[VsanClusterHealthSummary] = None
   dataToResync: Optional[long] = None
