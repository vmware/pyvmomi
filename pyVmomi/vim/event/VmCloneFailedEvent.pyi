# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from pyVmomi.vmodl.MethodFault import MethodFault

from pyVmomi.vim.event.FolderEventArgument import FolderEventArgument

from pyVmomi.vim.event.HostEventArgument import HostEventArgument

from pyVmomi.vim.event.VmCloneEvent import VmCloneEvent

class VmCloneFailedEvent(VmCloneEvent):
   destFolder: FolderEventArgument
   destName: str
   destHost: HostEventArgument
   reason: MethodFault
