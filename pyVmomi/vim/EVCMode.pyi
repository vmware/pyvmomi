# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vim.ElementDescription import ElementDescription

from pyVmomi.vim.host.CpuIdInfo import CpuIdInfo

from pyVmomi.vim.host.FeatureCapability import FeatureCapability

from pyVmomi.vim.host.FeatureMask import FeatureMask

from pyVmomi.vim.vm.FeatureRequirement import FeatureRequirement

class EVCMode(ElementDescription):
   guaranteedCPUFeatures: list[CpuIdInfo] = []
   featureCapability: list[FeatureCapability] = []
   featureMask: list[FeatureMask] = []
   featureRequirement: list[FeatureRequirement] = []
   vendor: str
   track: list[str] = []
   vendorTier: int
