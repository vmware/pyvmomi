# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from pyVmomi.VmomiSupport import long

from pyVmomi.vim.fault import GuestOperationsFault

from pyVmomi.vim.vm.guest import GuestAuthentication

class GuestAuthenticationChallenge(GuestOperationsFault):
   serverChallenge: GuestAuthentication
   sessionID: long
