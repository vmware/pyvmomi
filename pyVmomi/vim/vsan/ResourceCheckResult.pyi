# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from datetime import datetime

from typing import ClassVar
from typing import Optional

from pyVmomi.VmomiSupport import Enum
from pyVmomi.VmomiSupport import long

from pyVmomi.vmodl.LocalizableMessage import LocalizableMessage

from pyVmomi.vim.cluster.VsanClusterHealthSummary import VsanClusterHealthSummary

from pyVmomi.vim.vsan.EntityResourceCheckDetails import EntityResourceCheckDetails

from pyVmomi.vim.vsan.FaultDomainResourceCheckResult import FaultDomainResourceCheckResult

from pyVmomi.vim.vsan.VsanHealthThreshold import VsanHealthThreshold

class ResourceCheckResult(EntityResourceCheckDetails):
   class ResourceCheckDedupStoreHealthState(Enum):
      Inaccessible: ClassVar['ResourceCheckDedupStoreHealthState'] = 'Inaccessible'
      Noncompliant: ClassVar['ResourceCheckDedupStoreHealthState'] = 'Noncompliant'

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
   dedupStoreHealth: Optional[str] = None
