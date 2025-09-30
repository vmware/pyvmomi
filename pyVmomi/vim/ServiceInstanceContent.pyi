# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vim.AboutInfo import AboutInfo

from pyVmomi.vim.AuthorizationManager import AuthorizationManager

from pyVmomi.vim.CertificateManager import CertificateManager

from pyVmomi.vim.CustomFieldsManager import CustomFieldsManager

from pyVmomi.vim.CustomizationSpecManager import CustomizationSpecManager

from pyVmomi.vim.DatastoreNamespaceManager import DatastoreNamespaceManager

from pyVmomi.vim.DiagnosticManager import DiagnosticManager

from pyVmomi.vim.DirectPathProfileManager import DirectPathProfileManager

from pyVmomi.vim.ExtensionManager import ExtensionManager

from pyVmomi.vim.FileManager import FileManager

from pyVmomi.vim.Folder import Folder

from pyVmomi.vim.HealthUpdateManager import HealthUpdateManager

from pyVmomi.vim.IoFilterManager import IoFilterManager

from pyVmomi.vim.IpPoolManager import IpPoolManager

from pyVmomi.vim.LicenseManager import LicenseManager

from pyVmomi.vim.LocalizationManager import LocalizationManager

from pyVmomi.vim.OverheadMemoryManager import OverheadMemoryManager

from pyVmomi.vim.OvfManager import OvfManager

from pyVmomi.vim.PerformanceManager import PerformanceManager

from pyVmomi.vim.SearchIndex import SearchIndex

from pyVmomi.vim.ServiceManager import ServiceManager

from pyVmomi.vim.SessionManager import SessionManager

from pyVmomi.vim.SiteInfoManager import SiteInfoManager

from pyVmomi.vim.StorageQueryManager import StorageQueryManager

from pyVmomi.vim.StorageResourceManager import StorageResourceManager

from pyVmomi.vim.TaskManager import TaskManager

from pyVmomi.vim.UserDirectory import UserDirectory

from pyVmomi.vim.VirtualDiskManager import VirtualDiskManager

from pyVmomi.vim.VirtualizationManager import VirtualizationManager

from pyVmomi.vmodl.DynamicData import DynamicData

from pyVmomi.vim.alarm.AlarmManager import AlarmManager

from pyVmomi.vim.dvs.DistributedVirtualSwitchManager import DistributedVirtualSwitchManager

from pyVmomi.vim.encryption.CryptoManager import CryptoManager

from pyVmomi.vim.event.EventManager import EventManager

from pyVmomi.vim.host.LocalAccountManager import LocalAccountManager

from pyVmomi.vim.host.SnmpSystem import SnmpSystem

from pyVmomi.vim.option.OptionManager import OptionManager

from pyVmomi.vim.profile.ComplianceManager import ComplianceManager

from pyVmomi.vim.scheduler.ScheduledTaskManager import ScheduledTaskManager

from pyVmomi.vim.tenant.TenantManager import TenantManager

from pyVmomi.vim.vcha.FailoverClusterConfigurator import FailoverClusterConfigurator

from pyVmomi.vim.vcha.FailoverClusterManager import FailoverClusterManager

from pyVmomi.vim.view.ViewManager import ViewManager

from pyVmomi.vim.vm.GuestCustomizationManager import GuestCustomizationManager

from pyVmomi.vim.vslm.VStorageObjectManagerBase import VStorageObjectManagerBase

from pyVmomi.vmodl.query.PropertyCollector import PropertyCollector

from pyVmomi.vim.profile.cluster.ProfileManager import ProfileManager

from pyVmomi.vim.profile.host.HostSpecificationManager import HostSpecificationManager

from pyVmomi.vim.profile.host.ProfileManager import ProfileManager

from pyVmomi.vim.vm.check.CompatibilityChecker import CompatibilityChecker

from pyVmomi.vim.vm.check.ProvisioningChecker import ProvisioningChecker

from pyVmomi.vim.vm.guest.GuestOperationsManager import GuestOperationsManager

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
   directPathProfileManager: Optional[DirectPathProfileManager] = None
