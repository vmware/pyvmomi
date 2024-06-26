# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vim import EVCMode
from pyVmomi.vim import FeatureEVCMode

from pyVmomi.vmodl import DynamicData

class Capability(DynamicData):
   provisioningSupported: bool
   multiHostSupported: bool
   userShellAccessSupported: bool
   supportedEVCMode: list[EVCMode] = []
   supportedEVCGraphicsMode: list[FeatureEVCMode] = []
   networkBackupAndRestoreSupported: Optional[bool] = None
   ftDrsWithoutEvcSupported: Optional[bool] = None
   hciWorkflowSupported: Optional[bool] = None
   computePolicyVersion: Optional[int] = None
   clusterPlacementSupported: Optional[bool] = None
   lifecycleManagementSupported: Optional[bool] = None
   hostSeedingSupported: Optional[bool] = None
   scalableSharesSupported: Optional[bool] = None
   hadcsSupported: Optional[bool] = None
   configMgmtSupported: Optional[bool] = None
