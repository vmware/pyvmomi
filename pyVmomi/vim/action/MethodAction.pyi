# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.VmomiSupport import ManagedMethod

from pyVmomi.vim.action import Action
from pyVmomi.vim.action import MethodActionArgument

class MethodAction(Action):
   name: ManagedMethod
   argument: list[MethodActionArgument] = []
