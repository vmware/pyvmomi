# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vim.profile import ApplyProfile

from pyVmomi.vim.profile.host import AuthenticationProfile
from pyVmomi.vim.profile.host import DateTimeProfile
from pyVmomi.vim.profile.host import FirewallProfile
from pyVmomi.vim.profile.host import HostMemoryProfile
from pyVmomi.vim.profile.host import NetworkProfile
from pyVmomi.vim.profile.host import OptionProfile
from pyVmomi.vim.profile.host import SecurityProfile
from pyVmomi.vim.profile.host import ServiceProfile
from pyVmomi.vim.profile.host import StorageProfile
from pyVmomi.vim.profile.host import UserGroupProfile
from pyVmomi.vim.profile.host import UserProfile

class HostApplyProfile(ApplyProfile):
   memory: Optional[HostMemoryProfile] = None
   storage: Optional[StorageProfile] = None
   network: Optional[NetworkProfile] = None
   datetime: Optional[DateTimeProfile] = None
   firewall: Optional[FirewallProfile] = None
   security: Optional[SecurityProfile] = None
   service: list[ServiceProfile] = []
   option: list[OptionProfile] = []
   userAccount: list[UserProfile] = []
   usergroupAccount: list[UserGroupProfile] = []
   authentication: Optional[AuthenticationProfile] = None
