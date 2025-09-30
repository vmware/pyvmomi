# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.VmomiSupport import ManagedObject

from pyVmomi.vim.HostSystem import HostSystem

from pyVmomi.vmodl.DynamicData import DynamicData

from pyVmomi.vim.host.Capability import Capability

from pyVmomi.vim.host.DatastoreBrowser import DatastoreBrowser

from pyVmomi.vim.vm.ConfigOption import ConfigOption

from pyVmomi.vim.vm.ConfigOptionDescriptor import ConfigOptionDescriptor

from pyVmomi.vim.vm.ConfigTarget import ConfigTarget

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
