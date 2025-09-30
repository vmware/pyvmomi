# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vim.KeyValue import KeyValue

from pyVmomi.vim.VirtualMachine import VirtualMachine

from pyVmomi.vmodl.DynamicData import DynamicData

class VsanObjectIdentity(DynamicData):
   uuid: str
   type: str
   vmInstanceUuid: Optional[str] = None
   vmNsObjectUuid: Optional[str] = None
   vm: Optional[VirtualMachine] = None
   description: Optional[str] = None
   spbmProfileUuid: Optional[str] = None
   metadatas: list[KeyValue] = []
   typeExtId: Optional[str] = None
   spbmProfileName: Optional[str] = None
