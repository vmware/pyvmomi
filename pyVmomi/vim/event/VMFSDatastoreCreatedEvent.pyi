# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vim.event.DatastoreEventArgument import DatastoreEventArgument

from pyVmomi.vim.event.HostEvent import HostEvent

class VMFSDatastoreCreatedEvent(HostEvent):
   datastore: DatastoreEventArgument
   datastoreUrl: Optional[str] = None
