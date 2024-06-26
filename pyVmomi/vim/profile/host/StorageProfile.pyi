# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vim.profile import ApplyProfile

from pyVmomi.vim.profile.host import NasStorageProfile

class StorageProfile(ApplyProfile):
   nasStorage: list[NasStorageProfile] = []
