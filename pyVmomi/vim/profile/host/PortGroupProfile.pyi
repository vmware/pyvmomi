# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from pyVmomi.vim.profile import ApplyProfile

from pyVmomi.vim.profile.host import NetworkPolicyProfile

class PortGroupProfile(ApplyProfile):
   class VlanProfile(ApplyProfile):
      pass

   class VirtualSwitchSelectionProfile(ApplyProfile):
      pass

   key: str
   name: str
   vlan: VlanProfile
   vswitch: VirtualSwitchSelectionProfile
   networkPolicy: NetworkPolicyProfile
