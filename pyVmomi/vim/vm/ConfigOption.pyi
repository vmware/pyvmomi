# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vmodl import DynamicData

from pyVmomi.vim.vm import Capability
from pyVmomi.vim.vm import DatastoreOption
from pyVmomi.vim.vm import GuestOsDescriptor
from pyVmomi.vim.vm import PropertyRelation
from pyVmomi.vim.vm import VirtualHardwareOption

from pyVmomi.vim.vm.device import VirtualDevice

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
