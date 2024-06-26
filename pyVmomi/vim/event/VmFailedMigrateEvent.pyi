# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vmodl import MethodFault

from pyVmomi.vim.event import DatacenterEventArgument
from pyVmomi.vim.event import DatastoreEventArgument
from pyVmomi.vim.event import HostEventArgument
from pyVmomi.vim.event import VmEvent

class VmFailedMigrateEvent(VmEvent):
   destHost: HostEventArgument
   reason: MethodFault
   destDatacenter: Optional[DatacenterEventArgument] = None
   destDatastore: Optional[DatastoreEventArgument] = None
