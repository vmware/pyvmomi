# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from pyVmomi.vim.event.HostEventArgument import HostEventArgument

from pyVmomi.vim.event.MigrationEvent import MigrationEvent

from pyVmomi.vim.event.ResourcePoolEventArgument import ResourcePoolEventArgument

class MigrationResourceErrorEvent(MigrationEvent):
   dstPool: ResourcePoolEventArgument
   dstHost: HostEventArgument
