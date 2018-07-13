.. _int: https://docs.python.org/2/library/stdtypes.html

.. _long: https://docs.python.org/2/library/stdtypes.html

.. _bool: https://docs.python.org/2/library/stdtypes.html

.. _vim.Task: ../vim/Task.rst

.. _hardware: ../vim/HostSystem.rst#hardware

.. _VI API 2.5: ../vim/version.rst#vimversionversion2

.. _vim.Network: ../vim/Network.rst

.. _HostIpmiInfo: ../vim/host/IpmiInfo.rst

.. _HostFlagInfo: ../vim/host/FlagInfo.rst

.. _vim.Datastore: ../vim/Datastore.rst

.. _adminDisabled: ../vim/host/ConfigInfo.rst#adminDisabled

.. _LicenseManager: ../vim/LicenseManager.rst

.. _vSphere API 5.1: ../vim/version.rst#vimversionversion8

.. _vSphere API 5.0: ../vim/version.rst#vimversionversion7

.. _vSphere API 4.0: ../vim/version.rst#vimversionversion5

.. _vSphere API 4.1: ../vim/version.rst#vimversionversion6

.. _vim.host.Summary: ../vim/host/Summary.rst

.. _standbySupported: ../vim/host/Capability.rst#standbySupported

.. _vim.fault.NoHost: ../vim/fault/NoHost.rst

.. _vim.vm.ConfigInfo: ../vim/vm/ConfigInfo.rst

.. _vim.host.FlagInfo: ../vim/host/FlagInfo.rst

.. _shutdownSupported: ../vim/host/Capability.rst#shutdownSupported

.. _vim.ManagedEntity: ../vim/ManagedEntity.rst

.. _vim.host.IpmiInfo: ../vim/host/IpmiInfo.rst

.. _EnterLockdownMode: ../vim/HostSystem.rst#enterLockdownMode

.. _vim.fault.Timedout: ../vim/fault/Timedout.rst

.. _vim.VirtualMachine: ../vim/VirtualMachine.rst

.. _vim.host.Capability: ../vim/host/Capability.rst

.. _vim.host.ConfigInfo: ../vim/host/ConfigInfo.rst

.. _vim.host.ConnectInfo: ../vim/host/ConnectInfo.rst

.. _AuthorizationManager: ../vim/AuthorizationManager.rst

.. _vim.host.RuntimeInfo: ../vim/host/RuntimeInfo.rst

.. _vim.host.ConnectSpec: ../vim/host/ConnectSpec.rst

.. _vim.fault.InvalidName: ../vim/fault/InvalidName.rst

.. _vim.HostServiceTicket: ../vim/HostServiceTicket.rst

.. _vim.host.HardwareInfo: ../vim/host/HardwareInfo.rst

.. _vim.fault.InvalidLogin: ../vim/fault/InvalidLogin.rst

.. _vim.host.ConfigManager: ../vim/host/ConfigManager.rst

.. _vim.fault.InvalidState: ../vim/fault/InvalidState.rst

.. _vim.fault.AdminDisabled: ../vim/fault/AdminDisabled.rst

.. _vim.host.MaintenanceSpec: ../vim/host/MaintenanceSpec.rst

.. _vmodl.fault.NotSupported: ../vmodl/fault/NotSupported.rst

.. _vim.fault.SSLVerifyFault: ../vim/fault/SSLVerifyFault.rst

.. _vim.fault.DasConfigFault: ../vim/fault/DasConfigFault.rst

.. _vim.host.DatastoreBrowser: ../vim/host/DatastoreBrowser.rst

.. _vim.fault.HostConfigFault: ../vim/fault/HostConfigFault.rst

.. _vim.fault.AdminNotDisabled: ../vim/fault/AdminNotDisabled.rst

.. _vim.fault.NotSupportedHost: ../vim/fault/NotSupportedHost.rst

.. _vim.fault.HostConnectFault: ../vim/fault/HostConnectFault.rst

.. _HostSystemSwapConfiguration: ../vim/host/SystemSwapConfiguration.rst

.. _vmodl.fault.InvalidArgument: ../vmodl/fault/InvalidArgument.rst

.. _vim.fault.HostPowerOpFailed: ../vim/fault/HostPowerOpFailed.rst

