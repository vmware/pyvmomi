# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vmodl import DynamicData

from pyVmomi.vim.host import ConnectSpec

from pyVmomi.vim.vsan import DataEfficiencyConfig

from pyVmomi.vim.vsan.host import CreateNativeKeyProviderSpec
from pyVmomi.vim.vsan.host import EncryptionInfo

class VsanVcPostDeployConfigSpec(DynamicData):
   dcName: Optional[str] = None
   clusterName: Optional[str] = None
   firstHost: Optional[ConnectSpec] = None
   hostsToAdd: list[ConnectSpec] = []
   vsanDataEfficiencyConfig: Optional[DataEfficiencyConfig] = None
   vsanLicenseKey: Optional[str] = None
   hostLicenseKey: Optional[str] = None
   taskId: Optional[str] = None
   vsanDataEncryptionConfig: Optional[EncryptionInfo] = None
   createNativeKeyProviderSpec: Optional[CreateNativeKeyProviderSpec] = None
   vsanClusterMode: Optional[str] = None
