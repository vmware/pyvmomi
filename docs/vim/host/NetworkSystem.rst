.. _str: https://docs.python.org/2/library/stdtypes.html

.. _device: ../../vim/host/PhysicalNic.rst#device

.. _vim.Task: ../../vim/Task.rst

.. _vSphere API 4.0: ../../vim/version.rst#vimversionversion5

.. _HostNetworkInfo: ../../vim/host/NetworkInfo.rst

.. _vim.host.DnsConfig: ../../vim/host/DnsConfig.rst

.. _HostNicOrderPolicy: ../../vim/host/NetworkPolicy/NicOrderPolicy.rst

.. _vim.fault.NotFound: ../../vim/fault/NotFound.rst

.. _UpdateVirtualSwitch: ../../vim/host/NetworkSystem.rst#updateVirtualSwitch

.. _supportsNetworkHints: ../../vim/host/NetCapabilities.rst#supportsNetworkHints

.. _vim.host.NetworkInfo: ../../vim/host/NetworkInfo.rst

.. _HostConfigChangeMode: ../../vim/host/ConfigChange/Mode.rst

.. _usesServiceConsoleNic: ../../vim/host/NetCapabilities.rst#usesServiceConsoleNic

.. _updateNetworkConfig(): ../../vim/host/NetworkSystem.rst#updateNetworkConfig

.. _vim.fault.HostInDomain: ../../vim/fault/HostInDomain.rst

.. _vim.host.NetworkConfig: ../../vim/host/NetworkConfig.rst

.. _vim.host.IpRouteConfig: ../../vim/host/IpRouteConfig.rst

.. _vim.fault.InvalidState: ../../vim/fault/InvalidState.rst

.. _vim.fault.ResourceInUse: ../../vim/fault/ResourceInUse.rst

.. _vim.fault.AlreadyExists: ../../vim/fault/AlreadyExists.rst

.. _vim.host.NetCapabilities: ../../vim/host/NetCapabilities.rst

.. _vmodl.fault.NotSupported: ../../vmodl/fault/NotSupported.rst

.. _vim.fault.HostConfigFault: ../../vim/fault/HostConfigFault.rst

.. _canSetPhysicalNicLinkSpeed: ../../vim/host/NetCapabilities.rst#canSetPhysicalNicLinkSpeed

.. _vmodl.fault.InvalidArgument: ../../vmodl/fault/InvalidArgument.rst

.. _vim.ExtensibleManagedObject: ../../vim/ExtensibleManagedObject.rst

.. _vim.host.IpRouteTableConfig: ../../vim/host/IpRouteTableConfig.rst

.. _vim.host.NetworkConfig.Result: ../../vim/host/NetworkConfig/Result.rst

.. _vim.host.NetOffloadCapabilities: ../../vim/host/NetOffloadCapabilities.rst

.. _vim.host.PortGroup.Specification: ../../vim/host/PortGroup/Specification.rst

.. _vim.host.PhysicalNic.NetworkHint: ../../vim/host/PhysicalNic/NetworkHint.rst

.. _vim.host.VirtualNic.Specification: ../../vim/host/VirtualNic/Specification.rst

.. _vim.host.PhysicalNic.LinkSpeedDuplex: ../../vim/host/PhysicalNic/LinkSpeedDuplex.rst

.. _vim.host.VirtualSwitch.Specification: ../../vim/host/VirtualSwitch/Specification.rst


vim.host.NetworkSystem
======================
  This managed object type describes networking host configuration and serves as the top level container for relevant networking data objects.


:extends: vim.ExtensibleManagedObject_


Attributes
----------
    capabilities (`vim.host.NetCapabilities`_):
       Capability vector indicating the available product features.
    networkInfo (`vim.host.NetworkInfo`_):
       The network configuration and runtime information.
    offloadCapabilities (`vim.host.NetOffloadCapabilities`_):
       The offload capabilities available on this server.
    networkConfig (`vim.host.NetworkConfig`_):
       Network configuration information. This information can be applied using the `updateNetworkConfig()`_ method. The information is a strict subset of the information available in NetworkInfo.See `HostNetworkInfo`_ 
    dnsConfig (`vim.host.DnsConfig`_):
       Client-side DNS configuration.
    ipRouteConfig (`vim.host.IpRouteConfig`_):
       The IP route configuration.
    consoleIpRouteConfig (`vim.host.IpRouteConfig`_):
       IP route configuration for the service console. The IP route configuration is global to the entire host. This property is set only if IP routing can be configured for the service console.