.. _vmodl.fault.RequestCanceled: ../vmodl/fault/RequestCanceled.rst

.. _vim.host.SystemResourceInfo: ../vim/host/SystemResourceInfo.rst

.. _vim.HostSystem.ReconnectSpec: ../vim/HostSystem/ReconnectSpec.rst

.. _vim.host.TpmAttestationReport: ../vim/host/TpmAttestationReport.rst

.. _vim.fault.AlreadyBeingManaged: ../vim/fault/AlreadyBeingManaged.rst

.. _vmodl.fault.NotEnoughLicenses: ../vmodl/fault/NotEnoughLicenses.rst

.. _vim.fault.InvalidIpmiLoginInfo: ../vim/fault/InvalidIpmiLoginInfo.rst

.. _vim.fault.InvalidIpmiMacAddress: ../vim/fault/InvalidIpmiMacAddress.rst

.. _vim.host.SystemSwapConfiguration: ../vim/host/SystemSwapConfiguration.rst

.. _vim.fault.DisableAdminNotSupported: ../vim/fault/DisableAdminNotSupported.rst

.. _vim.host.Capability.rebootSupported: ../vim/host/Capability.rst#rebootSupported

.. _vim.LicenseManager.LicensableResourceInfo: ../vim/LicenseManager/LicensableResourceInfo.rst


vim.HostSystem
==============
  The HostSystem managed object type provides access to a virtualization host platform.Invoking destroy on a HostSystem of standalone type throws a NotSupported fault. A standalone HostSystem can be destroyed only by invoking destroy on its parent ComputeResource. Invoking destroy on a failover host throws a `DisallowedOperationOnFailoverHost`_ fault. See `ClusterFailoverHostAdmissionControlPolicy`_ .


:extends: vim.ManagedEntity_


Attributes
----------
    runtime (`vim.host.RuntimeInfo`_):
       Runtime state information about the host such as connection state.
    summary (`vim.host.Summary`_):
       Basic information about the host, including connection state.
    hardware (`vim.host.HardwareInfo`_):
       Hardware configuration of the host. This might not be available for a disconnected host.
    capability (`vim.host.Capability`_):
       Host capabilities. This might not be available for a disconnected host.
    licensableResource (`vim.LicenseManager.LicensableResourceInfo`_):
       Information about all licensable resources, currently present on this host.This information is used mostly by the modules, manipulating information in the `LicenseManager`_ . Developers of such modules should use this property instead of `hardware`_ .NOTE: The values in this property may not be accurate for pre-5.0 hosts when returned by vCenter 5.0
    configManager (`vim.host.ConfigManager`_):
       Host configuration systems. In releases after vSphere API 5.0, vSphere Servers might not generate property collector update notifications for this property. To obtain the latest value of the property, you can use PropertyCollector methods RetrievePropertiesEx or WaitForUpdatesEx. If you use the PropertyCollector.WaitForUpdatesEx method, specify an empty string for the version parameter. Any other version value will not produce any property values as no updates are generated.
    config (`vim.host.ConfigInfo`_):
       Host configuration information. This might not be available for a disconnected host.
    vm ([`vim.VirtualMachine`_]):
       List of virtual machines associated with this host.
    datastore ([`vim.Datastore`_]):
      privilege: System.View
       A collection of references to the subset of datastore objects in the datacenter that are available in this HostSystem.
    network ([`vim.Network`_]):
      privilege: System.View
       A collection of references to the subset of network objects in the datacenter that are available in this HostSystem.
    datastoreBrowser (`vim.host.DatastoreBrowser`_):
      privilege: System.View
       DatastoreBrowser to browse datastores for this host.
    systemResources (`vim.host.SystemResourceInfo`_):
       Reference for the system resource hierarchy, used for configuring the set of resources reserved to the system and unavailable to virtual machines.


Methods
-------


QueryTpmAttestationReport():
   Basic information about TPM attestation state of the host.
  since: `vSphere API 5.1`_


  Privilege:
               System.Read



  Args:


  Returns:
    `vim.host.TpmAttestationReport`_:



QueryHostConnectionInfo():
   Connection-oriented information about a host.


  Privilege:
               System.Read



  Args:


  Returns:
    `vim.host.ConnectInfo`_:



