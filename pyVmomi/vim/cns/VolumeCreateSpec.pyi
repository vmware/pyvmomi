# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vim.Datastore import Datastore

from pyVmomi.vmodl.DynamicData import DynamicData

from pyVmomi.vim.cns.BackingObjectDetails import BackingObjectDetails

from pyVmomi.vim.cns.BaseCreateSpec import BaseCreateSpec

from pyVmomi.vim.cns.VolumeMetadata import VolumeMetadata

from pyVmomi.vim.cns.VolumeSource import VolumeSource

from pyVmomi.vim.vm.ProfileSpec import ProfileSpec

class VolumeCreateSpec(DynamicData):
   name: str
   volumeType: str
   datastores: list[Datastore] = []
   metadata: Optional[VolumeMetadata] = None
   backingObjectDetails: BackingObjectDetails
   profile: list[ProfileSpec] = []
   createSpec: Optional[BaseCreateSpec] = None
   volumeSource: Optional[VolumeSource] = None
