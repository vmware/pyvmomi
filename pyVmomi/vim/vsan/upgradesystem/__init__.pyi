# Copyright (c) 2006-2026 Broadcom. All Rights Reserved.
# The term "Broadcom" refers to Broadcom Inc. and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

import typing as _typing
import pyVmomi.vim
import pyVmomi.vmodl



class BrokenDiskChainIssue(pyVmomi.vim.VsanUpgradeSystem.PreflightCheckIssue):
   uuids: list[str] = []


class DisallowDataMovementIssue(pyVmomi.vim.VsanUpgradeSystem.PreflightCheckIssue):
   pass


class DisallowEvacuateDataIssue(pyVmomi.vim.VsanUpgradeSystem.PreflightCheckIssue):
   hosts: list[pyVmomi.vim.HostSystem] = []


class DiskUnhealthIssue(pyVmomi.vim.VsanUpgradeSystem.PreflightCheckIssue):
   uuids: list[str] = []


class HigherObjectsPresentDuringDowngradeIssue(pyVmomi.vim.VsanUpgradeSystem.PreflightCheckIssue):
   uuids: list[str] = []


class HostPropertyRetrieveIssue(pyVmomi.vim.VsanUpgradeSystem.PreflightCheckIssue):
   hosts: list[pyVmomi.vim.HostSystem] = []


class HostWithHybridDiskgroupIssue(pyVmomi.vim.VsanUpgradeSystem.PreflightCheckIssue):
   hosts: list[pyVmomi.vim.HostSystem] = []


class HostsCompressionOnlyNotSupported(pyVmomi.vim.VsanUpgradeSystem.PreflightCheckIssue):
   hosts: list[pyVmomi.vim.HostSystem] = []


class MixedEsxVersionInClientIssue(pyVmomi.vim.VsanUpgradeSystem.PreflightCheckIssue):
   clusterName: str


class MixedEsxVersionIssue(pyVmomi.vim.VsanUpgradeSystem.PreflightCheckIssue):
   pass


class ObjectInaccessibleIssue(pyVmomi.vim.VsanUpgradeSystem.PreflightCheckIssue):
   uuids: list[str] = []


class ObjectPolicyIssue(pyVmomi.vim.VsanUpgradeSystem.PreflightCheckIssue):
   uuids: list[str] = []


class RemoteClusterNotCompatible(pyVmomi.vim.VsanUpgradeSystem.PreflightCheckIssue):
   compatibilityInfo: list[pyVmomi.vmodl.KeyAnyValue] = []


class UnknownScanIssue(pyVmomi.vim.VsanUpgradeSystem.PreflightCheckIssue):
   uuids: list[str] = []


class UnsupportedHighDiskVersionIssue(pyVmomi.vim.VsanUpgradeSystem.PreflightCheckIssue):
   hosts: list[pyVmomi.vim.HostSystem] = []
