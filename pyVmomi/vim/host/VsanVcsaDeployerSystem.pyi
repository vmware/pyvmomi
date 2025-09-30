# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.VmomiSupport import ManagedObject

from pyVmomi.vim.vsan.VsanPrepareVsanForVcsaSpec import VsanPrepareVsanForVcsaSpec

from pyVmomi.vim.vsan.VsanVcPostDeployConfigSpec import VsanVcPostDeployConfigSpec

from pyVmomi.vim.vsan.VsanVcsaDeploymentProgress import VsanVcsaDeploymentProgress

class VsanVcsaDeployerSystem(ManagedObject):
   def PrepareVsanForVcsa(self, spec: VsanPrepareVsanForVcsaSpec) -> Optional[str]: ...
   def PostConfigForVcsa(self, spec: VsanVcPostDeployConfigSpec) -> Optional[str]: ...
   def VcsaGetBootstrapProgress(self, taskId: list[str]) -> list[VsanVcsaDeploymentProgress]: ...
