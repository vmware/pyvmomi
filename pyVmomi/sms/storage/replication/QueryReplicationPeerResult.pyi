# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vmodl.DynamicData import DynamicData

from pyVmomi.vmodl.MethodFault import MethodFault

from pyVmomi.vim.vm.replication.FaultDomainId import FaultDomainId

class QueryReplicationPeerResult(DynamicData):
   sourceDomain: FaultDomainId
   targetDomain: list[FaultDomainId] = []
   error: list[MethodFault] = []
   warning: list[MethodFault] = []
