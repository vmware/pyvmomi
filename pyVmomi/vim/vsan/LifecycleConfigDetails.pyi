# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vmodl import DynamicData

from pyVmomi.vim.vsan import LifecycleFaultDomainDetails
from pyVmomi.vim.vsan import LifecycleWitnessDetails

class LifecycleConfigDetails(DynamicData):
   clusterType: str
   faultDomainsDetails: list[LifecycleFaultDomainDetails] = []
   witnessHostsDetails: list[LifecycleWitnessDetails] = []
