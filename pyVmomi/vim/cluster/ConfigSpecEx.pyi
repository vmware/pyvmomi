# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vim.ComputeResource import ComputeResource

from pyVmomi.vim.cluster.CryptoConfigInfo import CryptoConfigInfo

from pyVmomi.vim.cluster.DasConfigInfo import DasConfigInfo

from pyVmomi.vim.cluster.DasVmConfigSpec import DasVmConfigSpec

from pyVmomi.vim.cluster.DpmConfigInfo import DpmConfigInfo

from pyVmomi.vim.cluster.DpmHostConfigSpec import DpmHostConfigSpec

from pyVmomi.vim.cluster.DrsConfigInfo import DrsConfigInfo

from pyVmomi.vim.cluster.DrsVmConfigSpec import DrsVmConfigSpec

from pyVmomi.vim.cluster.GroupSpec import GroupSpec

from pyVmomi.vim.cluster.InfraUpdateHaConfigInfo import InfraUpdateHaConfigInfo

from pyVmomi.vim.cluster.OrchestrationInfo import OrchestrationInfo

from pyVmomi.vim.cluster.ProactiveDrsConfigInfo import ProactiveDrsConfigInfo

from pyVmomi.vim.cluster.RuleSpec import RuleSpec

from pyVmomi.vim.cluster.SystemVMsConfigSpec import SystemVMsConfigSpec

from pyVmomi.vim.cluster.VmOrchestrationSpec import VmOrchestrationSpec

from pyVmomi.vim.vsan.cluster.ConfigInfo import ConfigInfo

from pyVmomi.vim.vsan.cluster.CoreConfigSpec import CoreConfigSpec

from pyVmomi.vim.vsan.host.ConfigInfo import ConfigInfo

class ConfigSpecEx(ComputeResource.ConfigSpec):
   systemVMsConfig: Optional[SystemVMsConfigSpec] = None
   dasConfig: Optional[DasConfigInfo] = None
   dasVmConfigSpec: list[DasVmConfigSpec] = []
   drsConfig: Optional[DrsConfigInfo] = None
   drsVmConfigSpec: list[DrsVmConfigSpec] = []
   rulesSpec: list[RuleSpec] = []
   orchestration: Optional[OrchestrationInfo] = None
   vmOrchestrationSpec: list[VmOrchestrationSpec] = []
   dpmConfig: Optional[DpmConfigInfo] = None
   dpmHostConfigSpec: list[DpmHostConfigSpec] = []
   vsanConfig: Optional[ConfigInfo] = None
   vsanHostConfigSpec: list[ConfigInfo] = []
   groupSpec: list[GroupSpec] = []
   infraUpdateHaConfig: Optional[InfraUpdateHaConfigInfo] = None
   proactiveDrsConfig: Optional[ProactiveDrsConfigInfo] = None
   inHciWorkflow: Optional[bool] = None
   cryptoConfig: Optional[CryptoConfigInfo] = None
   vsanCoreConfigSpec: Optional[CoreConfigSpec] = None
