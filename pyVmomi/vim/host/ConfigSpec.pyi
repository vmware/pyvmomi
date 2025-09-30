# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vmodl.DynamicData import DynamicData

from pyVmomi.vmodl.KeyAnyValue import KeyAnyValue

from pyVmomi.vim.host.ActiveDirectorySpec import ActiveDirectorySpec

from pyVmomi.vim.host.AssignableHardwareConfig import AssignableHardwareConfig

from pyVmomi.vim.host.DateTimeConfig import DateTimeConfig

from pyVmomi.vim.host.FirewallConfig import FirewallConfig

from pyVmomi.vim.host.GraphicsConfig import GraphicsConfig

from pyVmomi.vim.host.LicenseSpec import LicenseSpec

from pyVmomi.vim.host.LocalAccountManager import LocalAccountManager

from pyVmomi.vim.host.MemorySpec import MemorySpec

from pyVmomi.vim.host.NasVolume import NasVolume

from pyVmomi.vim.host.NetworkConfig import NetworkConfig

from pyVmomi.vim.host.SecuritySpec import SecuritySpec

from pyVmomi.vim.host.ServiceConfig import ServiceConfig

from pyVmomi.vim.host.StorageDeviceInfo import StorageDeviceInfo

from pyVmomi.vim.host.VirtualNicManager import VirtualNicManager

from pyVmomi.vim.option.OptionValue import OptionValue

class ConfigSpec(DynamicData):
   nasDatastore: list[NasVolume.Config] = []
   network: Optional[NetworkConfig] = None
   nicTypeSelection: list[VirtualNicManager.NicTypeSelection] = []
   service: list[ServiceConfig] = []
   firewall: Optional[FirewallConfig] = None
   option: list[OptionValue] = []
   datastorePrincipal: Optional[str] = None
   datastorePrincipalPasswd: Optional[str] = None
   datetime: Optional[DateTimeConfig] = None
   storageDevice: Optional[StorageDeviceInfo] = None
   license: Optional[LicenseSpec] = None
   security: Optional[SecuritySpec] = None
   userAccount: list[LocalAccountManager.AccountSpecification] = []
   usergroupAccount: list[LocalAccountManager.AccountSpecification] = []
   memory: Optional[MemorySpec] = None
   activeDirectory: list[ActiveDirectorySpec] = []
   genericConfig: list[KeyAnyValue] = []
   graphicsConfig: Optional[GraphicsConfig] = None
   assignableHardwareConfig: Optional[AssignableHardwareConfig] = None
