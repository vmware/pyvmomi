# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vim import ElementDescription

from pyVmomi.vim.host import CpuIdInfo
from pyVmomi.vim.host import FeatureCapability
from pyVmomi.vim.host import FeatureMask

from pyVmomi.vim.vm import FeatureRequirement

class EVCMode(ElementDescription):
   guaranteedCPUFeatures: list[CpuIdInfo] = []
   featureCapability: list[FeatureCapability] = []
   featureMask: list[FeatureMask] = []
   featureRequirement: list[FeatureRequirement] = []
   vendor: str
   track: list[str] = []
   vendorTier: int
