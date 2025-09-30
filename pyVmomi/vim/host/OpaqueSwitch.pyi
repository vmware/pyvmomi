# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import ClassVar
from typing import Optional

from pyVmomi.VmomiSupport import Enum

from pyVmomi.vmodl.DynamicData import DynamicData

from pyVmomi.vim.host.FeatureCapability import FeatureCapability

from pyVmomi.vim.host.PhysicalNic import PhysicalNic

from pyVmomi.vim.host.VirtualNic import VirtualNic

from pyVmomi.vim.option.OptionValue import OptionValue

class OpaqueSwitch(DynamicData):
   class OpaqueSwitchState(Enum):
      up: ClassVar['OpaqueSwitchState'] = 'up'
      warning: ClassVar['OpaqueSwitchState'] = 'warning'
      down: ClassVar['OpaqueSwitchState'] = 'down'
      maintenance: ClassVar['OpaqueSwitchState'] = 'maintenance'

   class PhysicalNicZone(DynamicData):
      key: str
      pnicDevice: list[str] = []

   key: str
   name: Optional[str] = None
   pnic: list[PhysicalNic] = []
   pnicZone: list[PhysicalNicZone] = []
   status: Optional[str] = None
   vtep: list[VirtualNic] = []
   extraConfig: list[OptionValue] = []
   featureCapability: list[FeatureCapability] = []
