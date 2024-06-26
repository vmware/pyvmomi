# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vmodl import DynamicData
from pyVmomi.vmodl import KeyAnyValue

from pyVmomi.vim.host import ActiveDirectorySpec
from pyVmomi.vim.host import AssignableHardwareConfig
from pyVmomi.vim.host import DateTimeConfig
from pyVmomi.vim.host import FirewallConfig
from pyVmomi.vim.host import GraphicsConfig
from pyVmomi.vim.host import LicenseSpec
from pyVmomi.vim.host import LocalAccountManager
from pyVmomi.vim.host import MemorySpec
from pyVmomi.vim.host import NasVolume
from pyVmomi.vim.host import NetworkConfig
from pyVmomi.vim.host import SecuritySpec
from pyVmomi.vim.host import ServiceConfig
from pyVmomi.vim.host import StorageDeviceInfo
from pyVmomi.vim.host import VirtualNicManager

from pyVmomi.vim.option import OptionValue

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
