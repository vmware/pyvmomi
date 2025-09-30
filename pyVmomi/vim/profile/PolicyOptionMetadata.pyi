# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vim.ExtendedElementDescription import ExtendedElementDescription

from pyVmomi.vmodl.DynamicData import DynamicData

from pyVmomi.vim.profile.ParameterMetadata import ParameterMetadata

class PolicyOptionMetadata(DynamicData):
   id: ExtendedElementDescription
   parameter: list[ParameterMetadata] = []