UpdateSystemResources(resourceInfo):
   Update the configuration of the system resource hierarchy.


  Privilege:
               Host.Config.Resources



  Args:
    resourceInfo (`vim.host.SystemResourceInfo`_):




  Returns:
    None


  Raises:

    `vmodl.fault.InvalidArgument`_:
       if the resource specification is invalid.


UpdateSystemSwapConfiguration(sysSwapConfig):
   Update the System Swap Configuration.See `HostSystemSwapConfiguration`_
  since: `vSphere API 5.1`_


  Privilege:
               Host.Config.Settings



  Args:
    sysSwapConfig (`vim.host.SystemSwapConfiguration`_):
       Contains a list of system swap options that configure the system swap functionality.See `HostSystemSwapConfiguration`_




  Returns:
    None


  Raises:

    `vmodl.fault.InvalidArgument`_:
       if the supplied sysSwapConfig is not correct.See `HostSystemSwapConfiguration`_


ReconnectHost(cnxSpec, reconnectSpec):
   Reconnects to a host. This process reinstalls agents and reconfigures the host, if it has gotten out of date with VirtualCenter. The reconnection process goes through many of the same steps as addHost: ensuring the correct set of licenses for the number of CPUs on the host, ensuring the correct set of agents is installed, and ensuring that networks and datastores are discovered and registered with VirtualCenter.The client can change the IP address and port of the host when doing a reconnect operation. This can be useful if the client wants to preserve existing metadata, even though the host is changing its IP address. For example, clients could preserve existing statistics, alarms, and privileges.This method can also be used to change the SSL thumbprint of a connected host without disconnecting it.Any changes made to the resource hierarchy on the host when the host was disconnected are overridden by VirtualCenter settings on reconnect.This method is only supported through VirtualCenter.


  Privilege:
               Host.Config.Connection



  Args:
    cnxSpec (`vim.host.ConnectSpec`_, optional):
       Includes the parameters to use, including user name and password, when reconnecting to the host. If this parameter is not specified, the default connection parameters is used.


    reconnectSpec (`vim.HostSystem.ReconnectSpec`_, optional, since `vSphere API 5.0`_ ):
       Includes connection parameters specific to reconnect. This will mainly be used to indicate how to handle divergence between the host settings and vCenter Server settings when the host was disconnected.




  Returns:
     `vim.Task`_:


  Raises:

    `vim.fault.InvalidLogin`_:
       if the method fails to authenticate with the host.

    `vim.fault.InvalidState`_:
       if the host is not disconnected.

    `vim.fault.InvalidName`_:
       if the host name is invalid.

    `vim.fault.HostConnectFault`_:
       if an error occurred when attempting to reconnect to a host. Typically, a more specific subclass, such as AlreadyBeingManaged, is thrown.

    `vmodl.fault.NotSupported`_:
       if no host can be added to this group. This is the case if the ComputeResource is a standalone type.

    `vim.fault.AlreadyBeingManaged`_:
       if host is already being managed by another VirtualCenter server

    `vmodl.fault.NotEnoughLicenses`_:
       if there are not enough licenses to add this host.

    `vim.fault.NoHost`_:
       if the method is unable to contact the server.

    `vim.fault.NotSupportedHost`_:
       if the host is running a software version that is not supported.

    `vim.fault.SSLVerifyFault`_:
       if the host certificate could not be authenticated.


DisconnectHost():
   Disconnects from a host and instructs the server to stop sending heartbeats.


  Privilege:
               Host.Config.Connection



  Args:


  Returns:
     `vim.Task`_:


  Raises:

    `vmodl.fault.NotSupported`_:
       if run directly on an ESX Server host.


