# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vmodl import DynamicData

class UsbScanCodeSpec(DynamicData):
   class ModifierType(DynamicData):
      leftControl: Optional[bool] = None
      leftShift: Optional[bool] = None
      leftAlt: Optional[bool] = None
      leftGui: Optional[bool] = None
      rightControl: Optional[bool] = None
      rightShift: Optional[bool] = None
      rightAlt: Optional[bool] = None
      rightGui: Optional[bool] = None

   class KeyEvent(DynamicData):
      usbHidCode: int
      modifiers: Optional[ModifierType] = None

   keyEvents: list[KeyEvent] = []
