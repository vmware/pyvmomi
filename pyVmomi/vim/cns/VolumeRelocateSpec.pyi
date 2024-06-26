# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vim import Datastore

from pyVmomi.vmodl import DynamicData

from pyVmomi.vim.cns import VolumeId

from pyVmomi.vim.vm import ProfileSpec

class VolumeRelocateSpec(DynamicData):
   volumeId: VolumeId
   datastore: Datastore
   profile: list[ProfileSpec] = []