EnterMaintenanceMode(timeout, evacuatePoweredOffVms, maintenanceSpec):
   Puts the host in maintenance mode. While this task is running and when the host is in maintenance mode, no virtual machines can be powered on and no provisioning operations can be performed on the host. Once the call completes, it is safe to turn off a host without disrupting any virtual machines.The task completes once there are no powered-on virtual machines on the host and no provisioning operations in progress on the host. The operation does not directly initiate any operations to evacuate or power-down powered-on virtual machines. However, if the host is part of a cluster with VMware DRS enabled, DRS provides migration recommendations to evacuate the powered-on virtual machines. If DRS is in fully-automatic mode, these are automatically scheduled.If the host is part of a cluster and the task is issued through VirtualCenter with evacuatePoweredOffVms set to true, the task will not succeed unless all the powered-off virtual machines are reregistered to other hosts. If VMware DRS is enabled, vCenter Server will automatically evacuate powered-off virtual machines. The task is cancellable.


  Privilege:
               Host.Config.Maintenance



  Args:
    timeout (`int`_):
       The task completes when the host successfully enters maintenance mode or the timeout expires, and in the latter case the task contains a Timeout fault. If the timeout is less than or equal to zero, there is no timeout. The timeout is specified in seconds.


    evacuatePoweredOffVms (`bool`_, optional, since `VI API 2.5`_ ):
       This is a parameter only supported by VirtualCenter. If set to true, for a DRS disabled cluster, the task will not succeed unless all powered-off virtual machines have been manually reregistered; for a DRS enabled cluster, VirtualCenter will automatically reregister powered-off virtual machines and a powered-off virtual machine may remain at the host only for two reasons: (a) no compatible host found for reregistration, (b) DRS is disabled for the virtual machine. If set to false, powered-off virtual machines do not need to be moved.


    maintenanceSpec (`vim.host.MaintenanceSpec`_, optional, since `vSphere API 5.5`_ ):
       Any additional actions to be taken by the host upon entering maintenance mode. If omitted, default actions will be taken as documented in the `HostMaintenanceSpec`_ .




  Returns:
     `vim.Task`_:


  Raises:

    `vim.fault.InvalidState`_:
       if the host is already in maintenance mode.

    `vim.fault.Timedout`_:
       if the operation timed out.

    `vmodl.fault.RequestCanceled`_:
       if the operation is canceled.


ExitMaintenanceMode(timeout):
   Takes the host out of maintenance mode. This blocks if any concurrent running maintenance-only host configurations operations are being performed. For example, if VMFS volumes are being upgraded.The task is cancellable.


  Privilege:
               Host.Config.Maintenance



  Args:
    timeout (`int`_):
       Number of seconds to wait for the exit maintenance mode to succeed. If the timeout is less than or equal to zero, there is no timeout.




  Returns:
     `vim.Task`_:


  Raises:

    `vim.fault.InvalidState`_:
       if the host is not in maintenance mode.

    `vim.fault.Timedout`_:
       vim.fault.Timedout


RebootHost(force):
   Reboots a host. If the command is successful, then the host has been rebooted. If connected directly to the host, the client never receives an indicator of success in the returned task but simply loses connection to the host, upon success.This command is not supported on all hosts. Check the host capability `vim.host.Capability.rebootSupported`_ .


  Privilege:
               Host.Config.Maintenance



  Args:
    force (`bool`_):
       Flag to specify whether or not the host should be rebooted regardless of whether it is in maintenance mode. If true, the host is rebooted, even if there are virtual machines running or other operations in progress.




  Returns:
     `vim.Task`_:


  Raises:

    `vim.fault.InvalidState`_:
       if "force" is false and the host is not in maintenance mode.

    `vmodl.fault.NotSupported`_:
       if the host does not support the reboot operation.


ShutdownHost(force):
   Shuts down a host. If the command is successful, then the host has been shut down. Thus, the client never receives an indicator of success in the returned task if connected directly to the host.This command is not supported on all hosts. Check the host capability `shutdownSupported`_ .


  Privilege:
               Host.Config.Maintenance



  Args:
    force (`bool`_):
       Flag to specify whether or not the host should be shut down regardless of whether it is in maintenance mode. If true, the host is shut down, even if there are virtual machines running or other operations in progress.




  Returns:
     `vim.Task`_:


  Raises:

    `vim.fault.InvalidState`_:
       if "force" is false and the host is not in maintenance mode.

    `vmodl.fault.NotSupported`_:
       if the host does not support shutdown.


