# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vim.profile.ApplyProfile import ApplyProfile

from pyVmomi.vim.profile.host.ActiveDirectoryProfile import ActiveDirectoryProfile

class AuthenticationProfile(ApplyProfile):
   activeDirectory: Optional[ActiveDirectoryProfile] = None
