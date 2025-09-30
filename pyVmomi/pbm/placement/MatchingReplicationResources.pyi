# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.pbm.placement.MatchingResources import MatchingResources

from pyVmomi.vim.vm.replication.ReplicationGroupId import ReplicationGroupId

class MatchingReplicationResources(MatchingResources):
   replicationGroup: list[ReplicationGroupId] = []
