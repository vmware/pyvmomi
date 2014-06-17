.. _vim.Folder: ../vim/Folder.rst

.. _vim.AboutInfo: ../vim/AboutInfo.rst

.. _ServiceContent: ../vim/ServiceInstanceContent.rst

.. _vim.OvfManager: ../vim/OvfManager.rst

.. _vim.SearchIndex: ../vim/SearchIndex.rst

.. _vim.TaskManager: ../vim/TaskManager.rst

.. _ServiceInstance: ../vim/ServiceInstance.rst

.. _vim.FileManager: ../vim/FileManager.rst

.. _HostConfigManager: ../vim/host/ConfigManager.rst

.. _vim.UserDirectory: ../vim/UserDirectory.rst

.. _vim.IpPoolManager: ../vim/IpPoolManager.rst

.. _vmodl.DynamicData: ../vmodl/DynamicData.rst

.. _vim.LicenseManager: ../vim/LicenseManager.rst

.. _vim.ServiceManager: ../vim/ServiceManager.rst

.. _vim.SessionManager: ../vim/SessionManager.rst

.. _vim.host.SnmpSystem: ../vim/host/SnmpSystem.rst

.. _vim.view.ViewManager: ../vim/view/ViewManager.rst

.. _vim.ExtensionManager: ../vim/ExtensionManager.rst

.. _vim.DiagnosticManager: ../vim/DiagnosticManager.rst

.. _vim.alarm.AlarmManager: ../vim/alarm/AlarmManager.rst

.. _vim.PerformanceManager: ../vim/PerformanceManager.rst

.. _RetrieveServiceContent: ../vim/ServiceInstance.rst#retrieveContent

.. _vim.event.EventManager: ../vim/event/EventManager.rst

.. _vim.VirtualDiskManager: ../vim/VirtualDiskManager.rst

.. _vim.CustomFieldsManager: ../vim/CustomFieldsManager.rst

.. _vim.LocalizationManager: ../vim/LocalizationManager.rst

.. _vim.AuthorizationManager: ../vim/AuthorizationManager.rst

.. _vim.option.OptionManager: ../vim/option/OptionManager.rst

.. _vim.VirtualizationManager: ../vim/VirtualizationManager.rst

.. _vim.StorageResourceManager: ../vim/StorageResourceManager.rst

.. _vim.CustomizationSpecManager: ../vim/CustomizationSpecManager.rst

.. _vim.host.LocalAccountManager: ../vim/host/LocalAccountManager.rst

.. _vim.DatastoreNamespaceManager: ../vim/DatastoreNamespaceManager.rst

.. _vim.profile.ComplianceManager: ../vim/profile/ComplianceManager.rst

.. _vmodl.query.PropertyCollector: ../vmodl/query/PropertyCollector.rst

.. _vim.profile.host.ProfileManager: ../vim/profile/host/ProfileManager.rst

.. _vim.vm.check.ProvisioningChecker: ../vim/vm/check/ProvisioningChecker.rst

.. _vim.vm.check.CompatibilityChecker: ../vim/vm/check/CompatibilityChecker.rst

.. _vim.profile.cluster.ProfileManager: ../vim/profile/cluster/ProfileManager.rst

.. _vim.scheduler.ScheduledTaskManager: ../vim/scheduler/ScheduledTaskManager.rst

.. _vim.vm.guest.GuestOperationsManager: ../vim/vm/guest/GuestOperationsManager.rst

.. _vim.dvs.DistributedVirtualSwitchManager: ../vim/dvs/DistributedVirtualSwitchManager.rst


vim.ServiceInstanceContent
==========================
  The `ServiceContent`_ data object defines properties for the ServiceInstance managed object. The ServiceInstance itself does not have directly-accessible properties because reading the properties of a managed object requires the use of a property collector, and the property collector itself is a property of the `ServiceInstance`_ . For this reason, use the method `RetrieveServiceContent`_ to retrieve the `ServiceContent`_ object.
:extends: vmodl.DynamicData_

