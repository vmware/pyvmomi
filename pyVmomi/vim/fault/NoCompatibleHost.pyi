# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vim import HostSystem

from pyVmomi.vmodl import MethodFault

from pyVmomi.vim.fault import VimFault

class NoCompatibleHost(VimFault):
   host: list[HostSystem] = []
   error: list[MethodFault] = []