Methods
-------


UpdateNetworkConfig(config, changeMode):
   Applies the network configuration. This method operates primarily in two modes:replaceormodifymode.replaceWhen called inreplacemode, this method applies the fully specified networking configuration to the networking system.Upon successful completion of the call, the state of networking will match the configuration specified inconfig. In general, objects are created or destroyed to match the elements in the array of configurations. The identifier field in each element in an array of configurations is used to match an existing network entity. The state of existing network entities is patched to match that of the configuration.An exception to this approach applies to the array of PhysicalNic.Config objects. The cardinality of physical network adapters cannot be changed through this operation. Thus, the identifier of every element in the array must match an existing PhysicalNic. If there are fewer elements in the array than there are existing PhysicalNics, then no change is made on the unreferenced PhysicalNic objects.If the call fails, the networking error is returned as an exception and the state of networking reverts to the state prior to the start of the call.modifyWhen called inmodifymode, only changes that are specified are made. For singleton entities like DnsConfig, the state is changed only if the data object is set. For array elements, there is an Operation field that indicates if the element should be added, removed, or edited. In the case of editing or removal, the entity must exist or an exception is thrown. In the case of adding, a specification needs to be provided.It returns device names of vmkernel and service console virtual network adapter added to the system.Currently, the only mode that is implemented is incremental mode. Only add operations are supported for instances. Singleton configuration is not supported. The dynamic privilege check will ensure that users have Host.Config.Network privilege on the host, and Network.Assign privilege on the connecting DVPortGroup, or DVS if connecting to a standalone DVPort. Network.Assign privilege is not required for operations on standard network or for operations performed directly on the hostSee `HostConfigChangeMode`_ 


  Privilege:
               dynamic



  Args:
    config (`vim.host.NetworkConfig`_):
       See `HostConfigChangeMode`_ 


    changeMode (`str`_):
       See `HostConfigChangeMode`_ 




  Returns:
    `vim.host.NetworkConfig.Result`_:
         

  Raises:

    `vim.fault.AlreadyExists`_: 
       when a network entity specified in the configuration already exists.See `HostConfigChangeMode`_ 

    `vim.fault.NotFound`_: 
       when a network entity specified in the configuration already exists.See `HostConfigChangeMode`_ 

    `vim.fault.HostConfigFault`_: 
       for all other configuration failures.See `HostConfigChangeMode`_ 

    `vim.fault.ResourceInUse`_: 
       See `HostConfigChangeMode`_ 

    `vmodl.fault.InvalidArgument`_: 
       if an invalid parameter is passed in for one of the networking objects.See `HostConfigChangeMode`_ 

    `vmodl.fault.NotSupported`_: 
       if modify mode is not used, a remove or set operation is specified for an instance, or a singleton entity is configured.See `HostConfigChangeMode`_ 


UpdateDnsConfig(config):
   Applies the client-side DNS configuration.


  Privilege:
               Host.Config.Network



  Args:
    config (`vim.host.DnsConfig`_):




  Returns:
    None
         

  Raises:

    `vim.fault.NotFound`_: 
       when the DHCP virtual network adapter specified does not exist.

    `vim.fault.HostConfigFault`_: 
       for all other configuration failures.

    `vmodl.fault.InvalidArgument`_: 
       if any of the IP addresses are invalid, or for a DHCP DNS, if the DHCP virtual network adapter is not specified or the virtual network adapter specified is not DHCP enabled.

    `vmodl.fault.NotSupported`_: 
       if the host is not an ESX Server system.

    `vim.fault.HostInDomain`_: 
       if an attempt is made to change the host or domain name while the host is part of a Windows domain.