Attributes:
    rootFolder (`vim.Folder`_):

       Reference to the top of the inventory managed by this service.
    propertyCollector (`vmodl.query.PropertyCollector`_):

       Reference to a per-session object for retrieving properties and updates.
    viewManager (`vim.view.ViewManager`_, optional):

       A singleton managed object for tracking custom sets of objects.
    about (`vim.AboutInfo`_):

       Information about the service, such as the software version.
    setting (`vim.option.OptionManager`_, optional):

       Generic configuration for a management server. This is for example by vCenter to store the vCenter Settings. This is not used for a stand-alone host, instead the vim.host.ConfigManager.advancedOption is used.See `HostConfigManager`_ 
    userDirectory (`vim.UserDirectory`_, optional):

       A user directory managed object.
    sessionManager (`vim.SessionManager`_, optional):

       Managed object for logging in and managing sessions.
    authorizationManager (`vim.AuthorizationManager`_, optional):

       Manages permissions for managed entities in the service.
    serviceManager (`vim.ServiceManager`_, optional):

       A singleton managed object that manages local services.
    perfManager (`vim.PerformanceManager`_, optional):

       A singleton managed object that manages the collection and reporting of performance statistics.
    scheduledTaskManager (`vim.scheduler.ScheduledTaskManager`_, optional):

       A singleton managed object that manages scheduled tasks.
    alarmManager (`vim.alarm.AlarmManager`_, optional):

       A singleton managed object that manages alarms.
    eventManager (`vim.event.EventManager`_, optional):

       A singleton managed object that manages events.
    taskManager (`vim.TaskManager`_, optional):

       A singleton managed object that manages tasks.
    extensionManager (`vim.ExtensionManager`_, optional):

       A singleton managed object that manages extensions.
    customizationSpecManager (`vim.CustomizationSpecManager`_, optional):

       A singleton managed object that manages saved guest customization specifications.
    customFieldsManager (`vim.CustomFieldsManager`_, optional):

       A singleton managed object that managed custom fields.
    accountManager (`vim.host.LocalAccountManager`_, optional):

       A singleton managed object that manages host local user and group accounts.
    diagnosticManager (`vim.DiagnosticManager`_, optional):

       A singleton managed object that provides access to low-level log files.
    licenseManager (`vim.LicenseManager`_, optional):

       A singleton managed object that manages licensing
    searchIndex (`vim.SearchIndex`_, optional):

       A singleton managed object that allows search of the inventory
    fileManager (`vim.FileManager`_, optional):

       A singleton managed object that allows management of files present on datastores.
    datastoreNamespaceManager (`vim.DatastoreNamespaceManager`_, optional):

       Datastore Namespace manager. A singleton managed object that is used to manage manipulations related to datastores' namespaces.
    virtualDiskManager (`vim.VirtualDiskManager`_, optional):

       A singleton managed object that allows management of virtual disks on datastores.
    virtualizationManager (`vim.VirtualizationManager`_, optional):

       A singleton managed object that manages the discovery, analysis, recommendation and virtualization of physical machines
    snmpSystem (`vim.host.SnmpSystem`_, optional):

       A singleton managed object that allows SNMP configuration. Not set if not supported on a particular platform.
    vmProvisioningChecker (`vim.vm.check.ProvisioningChecker`_, optional):

       A singleton managed object that can answer questions about the feasibility of certain provisioning operations.
    vmCompatibilityChecker (`vim.vm.check.CompatibilityChecker`_, optional):

       A singleton managed object that can answer questions about compatibility of a virtual machine with a host.
    ovfManager (`vim.OvfManager`_, optional):

       A singleton managed object that can generate OVF descriptors (export) and create vApps (single-VM or vApp container-based) from OVF descriptors (import).
    ipPoolManager (`vim.IpPoolManager`_, optional):

       A singleton managed object that supports management of IpPool objects. IP pools are used when allocating IPv4 and IPv6 addresses to vApps.
    dvSwitchManager (`vim.dvs.DistributedVirtualSwitchManager`_, optional):

       A singleton managed object that provides relevant information of DistributedVirtualSwitch.
    hostProfileManager (`vim.profile.host.ProfileManager`_, optional):

       A singleton managed object that manages the host profiles.
    clusterProfileManager (`vim.profile.cluster.ProfileManager`_, optional):

       A singleton managed object that manages the cluster profiles.
    complianceManager (`vim.profile.ComplianceManager`_, optional):

       A singleton managed object that manages compliance aspects of entities.
    localizationManager (`vim.LocalizationManager`_, optional):

       A singleton managed object that provides methods for retrieving message catalogs for client-side localization support.
    storageResourceManager (`vim.StorageResourceManager`_, optional):

       A singleton managed object that provides methods for storage resource management.
    guestOperationsManager (`vim.vm.guest.GuestOperationsManager`_, optional):

       A singleton managed object that provides methods for guest operations.
