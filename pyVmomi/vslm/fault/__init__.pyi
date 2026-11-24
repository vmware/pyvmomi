# Copyright (c) 2006-2026 Broadcom. All Rights Reserved.
# The term "Broadcom" refers to Broadcom Inc. and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

import typing as _typing
import pyVmomi.vmodl
import pyVmomi.vim.vslm



class SyncFault(VslmFault):
   id: _typing.Optional[pyVmomi.vim.vslm.ID] = None


class VslmFault(pyVmomi.vmodl.MethodFault):
   msg: _typing.Optional[str] = None
