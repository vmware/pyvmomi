# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vim import ComputeResource

from pyVmomi.vim.cluster import CryptoConfigInfo
from pyVmomi.vim.cluster import DasConfigInfo
from pyVmomi.vim.cluster import DasVmConfigInfo
from pyVmomi.vim.cluster import DpmConfigInfo
from pyVmomi.vim.cluster import DpmHostConfigInfo
from pyVmomi.vim.cluster import DrsConfigInfo
from pyVmomi.vim.cluster import DrsVmConfigInfo
from pyVmomi.vim.cluster import GroupInfo
from pyVmomi.vim.cluster import InfraUpdateHaConfigInfo
from pyVmomi.vim.cluster import OrchestrationInfo
from pyVmomi.vim.cluster import ProactiveDrsConfigInfo
from pyVmomi.vim.cluster import RuleInfo
from pyVmomi.vim.cluster import SystemVMsConfigInfo
from pyVmomi.vim.cluster import VmOrchestrationInfo

from pyVmomi.vim.vsan.cluster import ConfigInfo

from pyVmomi.vim.vsan.host import ConfigInfo

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
