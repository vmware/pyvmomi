
vim.ServiceInstanceContent
==========================
  The `ServiceContent <vim/ServiceInstanceContent.rst>`_ data object defines properties for the ServiceInstance managed object. The ServiceInstance itself does not have directly-accessible properties because reading the properties of a managed object requires the use of a property collector, and the property collector itself is a property of the `ServiceInstance <vim/ServiceInstance.rst>`_ . For this reason, use the method `RetrieveServiceContent <vim/ServiceInstance.rst#retrieveContent>`_ to retrieve the `ServiceContent <vim/ServiceInstanceContent.rst>`_ object.
:extends: vmodl.DynamicData_

Attributes:
    rootFolder (`vim.Folder <vim/Folder.rst>`_):

       Reference to the top of the inventory managed by this service.
    propertyCollector (`vmodl.query.PropertyCollector <vmodl/query/PropertyCollector.rst>`_):

       Reference to a per-session object for retrieving properties and updates.
    viewManager (`vim.view.ViewManager <vim/view/ViewManager.rst>`_, optional):

       A singleton managed object for tracking custom sets of objects.
    about (`vim.AboutInfo <vim/AboutInfo.rst>`_):

       Information about the service, such as the software version.
    setting (`vim.option.OptionManager <vim/option/OptionManager.rst>`_, optional):

       Generic configuration for a management server. This is for example by vCenter to store the vCenter Settings. This is not used for a stand-alone host, instead the vim.host.ConfigManager.advancedOption is used.See `HostConfigManager <vim/host/ConfigManager.rst>`_ 
    userDirectory (`vim.UserDirectory <vim/UserDirectory.rst>`_, optional):

       A user directory managed object.
    sessionManager (`vim.SessionManager <vim/SessionManager.rst>`_, optional):

       Managed object for logging in and managing sessions.
    authorizationManager (`vim.AuthorizationManager <vim/AuthorizationManager.rst>`_, optional):

       Manages permissions for managed entities in the service.
    serviceManager (`vim.ServiceManager <vim/ServiceManager.rst>`_, optional):

       A singleton managed object that manages local services.
    perfManager (`vim.PerformanceManager <vim/PerformanceManager.rst>`_, optional):

       A singleton managed object that manages the collection and reporting of performance statistics.
    scheduledTaskManager (`vim.scheduler.ScheduledTaskManager <vim/scheduler/ScheduledTaskManager.rst>`_, optional):

       A singleton managed object that manages scheduled tasks.
    alarmManager (`vim.alarm.AlarmManager <vim/alarm/AlarmManager.rst>`_, optional):

       A singleton managed object that manages alarms.
    eventManager (`vim.event.EventManager <vim/event/EventManager.rst>`_, optional):

       A singleton managed object that manages events.
    taskManager (`vim.TaskManager <vim/TaskManager.rst>`_, optional):

       A singleton managed object that manages tasks.
    extensionManager (`vim.ExtensionManager <vim/ExtensionManager.rst>`_, optional):

       A singleton managed object that manages extensions.
    customizationSpecManager (`vim.CustomizationSpecManager <vim/CustomizationSpecManager.rst>`_, optional):

       A singleton managed object that manages saved guest customization specifications.
    customFieldsManager (`vim.CustomFieldsManager <vim/CustomFieldsManager.rst>`_, optional):

       A singleton managed object that managed custom fields.
    accountManager (`vim.host.LocalAccountManager <vim/host/LocalAccountManager.rst>`_, optional):

       A singleton managed object that manages host local user and group accounts.
    diagnosticManager (`vim.DiagnosticManager <vim/DiagnosticManager.rst>`_, optional):

       A singleton managed object that provides access to low-level log files.
    licenseManager (`vim.LicenseManager <vim/LicenseManager.rst>`_, optional):

       A singleton managed object that manages licensing
    searchIndex (`vim.SearchIndex <vim/SearchIndex.rst>`_, optional):

       A singleton managed object that allows search of the inventory
    fileManager (`vim.FileManager <vim/FileManager.rst>`_, optional):

       A singleton managed object that allows management of files present on datastores.
    datastoreNamespaceManager (`vim.DatastoreNamespaceManager <vim/DatastoreNamespaceManager.rst>`_, optional):

       Datastore Namespace manager. A singleton managed object that is used to manage manipulations related to datastores' namespaces.
    virtualDiskManager (`vim.VirtualDiskManager <vim/VirtualDiskManager.rst>`_, optional):

       A singleton managed object that allows management of virtual disks on datastores.
    virtualizationManager (`vim.VirtualizationManager <vim/VirtualizationManager.rst>`_, optional):

       A singleton managed object that manages the discovery, analysis, recommendation and virtualization of physical machines
    snmpSystem (`vim.host.SnmpSystem <vim/host/SnmpSystem.rst>`_, optional):

       A singleton managed object that allows SNMP configuration. Not set if not supported on a particular platform.
    vmProvisioningChecker (`vim.vm.check.ProvisioningChecker <vim/vm/check/ProvisioningChecker.rst>`_, optional):

       A singleton managed object that can answer questions about the feasibility of certain provisioning operations.
    vmCompatibilityChecker (`vim.vm.check.CompatibilityChecker <vim/vm/check/CompatibilityChecker.rst>`_, optional):

       A singleton managed object that can answer questions about compatibility of a virtual machine with a host.
    ovfManager (`vim.OvfManager <vim/OvfManager.rst>`_, optional):

       A singleton managed object that can generate OVF descriptors (export) and create vApps (single-VM or vApp container-based) from OVF descriptors (import).
    ipPoolManager (`vim.IpPoolManager <vim/IpPoolManager.rst>`_, optional):

       A singleton managed object that supports management of IpPool objects. IP pools are used when allocating IPv4 and IPv6 addresses to vApps.
    dvSwitchManager (`vim.dvs.DistributedVirtualSwitchManager <vim/dvs/DistributedVirtualSwitchManager.rst>`_, optional):

       A singleton managed object that provides relevant information of DistributedVirtualSwitch.
    hostProfileManager (`vim.profile.host.ProfileManager <vim/profile/host/ProfileManager.rst>`_, optional):

       A singleton managed object that manages the host profiles.
    clusterProfileManager (`vim.profile.cluster.ProfileManager <vim/profile/cluster/ProfileManager.rst>`_, optional):

       A singleton managed object that manages the cluster profiles.
    complianceManager (`vim.profile.ComplianceManager <vim/profile/ComplianceManager.rst>`_, optional):

       A singleton managed object that manages compliance aspects of entities.
    localizationManager (`vim.LocalizationManager <vim/LocalizationManager.rst>`_, optional):

       A singleton managed object that provides methods for retrieving message catalogs for client-side localization support.
    storageResourceManager (`vim.StorageResourceManager <vim/StorageResourceManager.rst>`_, optional):

       A singleton managed object that provides methods for storage resource management.
    guestOperationsManager (`vim.vm.guest.GuestOperationsManager <vim/vm/guest/GuestOperationsManager.rst>`_, optional):

       A singleton managed object that provides methods for guest operations.
