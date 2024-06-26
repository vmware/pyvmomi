# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vmodl import DynamicData
from pyVmomi.vmodl import MethodFault

from pyVmomi.vim.vm.replication import FaultDomainId

class QueryReplicationPeerResult(DynamicData):
   sourceDomain: FaultDomainId
   targetDomain: list[FaultDomainId] = []
   error: list[MethodFault] = []
   warning: list[MethodFault] = []
