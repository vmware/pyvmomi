# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vmodl.MethodFault import MethodFault

from pyVmomi.vim.event.DatacenterEventArgument import DatacenterEventArgument

from pyVmomi.vim.event.DatastoreEventArgument import DatastoreEventArgument

from pyVmomi.vim.event.HostEventArgument import HostEventArgument

from pyVmomi.vim.event.VmEvent import VmEvent

class VmFailedMigrateEvent(VmEvent):
   destHost: HostEventArgument
   reason: MethodFault
   destDatacenter: Optional[DatacenterEventArgument] = None
   destDatastore: Optional[DatastoreEventArgument] = None
