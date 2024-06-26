# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from pyVmomi.vim.event import HostEventArgument
from pyVmomi.vim.event import VmCloneEvent

class VmBeingClonedNoFolderEvent(VmCloneEvent):
   destName: str
   destHost: HostEventArgument
