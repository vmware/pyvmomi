# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from pyVmomi.vim.profile.ApplyProfile import ApplyProfile

from pyVmomi.vim.profile.host.NetworkPolicyProfile import NetworkPolicyProfile

class VirtualSwitchProfile(ApplyProfile):
   class LinkProfile(ApplyProfile):
      pass

   class NumPortsProfile(ApplyProfile):
      pass

   key: str
   name: str
   link: LinkProfile
   numPorts: NumPortsProfile
   networkPolicy: NetworkPolicyProfile
