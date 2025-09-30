# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.VmomiSupport import ManagedObject

from pyVmomi.vim.option.OptionDef import OptionDef

from pyVmomi.vim.option.OptionValue import OptionValue

class OptionManager(ManagedObject):
   @property
   def supportedOption(self) -> list[OptionDef]: ...
   @property
   def setting(self) -> list[OptionValue]: ...

   def QueryView(self, name: Optional[str]) -> list[OptionValue]: ...
   def UpdateValues(self, changedValue: list[OptionValue]) -> None: ...
