# Copyright (c) 2006-2026 Broadcom. All Rights Reserved.
# The term "Broadcom" refers to Broadcom Inc. and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

import typing as _typing
import pyVmomi.vim
import pyVmomi.vmodl



class ExtendedProductInfo(pyVmomi.vmodl.DynamicData):
   companyUrl: _typing.Optional[str] = None
   productUrl: _typing.Optional[str] = None
   managementUrl: _typing.Optional[str] = None
   self: _typing.Optional[pyVmomi.vim.ManagedEntity] = None


class ManagedByInfo(pyVmomi.vmodl.DynamicData):
   extensionKey: str
   type: str


class ManagedEntityInfo(pyVmomi.vmodl.DynamicData):
   type: str
   smallIconUrl: _typing.Optional[str] = None
   iconUrl: _typing.Optional[str] = None
   description: _typing.Optional[str] = None


class SolutionManagerInfo(pyVmomi.vmodl.DynamicData):
   class TabInfo(pyVmomi.vmodl.DynamicData):
      label: str
      url: str

   tab: list[TabInfo] = []
   smallIconUrl: _typing.Optional[str] = None