UpdateIpRouteConfig(config):
   Applies the IP route configuration.


  Privilege:
               Host.Config.Network



  Args:
    config (`vim.host.IpRouteConfig`_):




  Returns:
    None
         

  Raises:

    `vim.fault.HostConfigFault`_: 
       for all other configuration failures.

    `vim.fault.InvalidState`_: 
       if the an ipv6 address is specified in an ipv4 only system

    `vmodl.fault.InvalidArgument`_: 
       if any of the IP addresses are invalid.

    `vmodl.fault.NotSupported`_: 
       if the host is not an ESX Server system.


UpdateConsoleIpRouteConfig(config):
   Applies the IP route configuration for the service console.


  Privilege:
               Host.Config.Network



  Args:
    config (`vim.host.IpRouteConfig`_):




  Returns:
    None
         

  Raises:

    `vim.fault.HostConfigFault`_: 
       for all other configuration failures.

    `vmodl.fault.InvalidArgument`_: 
       if any of the IP addresses are invalid.

    `vmodl.fault.NotSupported`_: 
       if the host is not an ESX Server system.


UpdateIpRouteTableConfig(config):
   Applies the IP route table configuration.
  since: `vSphere API 4.0`_


  Privilege:
               Host.Config.Network



  Args:
    config (`vim.host.IpRouteTableConfig`_):




  Returns:
    None
         

  Raises:

    `vim.fault.HostConfigFault`_: 
       for all other configuration failures.

    `vmodl.fault.InvalidArgument`_: 
       if any of the IP addresses are invalid.

    `vmodl.fault.NotSupported`_: 
       if the host is not an ESX Server system.


AddVirtualSwitch(vswitchName, spec):
   Adds a new virtual switch to the system with the given name. The name must be unique with respect to other virtual switches on the host and is limited to 32 characters.See `UpdateVirtualSwitch`_ 


  Privilege:
               Host.Config.Network



  Args:
    vswitchName (`str`_):
       See `UpdateVirtualSwitch`_ 


    spec (`vim.host.VirtualSwitch.Specification`_, optional):
       See `UpdateVirtualSwitch`_ 




  Returns:
    None
         

  Raises:

    `vim.fault.AlreadyExists`_: 
       if the virtual switch already exists.See `UpdateVirtualSwitch`_ 

    `vim.fault.ResourceInUse`_: 
       if the physical network adapter being bridged is already in use.See `UpdateVirtualSwitch`_ 

    `vim.fault.HostConfigFault`_: 
       for all other configuration failures.See `UpdateVirtualSwitch`_ 

    `vmodl.fault.InvalidArgument`_: 
       if network vswitchName exceeds the maximum allowed length, or the number of ports specified falls out of valid range, or the network policy is invalid, or beacon configuration is invalid.See `UpdateVirtualSwitch`_ 


RemoveVirtualSwitch(vswitchName):
   Removes an existing virtual switch from the system.


  Privilege:
               Host.Config.Network



  Args:
    vswitchName (`str`_):




  Returns:
    None
         

  Raises:

    `vim.fault.NotFound`_: 
       if the virtual switch does not exist.

    `vim.fault.ResourceInUse`_: 
       if there are virtual network adapters associated with the virtual switch.

    `vim.fault.HostConfigFault`_: 
       for all other configuration failures.


UpdateVirtualSwitch(vswitchName, spec):
   Updates the properties of the virtual switch.If the bridge is NULL, the configuration will be unset.If a network adapter is listed in the active or standby list, then changing the set of network adapters to which the physical network adapter is associated may have a side effect of changing the network adapter order policy. If a network adapter is removed from the bridge configuration, then the network adapter is removed from the network adapter teaming order.The BondBridge configuration is the only valid bridge configuration for an ESX Server system.See `HostNicOrderPolicy`_ 


  Privilege:
               Host.Config.Network



  Args:
    vswitchName (`str`_):
       See `HostNicOrderPolicy`_ 


    spec (`vim.host.VirtualSwitch.Specification`_):
       See `HostNicOrderPolicy`_ 




  Returns:
    None
         

  Raises:

    `vim.fault.ResourceInUse`_: 
       if the physical network adapter being bridged is already in use.See `HostNicOrderPolicy`_ 

    `vim.fault.NotFound`_: 
       if the virtual switch does not exist.See `HostNicOrderPolicy`_ 

    `vim.fault.HostConfigFault`_: 
       for all other configuration failures.See `HostNicOrderPolicy`_ 

    `vmodl.fault.InvalidArgument`_: 
       if the bridge parameter is bad or the network policy is invalid or does not exist or the number of ports specified falls out of valid range, or the beacon configuration is invalid.See `HostNicOrderPolicy`_ 

    `vmodl.fault.NotSupported`_: 
       if network adapter teaming policy is set but is not supported.See `HostNicOrderPolicy`_ 


