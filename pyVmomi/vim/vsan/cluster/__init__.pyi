# Copyright (c) 2006-2026 Broadcom. All Rights Reserved.
# The term "Broadcom" refers to Broadcom Inc. and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

import typing as _typing
import pyVmomi.vmodl
import pyVmomi.vim.vsan


class ComplianceResourceCheckStatusType:
   pass


class ConfigInfo(pyVmomi.vmodl.DynamicData):
   class HostDefaultInfo(pyVmomi.vmodl.DynamicData):
      uuid: _typing.Optional[str] = None
      autoClaimStorage: _typing.Optional[bool] = None
      checksumEnabled: _typing.Optional[bool] = None

   enabled: _typing.Optional[bool] = None
   defaultConfig: _typing.Optional[HostDefaultInfo] = None
   vsanEsaEnabled: _typing.Optional[bool] = None
   vsanCyberRecoveryEnabled: _typing.Optional[bool] = None


class CoreConfigInfo(pyVmomi.vmodl.DynamicData):
   vsanMaxEnabled: _typing.Optional[bool] = None


class CoreConfigSpec(pyVmomi.vmodl.DynamicData):
   vsanMaxEnabled: _typing.Optional[bool] = None


class VbossClusterConfig(pyVmomi.vim.vsan.VbossConfig):
   pass

class VsanManagedStorageType:
   pass
