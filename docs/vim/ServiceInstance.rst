.. _str: https://docs.python.org/2/library/stdtypes.html

.. _datetime: https://docs.python.org/2/library/stdtypes.html

.. _vim.Task: ../vim/Task.rst

.. _VI API 2.5: ../vim/version.rst#vimversionversion2

.. _CurrentTime: ../vim/ServiceInstance.rst#currentTime

.. _serverClock: ../vim/ServiceInstance.rst#serverClock

.. _vim.HostSystem: ../vim/HostSystem.rst

.. _vim.Capability: ../vim/Capability.rst

.. _WaitForUpdates: ../vmodl/query/PropertyCollector.rst#waitForUpdates

.. _MigrateVM_Task: ../vim/VirtualMachine.rst#migrate

.. _RelocateVM_Task: ../vim/VirtualMachine.rst#relocate

.. _ServiceInstance: ../vim/ServiceInstance.rst

.. _vim.event.Event: ../vim/event/Event.rst

.. _vim.ResourcePool: ../vim/ResourcePool.rst

.. _PropertyCollector: ../vmodl/query/PropertyCollector.rst

.. _vim.VirtualMachine: ../vim/VirtualMachine.rst

.. _vim.fault.InvalidState: ../vim/fault/InvalidState.rst

.. _RetrieveServiceContent: ../vim/ServiceInstance.rst#retrieveContent

.. _vim.ServiceInstanceContent: ../vim/ServiceInstanceContent.rst

.. _vim.fault.InvalidPowerState: ../vim/fault/InvalidPowerState.rst

.. _vmodl.fault.InvalidArgument: ../vmodl/fault/InvalidArgument.rst

.. _vim.VirtualMachine.PowerState: ../vim/VirtualMachine/PowerState.rst

.. _vim.fault.NoActiveHostInCluster: ../vim/fault/NoActiveHostInCluster.rst

.. _vim.ServiceInstance.ProductComponentInfo: ../vim/ServiceInstance/ProductComponentInfo.rst

.. _vim.ServiceInstance.HostVMotionCompatibility: ../vim/ServiceInstance/HostVMotionCompatibility.rst


vim.ServiceInstance
===================
  The `ServiceInstance`_ managed object is the singleton root object of the inventory on both vCenter servers and servers running on standalone host agents. The server creates the `ServiceInstance`_ automatically, and also automatically creates the various manager entities that provide services in the virtual environment. Some examples of manager entities are `LicenseManager`_ , `PerformanceManager`_ , and `ViewManager`_ . You can access the manager entities through the `content`_ property.A vSphere API client application begins by connecting to a server and obtaining a reference to the `ServiceInstance`_ . The client can then use the `RetrieveServiceContent`_ method to gain access to the various vSphere manager entities and to the root folder of the inventory.When you create managed objects, the server adds them to the inventory. The inventory of managed objects includes instances the following object types:
   * `ServiceInstance`_
   * -- Root of the inventory; created by vSphere.
   * `Datacenter`_
   * -- A container that represents a virtual data center. It contains hosts, network entities, virtual machines and virtual applications, and datastores.
   * `Folder`_
   * -- A container used for hierarchical organization of the inventory.
   * `VirtualMachine`_
   * -- A virtual machine.
   * `VirtualApp`_
   * -- A virtual application.
   * `ComputeResource`_
   * -- A compute resource (either a cluster or a stand-alone host).
   * `ResourcePool`_
   * -- A subset of resources provided by a ComputeResource.
   * `HostSystem`_
   * -- A single host (ESX Server or VMware Server).
   * `Network`_
   * -- A network available to either hosts or virtual machines.
   * `DistributedVirtualSwitch`_
   * -- A distributed virtual switch.
   * `DistributedVirtualPortgroup`_
   * -- A distributed virtual port group.
   * `Datastore`_
   * -- Platform-independent, host-independent storage for virtual machine files.
   * 
   * The following figure shows the organization of managed objects in the vCenter hierarchy:
   * 
   * Every Datacenter has the following set of dedicated folders. These folders are empty until you create entities for the Datacenter.
   * 
   * A folder for any combination of
   * `VirtualMachine`_
   * and/or
   * `VirtualApp`_
   * objects.
   * `VirtualApp`_
   * objects can be nested, but only the parent
   * `VirtualApp`_
   * can be visible in the folder. Virtual machines that are children of virtual applications are not associated with a VirtualMachine/VirtualApp folder.
   * A folder for a
   * `ComputeResource`_
   * hierarchy.
   * A folder for network entities - any combination of
   * `Network`_
   * ,
   * `DistributedVirtualSwitch`_
   * , and/or
   * `DistributedVirtualPortgroup`_
   * objects.
   * A folder for
   * `Datastore`_
   * objects.
   * 
   * The host agent hierarchy has the same general form as the vCenter hierarchy, but most of the objects are limited to one instance:
   * 




