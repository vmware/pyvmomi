# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vim.KeyValue import KeyValue

from pyVmomi.vim.vm.ProfileRawData import ProfileRawData

from pyVmomi.vim.vm.ProfileSpec import ProfileSpec

from pyVmomi.vim.vm.replication.ReplicationSpec import ReplicationSpec

class DefinedProfileSpec(ProfileSpec):
   profileId: str
   replicationSpec: Optional[ReplicationSpec] = None
   profileData: Optional[ProfileRawData] = None
   profileParams: list[KeyValue] = []
