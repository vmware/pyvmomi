# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vim import ElementDescription

from pyVmomi.vmodl import DynamicData

from pyVmomi.vim.option import OptionDef

class DvxClassInfo(DynamicData):
   deviceClass: ElementDescription
   vendorName: str
   sriovNic: bool
   configParams: list[OptionDef] = []
