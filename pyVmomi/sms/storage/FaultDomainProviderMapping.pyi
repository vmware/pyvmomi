# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vmodl import DynamicData

from pyVmomi.sms.provider import Provider

from pyVmomi.vim.vm.replication import FaultDomainId

class FaultDomainProviderMapping(DynamicData):
   activeProvider: Provider
   faultDomainId: list[FaultDomainId] = []
