# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.VmomiSupport import ManagedObject

from pyVmomi.vim import HostSystem

from pyVmomi.vmodl import DynamicData

from pyVmomi.vim.host import Capability
from pyVmomi.vim.host import DatastoreBrowser

from pyVmomi.vim.vm import ConfigOption
from pyVmomi.vim.vm import ConfigOptionDescriptor
from pyVmomi.vim.vm import ConfigTarget

class EnvironmentBrowser(ManagedObject):
   class ConfigOptionQuerySpec(DynamicData):
      key: Optional[str] = None
      host: Optional[HostSystem] = None
      guestId: list[str] = []

   @property
   def datastoreBrowser(self) -> Optional[DatastoreBrowser]: ...

   def QueryConfigOptionDescriptor(self) -> list[ConfigOptionDescriptor]: ...
   def QueryConfigOption(self, key: Optional[str], host: Optional[HostSystem]) -> Optional[ConfigOption]: ...
   def QueryConfigOptionEx(self, spec: Optional[ConfigOptionQuerySpec]) -> Optional[ConfigOption]: ...
   def QueryConfigTarget(self, host: Optional[HostSystem]) -> Optional[ConfigTarget]: ...
   def QueryTargetCapabilities(self, host: Optional[HostSystem]) -> Optional[Capability]: ...
