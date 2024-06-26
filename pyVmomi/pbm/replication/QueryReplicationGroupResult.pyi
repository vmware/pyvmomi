# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.pbm import ServerObjectRef

from pyVmomi.vmodl import DynamicData
from pyVmomi.vmodl import MethodFault

from pyVmomi.vim.vm.replication import ReplicationGroupId

class QueryReplicationGroupResult(DynamicData):
   object: ServerObjectRef
   replicationGroupId: Optional[ReplicationGroupId] = None
   fault: Optional[MethodFault] = None
