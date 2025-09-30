# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vmodl.DynamicData import DynamicData

from pyVmomi.vim.host.ConnectSpec import ConnectSpec

from pyVmomi.vim.vsan.DataEfficiencyConfig import DataEfficiencyConfig

from pyVmomi.vim.vsan.VsanDeconvergedNetConfig import VsanDeconvergedNetConfig

from pyVmomi.vim.vsan.host.CreateNativeKeyProviderSpec import CreateNativeKeyProviderSpec

from pyVmomi.vim.vsan.host.EncryptionInfo import EncryptionInfo

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
   deconvergedNetConfig: Optional[VsanDeconvergedNetConfig] = None
