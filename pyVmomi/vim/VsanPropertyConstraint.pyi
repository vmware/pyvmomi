# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vim import VsanResourceConstraint

from pyVmomi.vmodl import KeyAnyValue

class VsanPropertyConstraint(VsanResourceConstraint):
   propertyName: Optional[str] = None
   comparator: Optional[str] = None
   comparableValue: Optional[KeyAnyValue] = None
