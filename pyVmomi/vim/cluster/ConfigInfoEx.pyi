# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vim.ComputeResource import ComputeResource

from pyVmomi.vim.cluster.CryptoConfigInfo import CryptoConfigInfo

from pyVmomi.vim.cluster.DasConfigInfo import DasConfigInfo

from pyVmomi.vim.cluster.DasVmConfigInfo import DasVmConfigInfo

from pyVmomi.vim.cluster.DpmConfigInfo import DpmConfigInfo

from pyVmomi.vim.cluster.DpmHostConfigInfo import DpmHostConfigInfo

from pyVmomi.vim.cluster.DrsConfigInfo import DrsConfigInfo

from pyVmomi.vim.cluster.DrsVmConfigInfo import DrsVmConfigInfo

from pyVmomi.vim.cluster.GroupInfo import GroupInfo

from pyVmomi.vim.cluster.InfraUpdateHaConfigInfo import InfraUpdateHaConfigInfo

from pyVmomi.vim.cluster.OrchestrationInfo import OrchestrationInfo

from pyVmomi.vim.cluster.ProactiveDrsConfigInfo import ProactiveDrsConfigInfo

from pyVmomi.vim.cluster.RuleInfo import RuleInfo

from pyVmomi.vim.cluster.SystemVMsConfigInfo import SystemVMsConfigInfo

from pyVmomi.vim.cluster.VmOrchestrationInfo import VmOrchestrationInfo

from pyVmomi.vim.vsan.cluster.ConfigInfo import ConfigInfo

from pyVmomi.vim.vsan.cluster.CoreConfigInfo import CoreConfigInfo

from pyVmomi.vim.vsan.host.ConfigInfo import ConfigInfo

class ConfigInfoEx(ComputeResource.ConfigInfo):
   systemVMsConfig: Optional[SystemVMsConfigInfo] = None
   dasConfig: DasConfigInfo
   dasVmConfig: list[DasVmConfigInfo] = []
   drsConfig: DrsConfigInfo
   drsVmConfig: list[DrsVmConfigInfo] = []
   rule: list[RuleInfo] = []
   orchestration: Optional[OrchestrationInfo] = None
   vmOrchestration: list[VmOrchestrationInfo] = []
   dpmConfigInfo: Optional[DpmConfigInfo] = None
   dpmHostConfig: list[DpmHostConfigInfo] = []
   vsanConfigInfo: Optional[ConfigInfo] = None
   vsanHostConfig: list[ConfigInfo] = []
   group: list[GroupInfo] = []
   infraUpdateHaConfig: Optional[InfraUpdateHaConfigInfo] = None
   proactiveDrsConfig: Optional[ProactiveDrsConfigInfo] = None
   cryptoConfig: Optional[CryptoConfigInfo] = None
   vsanCoreConfig: Optional[CoreConfigInfo] = None