AddPortGroup(portgrp):
   Adds a port group to the virtual switch.


  Privilege:
               Host.Config.Network



  Args:
    portgrp (`vim.host.PortGroup.Specification`_):




  Returns:
    None
         

  Raises:

    `vim.fault.AlreadyExists`_: 
       if the port group already exists.

    `vim.fault.NotFound`_: 
       if the virtual switch does not exist.

    `vim.fault.HostConfigFault`_: 
       for all other configuration failures.

    `vmodl.fault.InvalidArgument`_: 
       if the PortGroup vlanId is invalid. Valid vlanIds range from [0,4095], where 0 means no vlan tagging. Exception is also thrown if network policy is invalid.


RemovePortGroup(pgName):
   Removes port group from the virtual switch.


  Privilege:
               Host.Config.Network



  Args:
    pgName (`str`_):




  Returns:
    None
         

  Raises:

    `vim.fault.NotFound`_: 
       if the port group or virtual switch does not exist.

    `vim.fault.ResourceInUse`_: 
       if the port group can not be removed because there are virtual network adapters associated with it.

    `vim.fault.HostConfigFault`_: 
       for all other configuration failures.


UpdatePortGroup(pgName, portgrp):
   Reconfigures a port group on the virtual switch.


  Privilege:
               Host.Config.Network



  Args:
    pgName (`str`_):


    portgrp (`vim.host.PortGroup.Specification`_):




  Returns:
    None
         

  Raises:

    `vim.fault.AlreadyExists`_: 
       if the update causes the port group to conflict with an existing port group.

    `vim.fault.NotFound`_: 
       if the port group or virtual switch does not exist.

    `vim.fault.HostConfigFault`_: 
       for all other configuration failures.

    `vmodl.fault.InvalidArgument`_: 
       if the PortGroup vlanId is invalid. Valid vlanIds range from [0,4095], where 0 means no vlan tagging. Exception is also thrown if network policy is invalid.


UpdatePhysicalNicLinkSpeed(device, linkSpeed):
   Configures link speed and duplexity. If linkSpeed is not specified, physical network adapter will be set to autonegotiate.See `canSetPhysicalNicLinkSpeed`_ 


  Privilege:
               Host.Config.Network



  Args:
    device (`str`_):
       See `canSetPhysicalNicLinkSpeed`_ 


    linkSpeed (`vim.host.PhysicalNic.LinkSpeedDuplex`_, optional):
       See `canSetPhysicalNicLinkSpeed`_ 




  Returns:
    None
         

  Raises:

    `vim.fault.NotFound`_: 
       if the physical network adapter does not exist.See `canSetPhysicalNicLinkSpeed`_ 

    `vim.fault.HostConfigFault`_: 
       for all other configuration failures.See `canSetPhysicalNicLinkSpeed`_ 

    `vmodl.fault.NotSupported`_: 
       if the host is not an ESX Server system.See `canSetPhysicalNicLinkSpeed`_ 

    `vmodl.fault.InvalidArgument`_: 
       if the speed and duplexity is not one of the valid configurations.See `canSetPhysicalNicLinkSpeed`_ 