PowerDownHostToStandBy(timeoutSec, evacuatePoweredOffVms):
   Puts the host in standby mode, a mode in which the host is in a standby state from which it can be powered up remotely. While this task is running, no virtual machines can be powered on and no provisioning operations can be performed on the host.The task completes only if there are no powered-on virtual machines on the host, no provisioning operations in progress on the host, and the host stopped responding. The operation does not directly initiate any operations to evacuate or power-down powered-on virtual machines. However, if a dynamic recommendation generation module is running, if possible, it will provide, and depending on the automation level, it will execute migrations of powered-on virtual machine. Furthermore, VMware power management module may evacute and put a host in standby mode to save power. If the host is part of a cluster and the task is issued through VirtualCenter with evacuatePoweredOffVms set to true, the task will not succeed unless all the powered-off virtual machines are reregistered to other hosts. If VMware DRS is enabled, vCenter Server will automatically evacuate powered-off virtual machines.The task is cancellable.This command is not supported on all hosts. Check the host capability `standbySupported`_ .
  since: `VI API 2.5`_


  Privilege:
               Host.Config.Maintenance



  Args:
    timeoutSec (`int`_):
       The task completes when the host successfully enters standby mode and stops sending heartbeat signals. If heartbeats are still coming after timeoutSecs seconds, the host is declared timedout, and the task is assumed failed.


    evacuatePoweredOffVms (`bool`_, optional):
       This is a parameter used only by VirtualCenter. If set to true, for a DRS disabled cluster, the task will not succeed unless all powered-off virtual machines have been manually reregistered; for a DRS enabled cluster, VirtualCenter will automatically reregister powered-off virtual machines and a powered-off virtual machine may remain at the host only for two reasons: (a) no compatible host found for reregistration, (b) DRS is disabled for the virtual machine.




  Returns:
     `vim.Task`_:


  Raises:

    `vim.fault.HostPowerOpFailed`_:
       if the standby operation fails.

    `vim.fault.InvalidState`_:
       if the host is already in standby mode, or disconnected.

    `vmodl.fault.NotSupported`_:
       if the host does not support standby mode.

    `vim.fault.Timedout`_:
       vim.fault.Timedout

    `vmodl.fault.RequestCanceled`_:
       if the operation is canceled.


PowerUpHostFromStandBy(timeoutSec):
   Takes the host out of standby mode. If the command is successful, the host wakes up and starts sending heartbeats. This method may be called automatically by a dynamic recommendation generation module to add capacity to a cluster, if the host is not in maintenance mode.Note that, depending on the implementation of the wakeup method, the client may never receive an indicator of success in the returned task. In some cases, it is not even possible to ensure that the wakeup request has made it to the host.The task is cancellable.
  since: `VI API 2.5`_


  Privilege:
               Host.Config.Maintenance



  Args:
    timeoutSec (`int`_):
       The task completes when the host successfully exits standby state and sends a heartbeat signal. If nothing is received from the host for timeoutSec seconds, the host is declared timedout, and the task is assumed failed.




  Returns:
     `vim.Task`_:


  Raises:

    `vim.fault.HostPowerOpFailed`_:
       if the standby operation fails.

    `vim.fault.InvalidState`_:
       if the host is in a state from which it cannot be woken up (e.g., disconnected, poweredOff)

    `vmodl.fault.NotSupported`_:
       if the host does not support standby mode.

    `vim.fault.Timedout`_:
       vim.fault.Timedout

    `vmodl.fault.RequestCanceled`_:
       if the operation is canceled.


QueryMemoryOverhead(memorySize, videoRamSize, numVcpus):
   Determines the amount of memory overhead necessary to power on a virtual machine with the specified characteristics.


  Privilege:
               System.Read



  Args:
    memorySize (`long`_):
       The amount of virtual system RAM, in bytes. For an existing virtual machine, this value can be found (in megabytes) as the memoryMB property of the `VirtualHardware`_ .


    videoRamSize (`int`_, optional):
       The amount of virtual video RAM, in bytes. For an existing virtual machine on a host that supports advertising this property, this value can be found (in kilobytes) as the videoRamSizeInKB property of the `VirtualMachineVideoCard`_ . If this parameter is left unset, the default video RAM size for virtual machines on this host is assumed.


    numVcpus (`int`_):
       The number of virtual CPUs. For an existing virtual machine, this value can be found as the numCPU property of the `VirtualHardware`_ .




  Returns:
    `long`_:
         The amount of overhead memory required to power on such a virtual machine, in bytes.

  Raises:

    `vmodl.fault.NotSupported`_:
       if the host does not have memory resource allocation features.


