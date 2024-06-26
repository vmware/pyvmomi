# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vmodl import DynamicData

from pyVmomi.vim.cns import BackingObjectDetails
from pyVmomi.vim.cns import VolumeId
from pyVmomi.vim.cns import VolumeMetadata

class Volume(DynamicData):
   volumeId: VolumeId
   datastoreUrl: Optional[str] = None
   name: Optional[str] = None
   volumeType: Optional[str] = None
   storagePolicyId: Optional[str] = None
   metadata: Optional[VolumeMetadata] = None
   backingObjectDetails: Optional[BackingObjectDetails] = None
   complianceStatus: Optional[str] = None
   datastoreAccessibilityStatus: Optional[str] = None
   healthStatus: Optional[str] = None
