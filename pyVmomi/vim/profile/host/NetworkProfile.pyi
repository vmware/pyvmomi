# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vim.profile import ApplyProfile

from pyVmomi.vim.profile.host import DvsHostVNicProfile
from pyVmomi.vim.profile.host import DvsProfile
from pyVmomi.vim.profile.host import DvsServiceConsoleVNicProfile
from pyVmomi.vim.profile.host import HostPortGroupProfile
from pyVmomi.vim.profile.host import IpRouteProfile
from pyVmomi.vim.profile.host import NetStackInstanceProfile
from pyVmomi.vim.profile.host import NsxHostVNicProfile
from pyVmomi.vim.profile.host import OpaqueSwitchProfile
from pyVmomi.vim.profile.host import PhysicalNicProfile
from pyVmomi.vim.profile.host import ServiceConsolePortGroupProfile
from pyVmomi.vim.profile.host import VirtualSwitchProfile
from pyVmomi.vim.profile.host import VmPortGroupProfile

class NetworkProfile(ApplyProfile):
   class DnsConfigProfile(ApplyProfile):
      pass

   vswitch: list[VirtualSwitchProfile] = []
   vmPortGroup: list[VmPortGroupProfile] = []
   hostPortGroup: list[HostPortGroupProfile] = []
   serviceConsolePortGroup: list[ServiceConsolePortGroupProfile] = []
   dnsConfig: Optional[DnsConfigProfile] = None
   ipRouteConfig: Optional[IpRouteProfile] = None
   consoleIpRouteConfig: Optional[IpRouteProfile] = None
   pnic: list[PhysicalNicProfile] = []
   dvswitch: list[DvsProfile] = []
   dvsServiceConsoleNic: list[DvsServiceConsoleVNicProfile] = []
   dvsHostNic: list[DvsHostVNicProfile] = []
   nsxHostNic: list[NsxHostVNicProfile] = []
   netStackInstance: list[NetStackInstanceProfile] = []
   opaqueSwitch: Optional[OpaqueSwitchProfile] = None
