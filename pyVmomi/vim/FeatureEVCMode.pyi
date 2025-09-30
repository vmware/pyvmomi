# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vim.ElementDescription import ElementDescription

from pyVmomi.vim.host.FeatureCapability import FeatureCapability

from pyVmomi.vim.host.FeatureMask import FeatureMask

from pyVmomi.vim.vm.FeatureRequirement import FeatureRequirement

class FeatureEVCMode(ElementDescription):
   mask: list[FeatureMask] = []
   capability: list[FeatureCapability] = []
   requirement: list[FeatureRequirement] = []
