# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.pbm.placement import MatchingResources

from pyVmomi.vim.vm.replication import ReplicationGroupId

class MatchingReplicationResources(MatchingResources):
   replicationGroup: list[ReplicationGroupId] = []
