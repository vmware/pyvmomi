# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import ClassVar
from typing import Optional

from pyVmomi.VmomiSupport import Enum

from pyVmomi.vmodl import DynamicData
from pyVmomi.vmodl import MethodFault

from pyVmomi.vim.encryption import CryptoKeyId

class ToolsConfigInfo(DynamicData):
   class UpgradePolicy(Enum):
      manual: ClassVar['UpgradePolicy'] = 'manual'
      upgradeAtPowerCycle: ClassVar['UpgradePolicy'] = 'upgradeAtPowerCycle'

   class ToolsLastInstallInfo(DynamicData):
      counter: int
      fault: Optional[MethodFault] = None

   toolsVersion: Optional[int] = None
   toolsInstallType: Optional[str] = None
   afterPowerOn: Optional[bool] = None
   afterResume: Optional[bool] = None
   beforeGuestStandby: Optional[bool] = None
   beforeGuestShutdown: Optional[bool] = None
   beforeGuestReboot: Optional[bool] = None
   toolsUpgradePolicy: Optional[str] = None
   pendingCustomization: Optional[str] = None
   customizationKeyId: Optional[CryptoKeyId] = None
   syncTimeWithHostAllowed: Optional[bool] = None
   syncTimeWithHost: Optional[bool] = None
   lastInstallInfo: Optional[ToolsLastInstallInfo] = None