QueryNetworkHint(device):
   Requests network hint information for a physical network adapter. A network hint is some information about the network to which the physical network adapter is attached. The method receives in a list of physical network adapter devices and returns an equal number of hints if some devices are provided. If the list of devices is empty, then the method accesses hints for all physical network adapters.See `supportsNetworkHints`_ See `device`_ 


  Privilege:
               System.Read



  Args:
    device (`str`_, optional):
       See `supportsNetworkHints`_ See `device`_ 




  Returns:
    `vim.host.PhysicalNic.NetworkHint`_:
         

  Raises:

    `vim.fault.NotFound`_: 
       if a specified physical network adapter does not exist.See `supportsNetworkHints`_ See `device`_ 

    `vim.fault.HostConfigFault`_: 
       for all other configuration failures.See `supportsNetworkHints`_ See `device`_ 

    `vmodl.fault.InvalidArgument`_: 
       if the speed and duplexity combination is not valid for the current link driver.See `supportsNetworkHints`_ See `device`_ 

    `vmodl.fault.NotSupported`_: 
       if the host is not an ESX Server system.See `supportsNetworkHints`_ See `device`_ 


AddVirtualNic(portgroup, nic):
   Adds a virtual host/VMkernel network adapter. Returns the device of the virtual network adapter.IP configuration is required although it does not have to be enabled if the host is an ESX Server system. The dynamic privilege check will ensure that users have Host.Config.Network privilege on the host, and Network.Assign privilege on the connecting DVPortGroup, or DVS if connecting to a standalone DVPort. Network.Assign privilege is not required for operations on standard network or for operations performed directly on the host.


  Privilege:
               dynamic



  Args:
    portgroup (`str`_):
       Note: Must be the empty string in case nic.distributedVirtualPort is set.


    nic (`vim.host.VirtualNic.Specification`_):




  Returns:
    `str`_:
         

  Raises:

    `vim.fault.AlreadyExists`_: 
       if the portgroup already has a virtual network adapter.

    `vim.fault.HostConfigFault`_: 
       for all other configuration failures.

    `vim.fault.InvalidState`_: 
       if the an ipv6 address is specified in an ipv4 only system

    `vmodl.fault.InvalidArgument`_: 
       if the IP address or subnet mask in the IP configuration are invalid. In the case of an ESX Server system, DHCP is not supported and this exception will be thrown if DHCP is specified. Exception may also be thrown if the named PortGroup does not exist.


RemoveVirtualNic(device):
   Removes a virtual host/VMkernel network adapter.


  Privilege:
               Host.Config.Network



  Args:
    device (`str`_):




  Returns:
    None
         

  Raises:

    `vim.fault.NotFound`_: 
       if the virtual network adapter cannot be found.

    `vim.fault.HostConfigFault`_: 
       for all other configuration failures.


UpdateVirtualNic(device, nic):
   Configures virtual host/VMkernel network adapter.IP configuration is required although it does not have to be enabled if the host is an ESX Server system. The dynamic privilege check will ensure that users have Host.Config.Network privilege on the host, and Network.Assign privilege on the connecting DVPortGroup, or DVS if connecting to a standalone DVPort. Network.Assign privilege is not required for operations on standard network or for operations performed directly on the host.


  Privilege:
               dynamic



  Args:
    device (`str`_):


    nic (`vim.host.VirtualNic.Specification`_):




  Returns:
    None
         

  Raises:

    `vim.fault.NotFound`_: 
       if the virtual network adapter cannot be found.

    `vim.fault.HostConfigFault`_: 
       for all other configuration failures.

    `vim.fault.InvalidState`_: 
       if the an ipv6 address is specified in an ipv4 only system

    `vmodl.fault.InvalidArgument`_: 
       if the IP address or subnet mask in the IP configuration are invalid. In the case of an ESX Server system, DHCP is not supported and this exception is thrown if DHCP is specified. Exception may also be thrown if the named PortGroup does not exist.