Attributes
----------
    serverClock (`datetime`_):
      privilege: System.View
       Contains the time most recently obtained from the server. The time is not necessarily current. This property is intended for use with the PropertyCollector `WaitForUpdates`_ method. The PropertyCollector will provide notification if some event occurs that changes the server clock time in a non-linear fashion.You should not rely on the serverClock property to get the current time on the server; instead, use the `CurrentTime`_ method.
    capability (`vim.Capability`_):
      privilege: System.View
       API-wide capabilities.
    content (`vim.ServiceInstanceContent`_):
      privilege: System.Anonymous
       The properties of the ServiceInstance managed object. The content property is identical to the return value from the `RetrieveServiceContent`_ method.Use the content property with the `PropertyCollector`_ to perform inventory traversal that includes the ServiceInstance. (In the absence of a content property, a traversal that encounters the `ServiceInstance`_ would require calling the `RetrieveServiceContent`_ method, and then invoking a second traversal to continue.)


Methods
-------


CurrentTime():
   Returns the current time on the server. To monitor non-linear time changes, use the `serverClock`_ property.


  Privilege:
               System.View



  Args:


  Returns:
    `datetime`_:
         The date and time on the server.


RetrieveServiceContent():
   Retrieves the properties of the service instance.


  Privilege:
               System.Anonymous



  Args:


  Returns:
    `vim.ServiceInstanceContent`_:
         The properties belonging to the service instance, including various object managers.


ValidateMigration(vm, state, testType, pool, host):
   Checks the validity of a set of proposed migrations. A migration is the act of changing the assigned execution host of a virtual machine, which can result from invoking `MigrateVM_Task`_ or `RelocateVM_Task`_ .


  Privilege:
               System.View



  Args:
    vm (`vim.VirtualMachine`_):
       The set of virtual machines intended for migration.


    state (`vim.VirtualMachine.PowerState`_, optional):
       The power state that the virtual machines must have. If this argument is not set, each virtual machine is evaluated according to its current power state.


    testType (`str`_, optional):
       The set of tests to run. If this argument is not set, all tests will be run.


    pool (`vim.ResourcePool`_, optional):
       The target resource pool for the virtual machines. If the pool parameter is left unset, the target pool for each particular virtual machine's migration will be that virtual machine's current pool. If the virtual machine is a template then either this parameter or the host parameter must be set; additionally if resource tests are requested then this parameter is required.


    host (`vim.HostSystem`_, optional):
       The target host on which the virtual machines will run. The host parameter may be left unset if the compute resource associated with the target pool represents a stand-alone host or a DRS-enabled cluster. In the former case the stand-alone host is used as the target host. In the latter case, each connected host in the cluster that is not in maintenance mode is tested as a target host. If the virtual machine is a template then either this parameter or the pool parameter must be set.




  Returns:
    `vim.event.Event`_:
         A set of events that describe the warnings or errors that would apply if the proposed set of migrations were executed.

  Raises:

    `vim.fault.InvalidState`_: 
       vim.fault.InvalidState

    `vmodl.fault.InvalidArgument`_: 
       if the target host(s) and target pool for a migration are not associated with the same compute resource, or if the host parameter is left unset when the target pool is associated with a non-DRS cluster.

    `vim.fault.InvalidPowerState`_: 
       if the state argument is set and at least one of the specified virtual machines is not in that power state.

    `vim.fault.NoActiveHostInCluster`_: 
       if a target host is not specified and a cluster associated with a target pool does not contain at least one potential target host. A host must be connected and not in maintenance mode in order to be considered as a potential target host.


QueryVMotionCompatibility(vm, host, compatibility):
   Investigates the general VMotion compatibility of a virtual machine with a set of hosts. The virtual machine may be in any power state. Hosts may be in any connection state and also may be in maintenance mode.


  Privilege:
               Resource.QueryVMotion



  Args:
    vm (`vim.VirtualMachine`_):
       The virtual machine that is the designated VMotion candidate.


    host (`vim.HostSystem`_):
       The group of hosts to analyze for compatibility.


    compatibility (`str`_, optional):
       The set of compatibility types to investigate. Each is a string chosen from VMotionCompatibilityType. If this argument is not set, then all compatibility types are investigated.




  Returns:
    `vim.ServiceInstance.HostVMotionCompatibility`_:
         An array where each element, associated with one of the input hosts, specifies which of the requested compatibility types applies to that host. If an input host has never been connected and therefore has no information available for determining its compatibility, it is omitted from the return list.


RetrieveProductComponents():
   Component information for bundled products
  since: `VI API 2.5`_


  Privilege:
               System.Anonymous



  Args:


  Returns:
    `vim.ServiceInstance.ProductComponentInfo`_:
         


