# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vim import AboutInfo
from pyVmomi.vim import AuthorizationManager
from pyVmomi.vim import CertificateManager
from pyVmomi.vim import CustomFieldsManager
from pyVmomi.vim import CustomizationSpecManager
from pyVmomi.vim import DatastoreNamespaceManager
from pyVmomi.vim import DiagnosticManager
from pyVmomi.vim import ExtensionManager
from pyVmomi.vim import FileManager
from pyVmomi.vim import Folder
from pyVmomi.vim import HealthUpdateManager
from pyVmomi.vim import IoFilterManager
from pyVmomi.vim import IpPoolManager
from pyVmomi.vim import LicenseManager
from pyVmomi.vim import LocalizationManager
from pyVmomi.vim import OverheadMemoryManager
from pyVmomi.vim import OvfManager
from pyVmomi.vim import PerformanceManager
from pyVmomi.vim import SearchIndex
from pyVmomi.vim import ServiceManager
from pyVmomi.vim import SessionManager
from pyVmomi.vim import SiteInfoManager
from pyVmomi.vim import StorageQueryManager
from pyVmomi.vim import StorageResourceManager
from pyVmomi.vim import TaskManager
from pyVmomi.vim import UserDirectory
from pyVmomi.vim import VirtualDiskManager
from pyVmomi.vim import VirtualizationManager

from pyVmomi.vmodl import DynamicData

from pyVmomi.vim.alarm import AlarmManager

from pyVmomi.vim.dvs import DistributedVirtualSwitchManager

from pyVmomi.vim.encryption import CryptoManager

from pyVmomi.vim.event import EventManager

from pyVmomi.vim.host import LocalAccountManager
from pyVmomi.vim.host import SnmpSystem

from pyVmomi.vim.option import OptionManager

from pyVmomi.vim.profile import ComplianceManager

from pyVmomi.vim.scheduler import ScheduledTaskManager

from pyVmomi.vim.tenant import TenantManager

from pyVmomi.vim.vcha import FailoverClusterConfigurator
from pyVmomi.vim.vcha import FailoverClusterManager

from pyVmomi.vim.view import ViewManager

from pyVmomi.vim.vm import GuestCustomizationManager

from pyVmomi.vim.vslm import VStorageObjectManagerBase

from pyVmomi.vmodl.query import PropertyCollector

from pyVmomi.vim.profile.cluster import ProfileManager

from pyVmomi.vim.profile.host import HostSpecificationManager
from pyVmomi.vim.profile.host import ProfileManager

from pyVmomi.vim.vm.check import CompatibilityChecker
from pyVmomi.vim.vm.check import ProvisioningChecker

from pyVmomi.vim.vm.guest import GuestOperationsManager

class ServiceInstanceContent(DynamicData):
   rootFolder: Folder
   propertyCollector: PropertyCollector
   viewManager: Optional[ViewManager] = None
   about: AboutInfo
   setting: Optional[OptionManager] = None
   userDirectory: Optional[UserDirectory] = None
   sessionManager: Optional[SessionManager] = None
   authorizationManager: Optional[AuthorizationManager] = None
   serviceManager: Optional[ServiceManager] = None
   perfManager: Optional[PerformanceManager] = None
   scheduledTaskManager: Optional[ScheduledTaskManager] = None
   alarmManager: Optional[AlarmManager] = None
   eventManager: Optional[EventManager] = None
   taskManager: Optional[TaskManager] = None
   extensionManager: Optional[ExtensionManager] = None
   customizationSpecManager: Optional[CustomizationSpecManager] = None
   guestCustomizationManager: Optional[GuestCustomizationManager] = None
   customFieldsManager: Optional[CustomFieldsManager] = None
   accountManager: Optional[LocalAccountManager] = None
   diagnosticManager: Optional[DiagnosticManager] = None
   licenseManager: Optional[LicenseManager] = None
   searchIndex: Optional[SearchIndex] = None
   fileManager: Optional[FileManager] = None
   datastoreNamespaceManager: Optional[DatastoreNamespaceManager] = None
   virtualDiskManager: Optional[VirtualDiskManager] = None
   virtualizationManager: Optional[VirtualizationManager] = None
   snmpSystem: Optional[SnmpSystem] = None
   vmProvisioningChecker: Optional[ProvisioningChecker] = None
   vmCompatibilityChecker: Optional[CompatibilityChecker] = None
   ovfManager: Optional[OvfManager] = None
   ipPoolManager: Optional[IpPoolManager] = None
   dvSwitchManager: Optional[DistributedVirtualSwitchManager] = None
   hostProfileManager: Optional[ProfileManager] = None
   clusterProfileManager: Optional[ProfileManager] = None
   complianceManager: Optional[ComplianceManager] = None
   localizationManager: Optional[LocalizationManager] = None
   storageResourceManager: Optional[StorageResourceManager] = None
   guestOperationsManager: Optional[GuestOperationsManager] = None
   overheadMemoryManager: Optional[OverheadMemoryManager] = None
   certificateManager: Optional[CertificateManager] = None
   ioFilterManager: Optional[IoFilterManager] = None
   vStorageObjectManager: Optional[VStorageObjectManagerBase] = None
   hostSpecManager: Optional[HostSpecificationManager] = None
   cryptoManager: Optional[CryptoManager] = None
   healthUpdateManager: Optional[HealthUpdateManager] = None
   failoverClusterConfigurator: Optional[FailoverClusterConfigurator] = None
   failoverClusterManager: Optional[FailoverClusterManager] = None
   tenantManager: Optional[TenantManager] = None
   siteInfoManager: Optional[SiteInfoManager] = None
   storageQueryManager: Optional[StorageQueryManager] = None
