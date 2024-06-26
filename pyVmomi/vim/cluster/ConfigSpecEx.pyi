# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vim import ComputeResource

from pyVmomi.vim.cluster import CryptoConfigInfo
from pyVmomi.vim.cluster import DasConfigInfo
from pyVmomi.vim.cluster import DasVmConfigSpec
from pyVmomi.vim.cluster import DpmConfigInfo
from pyVmomi.vim.cluster import DpmHostConfigSpec
from pyVmomi.vim.cluster import DrsConfigInfo
from pyVmomi.vim.cluster import DrsVmConfigSpec
from pyVmomi.vim.cluster import GroupSpec
from pyVmomi.vim.cluster import InfraUpdateHaConfigInfo
from pyVmomi.vim.cluster import OrchestrationInfo
from pyVmomi.vim.cluster import ProactiveDrsConfigInfo
from pyVmomi.vim.cluster import RuleSpec
from pyVmomi.vim.cluster import SystemVMsConfigSpec
from pyVmomi.vim.cluster import VmOrchestrationSpec

from pyVmomi.vim.vsan.cluster import ConfigInfo

from pyVmomi.vim.vsan.host import ConfigInfo

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
