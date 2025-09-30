# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from pyVmomi.vmodl.DynamicData import DynamicData

from pyVmomi.vim.host.HostBusAdapter import HostBusAdapter

class LunHbaAssociation(DynamicData):
   canonicalName: str
   hba: list[HostBusAdapter] = []
