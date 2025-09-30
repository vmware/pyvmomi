# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vim.OvfConsumer import OvfConsumer

from pyVmomi.vmodl.DynamicData import DynamicData

from pyVmomi.vim.vApp.EntityConfigInfo import EntityConfigInfo

class ImportSpec(DynamicData):
   entityConfig: Optional[EntityConfigInfo] = None
   instantiationOst: Optional[OvfConsumer.OstNode] = None
