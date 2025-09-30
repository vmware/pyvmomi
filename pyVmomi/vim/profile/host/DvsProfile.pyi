# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vim.profile.ApplyProfile import ApplyProfile

from pyVmomi.vim.profile.host.PnicUplinkProfile import PnicUplinkProfile

class DvsProfile(ApplyProfile):
   key: str
   name: str
   uplink: list[PnicUplinkProfile] = []
