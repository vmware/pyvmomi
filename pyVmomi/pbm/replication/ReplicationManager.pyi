# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.VmomiSupport import ManagedObject

from pyVmomi.pbm import ServerObjectRef

from pyVmomi.pbm.replication import QueryReplicationGroupResult

class ReplicationManager(ManagedObject):
   def QueryReplicationGroups(self, entities: list[ServerObjectRef]) -> list[QueryReplicationGroupResult]: ...
