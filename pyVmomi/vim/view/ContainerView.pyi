# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vim import ManagedEntity

from pyVmomi.vim.view import ManagedObjectView

class ContainerView(ManagedObjectView):
   @property
   def container(self) -> ManagedEntity: ...
   @property
   def type(self) -> list[type]: ...
   @property
   def recursive(self) -> bool: ...
