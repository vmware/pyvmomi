# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vim.option import IntOption

from pyVmomi.vim.vm.device import VirtualControllerOption

class VirtualNVMEControllerOption(VirtualControllerOption):
   numNVMEDisks: IntOption
   sharing: list[str] = []
