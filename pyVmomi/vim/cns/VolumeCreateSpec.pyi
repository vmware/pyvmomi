# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vim import Datastore

from pyVmomi.vmodl import DynamicData

from pyVmomi.vim.cns import BackingObjectDetails
from pyVmomi.vim.cns import BaseCreateSpec
from pyVmomi.vim.cns import VolumeMetadata
from pyVmomi.vim.cns import VolumeSource

from pyVmomi.vim.vm import ProfileSpec

class VolumeCreateSpec(DynamicData):
   name: str
   volumeType: str
   datastores: list[Datastore] = []
   metadata: Optional[VolumeMetadata] = None
   backingObjectDetails: BackingObjectDetails
   profile: list[ProfileSpec] = []
   createSpec: Optional[BaseCreateSpec] = None
   volumeSource: Optional[VolumeSource] = None
