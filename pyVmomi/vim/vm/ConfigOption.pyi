# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vmodl.DynamicData import DynamicData

from pyVmomi.vim.vm.Capability import Capability

from pyVmomi.vim.vm.DatastoreOption import DatastoreOption

from pyVmomi.vim.vm.GuestOsDescriptor import GuestOsDescriptor

from pyVmomi.vim.vm.PropertyRelation import PropertyRelation

from pyVmomi.vim.vm.VirtualHardwareOption import VirtualHardwareOption

from pyVmomi.vim.vm.device.VirtualDevice import VirtualDevice

class ConfigOption(DynamicData):
   version: str
   description: str
   guestOSDescriptor: list[GuestOsDescriptor] = []
   guestOSDefaultIndex: int
   hardwareOptions: VirtualHardwareOption
   capabilities: Capability
   datastore: DatastoreOption
   defaultDevice: list[VirtualDevice] = []
   supportedMonitorType: list[str] = []
   supportedOvfEnvironmentTransport: list[str] = []
   supportedOvfInstallTransport: list[str] = []
   propertyRelations: list[PropertyRelation] = []
