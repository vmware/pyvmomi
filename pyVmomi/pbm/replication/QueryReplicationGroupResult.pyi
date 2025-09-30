# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.pbm.ServerObjectRef import ServerObjectRef

from pyVmomi.vmodl.DynamicData import DynamicData

from pyVmomi.vmodl.MethodFault import MethodFault

from pyVmomi.vim.vm.replication.ReplicationGroupId import ReplicationGroupId

class QueryReplicationGroupResult(DynamicData):
   object: ServerObjectRef
   replicationGroupId: Optional[ReplicationGroupId] = None
   fault: Optional[MethodFault] = None
