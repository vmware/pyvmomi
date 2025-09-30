# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vim.profile.ApplyProfile import ApplyProfile

from pyVmomi.vim.profile.host.AuthenticationProfile import AuthenticationProfile

from pyVmomi.vim.profile.host.DateTimeProfile import DateTimeProfile

from pyVmomi.vim.profile.host.FirewallProfile import FirewallProfile

from pyVmomi.vim.profile.host.HostMemoryProfile import HostMemoryProfile

from pyVmomi.vim.profile.host.NetworkProfile import NetworkProfile

from pyVmomi.vim.profile.host.OptionProfile import OptionProfile

from pyVmomi.vim.profile.host.SecurityProfile import SecurityProfile

from pyVmomi.vim.profile.host.ServiceProfile import ServiceProfile

from pyVmomi.vim.profile.host.StorageProfile import StorageProfile

from pyVmomi.vim.profile.host.UserGroupProfile import UserGroupProfile

from pyVmomi.vim.profile.host.UserProfile import UserProfile

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
