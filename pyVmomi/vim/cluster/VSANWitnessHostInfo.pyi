# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vim import HostSystem

from pyVmomi.vmodl import DynamicData

class VSANWitnessHostInfo(DynamicData):
   nodeUuid: str
   faultDomainName: Optional[str] = None
   preferredFdName: Optional[str] = None
   preferredFdUuid: Optional[str] = None
   unicastAgentAddr: Optional[str] = None
   host: Optional[HostSystem] = None
   metadataMode: Optional[bool] = None
