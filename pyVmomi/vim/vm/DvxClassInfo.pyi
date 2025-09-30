# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vim.ElementDescription import ElementDescription

from pyVmomi.vmodl.DynamicData import DynamicData

from pyVmomi.vim.option.OptionDef import OptionDef

class DvxClassInfo(DynamicData):
   deviceClass: ElementDescription
   vendorName: str
   sriovNic: bool
   configParams: list[OptionDef] = []