AddServiceConsoleVirtualNic(portgroup, nic):
   Adds a virtual service console network adapter. Returns the device of the VirtualNic.IP configuration is required although it does not have to be enabled if the host is an ESX Server system. The dynamic privilege check will ensure that users have Host.Config.Network privilege on the host, and Network.Assign privilege on the connecting DVPortGroup, or DVS if connecting to a standalone DVPort. Network.Assign privilege is not required for operations on standard network or for operations performed directly on the hostSee `usesServiceConsoleNic`_ 


  Privilege:
               dynamic



  Args:
    portgroup (`str`_):
       See `usesServiceConsoleNic`_ 


    nic (`vim.host.VirtualNic.Specification`_):
       See `usesServiceConsoleNic`_ 




  Returns:
    `str`_:
         

  Raises:

    `vim.fault.HostConfigFault`_: 
       for all other configuration failures.See `usesServiceConsoleNic`_ 

    `vmodl.fault.InvalidArgument`_: 
       if the IP address or subnet mask in the IP configuration are invalid or the named PortGroup does not exist.See `usesServiceConsoleNic`_ 

    `vmodl.fault.NotSupported`_: 
       if the host is not an ESX Server system.See `usesServiceConsoleNic`_ 


RemoveServiceConsoleVirtualNic(device):
   Removes a virtual service console network adapter.See `usesServiceConsoleNic`_ 


  Privilege:
               Host.Config.Network



  Args:
    device (`str`_):
       See `usesServiceConsoleNic`_ 




  Returns:
    None
         

  Raises:

    `vim.fault.NotFound`_: 
       if the virtual network adapter cannot be found.See `usesServiceConsoleNic`_ 

    `vim.fault.ResourceInUse`_: 
       if the network adapter is currently used by DHCP DNS.See `usesServiceConsoleNic`_ 

    `vim.fault.HostConfigFault`_: 
       for all other configuration failures.See `usesServiceConsoleNic`_ 

    `vmodl.fault.NotSupported`_: 
       if the host is not an ESX Server system.See `usesServiceConsoleNic`_ 


UpdateServiceConsoleVirtualNic(device, nic):
   Configures the IP configuration for a virtual service console network adapter.IP configuration is required although it does not have to be enabled if the host is an ESX Server system. The dynamic privilege check will check that the users have Network.Assign privilege on the DVPortGroup or the DVS if the port resides on a DVPortGroup or is a stand-alone DVS port.See `usesServiceConsoleNic`_ 


  Privilege:
               dynamic



  Args:
    device (`str`_):
       See `usesServiceConsoleNic`_ 


    nic (`vim.host.VirtualNic.Specification`_):
       See `usesServiceConsoleNic`_ 




  Returns:
    None
         

  Raises:

    `vim.fault.NotFound`_: 
       if the virtual network adapter cannot be found.See `usesServiceConsoleNic`_ 

    `vim.fault.ResourceInUse`_: 
       if tries to turn of DHCP while the network adapter is currently used by DHCP DNS.See `usesServiceConsoleNic`_ 

    `vim.fault.HostConfigFault`_: 
       for all other configuration failures.See `usesServiceConsoleNic`_ 

    `vmodl.fault.InvalidArgument`_: 
       if the IP address or subnet mask in the IP configuration are invalid or the named PortGroup does not exist.See `usesServiceConsoleNic`_ 

    `vmodl.fault.NotSupported`_: 
       if the host is not an ESX Server system.See `usesServiceConsoleNic`_ 


RestartServiceConsoleVirtualNic(device):
   Restart the service console virtual network adapter interface. If the service console virtual network adapter uses DHCP, restarting the interface may result it with a different IP configuration, or even fail to be brought up depending on the host system network configuration.See `usesServiceConsoleNic`_ 


  Privilege:
               Host.Config.Network



  Args:
    device (`str`_):
       See `usesServiceConsoleNic`_ 




  Returns:
    None
         

  Raises:

    `vim.fault.NotFound`_: 
       if the virtual network adapter cannot be found.See `usesServiceConsoleNic`_ 

    `vim.fault.HostConfigFault`_: 
       for all other configuration failures.See `usesServiceConsoleNic`_ 

    `vmodl.fault.NotSupported`_: 
       if the host is not an ESX Server system.See `usesServiceConsoleNic`_ 


RefreshNetworkSystem():
   Refresh the network information and settings to pick up any changes that might have occurred.


  Privilege:
               Host.Config.Network



  Args:


  Returns:
    None
         


