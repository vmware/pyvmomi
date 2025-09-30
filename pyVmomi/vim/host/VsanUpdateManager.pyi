# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.VmomiSupport import ManagedObject

from pyVmomi.vim.ComputeResource import ComputeResource

from pyVmomi.vim.Task import Task

from pyVmomi.vim.host.MaintenanceSpec import MaintenanceSpec

from pyVmomi.vim.host.VsanHclFirmwareUpdateSpec import VsanHclFirmwareUpdateSpec

from pyVmomi.vim.vsan.VsanVibInstallPreflightStatus import VsanVibInstallPreflightStatus

from pyVmomi.vim.vsan.VsanVibScanResult import VsanVibScanResult

from pyVmomi.vim.vsan.VsanVibSpec import VsanVibSpec

class VsanUpdateManager(ManagedObject):
   def VsanVibScan(self, cluster: Optional[ComputeResource], vibSpecs: list[VsanVibSpec]) -> list[VsanVibScanResult]: ...
   def VsanVibInstall(self, cluster: Optional[ComputeResource], vibSpecs: list[VsanVibSpec], scanResults: list[VsanVibScanResult], firmwareSpecs: list[VsanHclFirmwareUpdateSpec], maintenanceSpec: Optional[MaintenanceSpec], rolling: Optional[bool], noSigCheck: Optional[bool]) -> Task: ...
   def VsanVibInstallPreflightCheck(self, cluster: Optional[ComputeResource]) -> VsanVibInstallPreflightStatus: ...
