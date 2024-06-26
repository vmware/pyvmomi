# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from datetime import datetime

from typing import ClassVar
from typing import Optional

from pyVmomi.VmomiSupport import Enum

from pyVmomi.vmodl import DynamicData

from pyVmomi.vim.event import ComputeResourceEventArgument
from pyVmomi.vim.event import DatacenterEventArgument
from pyVmomi.vim.event import DatastoreEventArgument
from pyVmomi.vim.event import DvsEventArgument
from pyVmomi.vim.event import HostEventArgument
from pyVmomi.vim.event import NetworkEventArgument
from pyVmomi.vim.event import VmEventArgument

class Event(DynamicData):
   class EventSeverity(Enum):
      error: ClassVar['EventSeverity'] = 'error'
      warning: ClassVar['EventSeverity'] = 'warning'
      info: ClassVar['EventSeverity'] = 'info'
      user: ClassVar['EventSeverity'] = 'user'

   key: int
   chainId: int
   createdTime: datetime
   userName: str
   datacenter: Optional[DatacenterEventArgument] = None
   computeResource: Optional[ComputeResourceEventArgument] = None
   host: Optional[HostEventArgument] = None
   vm: Optional[VmEventArgument] = None
   ds: Optional[DatastoreEventArgument] = None
   net: Optional[NetworkEventArgument] = None
   dvs: Optional[DvsEventArgument] = None
   fullFormattedMessage: Optional[str] = None
   changeTag: Optional[str] = None