QueryMemoryOverheadEx(vmConfigInfo):
   Determines the amount of memory overhead necessary to power on a virtual machine with the specified characteristics.
  since: `VI API 2.5`_


  Privilege:
               System.Read



  Args:
    vmConfigInfo (`vim.vm.ConfigInfo`_):
       The configuration of the virtual machine.




  Returns:
    `long`_:
         The amount of overhead memory required to power on such a virtual machine, in bytes.

  Raises:

    `vmodl.fault.NotSupported`_:
       if the host does not have memory resource allocation features.


ReconfigureHostForDAS():
   Reconfigures the host for vSphere HA.If the host is part of a HA cluster, this operation reconfigures the host for HA. For example, this operation may be used if a host is added to a HA enabled cluster and the automatic HA configuration system task fails. Automatic HA configuration may fail for a variety of reasons. For example, the host is configured incorrectly.


  Privilege:
               Host.Config.Connection



  Args:


  Returns:
     `vim.Task`_:


  Raises:

    `vim.fault.DasConfigFault`_:
       if there is a problem reconfiguring the host for HA.

    `vmodl.fault.NotSupported`_:
       if run directly on an ESX Server host.


UpdateFlags(flagInfo):
   Update flags that are part of the `HostFlagInfo`_ object.
  since: `VI API 2.5`_


  Privilege:
               Host.Config.Settings



  Args:
    flagInfo (`vim.host.FlagInfo`_):




  Returns:
    None



EnterLockdownMode():
   Modifies the permissions on the host, so that it will only be accessible through local console or an authorized centralized management application. Any user defined permissions found on the host are lost.Access via a VI client connected to the host is blocked. Access though other services running on the host is also blocked.If the operation is successful, `adminDisabled`_ will be set to true. This API is not supported on the host, If invoked directly on a host, a NotSupported fault will be thrown.See `AuthorizationManager`_
  since: `vSphere API 4.1`_


  Privilege:
               Host.Config.Settings



  Args:


  Returns:
    None


  Raises:

    `vim.fault.HostConfigFault`_:
       See `AuthorizationManager`_

    `vim.fault.AdminDisabled`_:
       If the host's Administrator permission has been disabled.See `AuthorizationManager`_

    `vim.fault.DisableAdminNotSupported`_:
       If invoked directly on the host or the host doesn't support this operation.See `AuthorizationManager`_


ExitLockdownMode():
   Restores Administrator permission for the local administrative account for the host that was removed by prior call to `EnterLockdownMode`_ . If the operation is successful, `adminDisabled`_ will be set to false. This API is not supported on the host. If invoked directly on a host, a NotSupported fault will be thrown.See `AuthorizationManager`_
  since: `vSphere API 4.1`_


  Privilege:
               Host.Config.Settings



  Args:


  Returns:
    None


  Raises:

    `vim.fault.HostConfigFault`_:
       See `AuthorizationManager`_

    `vim.fault.DisableAdminNotSupported`_:
       If invoked directly on the host or the host doesn't support this operation.See `AuthorizationManager`_

    `vim.fault.AdminNotDisabled`_:
       If the host's Administrator permission is not disabled.See `AuthorizationManager`_


AcquireCimServicesTicket():
   Creates and returns a one-time credential used to establish a remote connection to a CIM interface. The port to connect to is the standard well known port for the service.
  since: `VI API 2.5`_


  Privilege:
               Host.Cim.CimInteraction



  Args:


  Returns:
    `vim.HostServiceTicket`_:



UpdateIpmi(ipmiInfo):
   Update fields that are part of the `HostIpmiInfo`_ object.
  since: `vSphere API 4.0`_


  Privilege:
               Host.Config.Settings



  Args:
    ipmiInfo (`vim.host.IpmiInfo`_):




  Returns:
    None


  Raises:

    `vim.fault.InvalidIpmiLoginInfo`_:
       if the supplied user ID and/or password is invalid.

    `vim.fault.InvalidIpmiMacAddress`_:
       if the supplied MAC address is invalid.


RetrieveHardwareUptime():
   Return the hardware uptime of the host in seconds. The harware uptime of a host is not affected by NTP and changes to its wall clock time and can be used by clients to provide a common time reference for all hosts.
  since: `vSphere API 4.1`_


  Privilege:
               System.Read



  Args:


  Returns:
    `long`_:
