# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from pyVmomi.vim import ExtendedElementDescription

from pyVmomi.vmodl import DynamicData

from pyVmomi.vim.profile import PolicyOptionMetadata

class PolicyMetadata(DynamicData):
   id: ExtendedElementDescription
   possibleOption: list[PolicyOptionMetadata] = []
