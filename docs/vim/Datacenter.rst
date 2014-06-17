.. _int: https://docs.python.org/2/library/stdtypes.html

.. _str: https://docs.python.org/2/library/stdtypes.html

.. _bool: https://docs.python.org/2/library/stdtypes.html

.. _host: ../vim/vm/ConfigOptionDescriptor.rst#host

.. _Network: ../vim/Network.rst

.. _template: ../vim/vm/ConfigInfo.rst#template

.. _vim.Task: ../vim/Task.rst

.. _VirtualApp: ../vim/VirtualApp.rst

.. _vim.Folder: ../vim/Folder.rst

.. _VI API 2.5: ../vim/version.rst#vimversionversion2

.. _vim.Network: ../vim/Network.rst

.. _ResourcePool: ../vim/ResourcePool.rst

.. _vim.Datastore: ../vim/Datastore.rst

.. _VirtualMachine: ../vim/VirtualMachine.rst

.. _vSphere API 5.1: ../vim/version.rst#vimversionversion8

.. _vSphere API 4.0: ../vim/version.rst#vimversionversion5

.. _vim.fault.NoHost: ../vim/fault/NoHost.rst

.. _vim.ManagedEntity: ../vim/ManagedEntity.rst

.. _vim.VirtualMachine: ../vim/VirtualMachine.rst

.. _vim.host.ConnectInfo: ../vim/host/ConnectInfo.rst

.. _vim.option.OptionValue: ../vim/option/OptionValue.rst

.. _vim.fault.InvalidLogin: ../vim/fault/InvalidLogin.rst

.. _vmodl.fault.NotSupported: ../vmodl/fault/NotSupported.rst

.. _vim.fault.SSLVerifyFault: ../vim/fault/SSLVerifyFault.rst

.. _DistributedVirtualSwitch: ../vim/DistributedVirtualSwitch.rst

.. _vim.Datacenter.ConfigSpec: ../vim/Datacenter/ConfigSpec.rst

.. _defaultHardwareVersionKey: ../vim/Datacenter/ConfigSpec.rst#defaultHardwareVersionKey

.. _vim.Datacenter.ConfigInfo: ../vim/Datacenter/ConfigInfo.rst

.. _vim.fault.SSLDisabledFault: ../vim/fault/SSLDisabledFault.rst

.. _vim.fault.AlreadyConnected: ../vim/fault/AlreadyConnected.rst

.. _vim.fault.NotSupportedHost: ../vim/fault/NotSupportedHost.rst

.. _vim.fault.HostConnectFault: ../vim/fault/HostConnectFault.rst

.. _DistributedVirtualPortgroup: ../vim/dvs/DistributedVirtualPortgroup.rst

.. _vmodl.fault.InvalidArgument: ../vmodl/fault/InvalidArgument.rst

.. _vim.cluster.PowerOnVmResult: ../vim/cluster/PowerOnVmResult.rst

.. _vim.vm.ConfigOptionDescriptor: ../vim/vm/ConfigOptionDescriptor.rst


vim.Datacenter
==============
  The `Datacenter`_ managed object provides the interface to the common container object for hosts, virtual machines, networks, and datastores. These entities must be under a distinct datacenter in the inventory, and datacenters may not be nested under other datacenters.Every `Datacenter`_ has the following set of dedicated folders. These folders are empty until you create entities for the Datacenter.
   * A folder for
   * `VirtualMachine`_
   * , template, and
   * `VirtualApp`_
   * objects.
   * A folder for a
   * `ComputeResource`_
   * hierarchy.
   * A folder for
   * `Network`_
   * ,
   * `DistributedVirtualSwitch`_
   * , and
   * `DistributedVirtualPortgroup`_
   * objects.
   * A folder for
   * `Datastore`_
   * objects.
   * 
   * For a visual representation of the organization of objects in a vCenter hierarchy, see the description of the
   * `ServiceInstance`_
   * object.


:extends: vim.ManagedEntity_


Attributes
----------
    vmFolder (`vim.Folder`_):
      privilege: System.View
       A reference to the folder hierarchy that contains `VirtualMachine`_ virtual machine templates (identified by the `template`_ property, and `VirtualApp`_ objects for this datacenter.Note that a VirtualApp that is a child of a `ResourcePool`_ may also be visible in this folder. VirtualApp objects can be nested, but only the parent VirtualApp can be visible in the folder.This folder is guaranteed to exist.
    hostFolder (`vim.Folder`_):
      privilege: System.View
       A reference to the folder hierarchy that contains the compute resources, including hosts and clusters, for this datacenter.This folder is guaranteed to exist.
    datastoreFolder (`vim.Folder`_):
      privilege: System.View
       A reference to the folder hierarchy that contains the datastores for this datacenter.This folder is guaranteed to exist.
    networkFolder (`vim.Folder`_):
      privilege: System.View
       A reference to the folder hierarchy that contains the network entities for this datacenter. The folder can include `Network`_ , `DistributedVirtualSwitch`_ , and `DistributedVirtualPortgroup`_ objects.This folder is guaranteed to exist.
    datastore (`vim.Datastore`_):
       A collection of references to the datastore objects available in this datacenter.
    network (`vim.Network`_):
       A collection of references to the network objects available in this datacenter.
    configuration (`vim.Datacenter.ConfigInfo`_):
      privilege: System.View
       Configuration of the datacenter.


Methods
-------


QueryConnectionInfo(hostname, port, username, password, sslThumbprint):
   This method provides a way of getting basic information about a host without adding it to a datacenter. Connection wizards typically use this method to show information about a host so a user can confirm a set of changes before applying them.


  Privilege:
               System.View



  Args:
    hostname (`str`_):
       The target of the query.


    port (`int`_):
       The port number of the target host. For ESX 2.x this is the authd port (902 by default). For ESX 3.x and above and for VMware Server hosts this is the https port (443 by default). You can specify -1 to have the vCenter Server try the default ports.


    username (`str`_):
       The name of the user.


    password (`str`_):
       The password of the user.


    sslThumbprint (`str`_, optional, since `VI API 2.5`_ ):
       The expected SSL thumbprint of the host's certificate




  Returns:
    `vim.host.ConnectInfo`_:
         

  Raises:

    `vim.fault.InvalidLogin`_: 
       if unable to authenticate with the host.

    `vim.fault.HostConnectFault`_: 
       if an error occurred when querying about a host. Typically, a more specific subclass, such as AlreadyBeingManaged, is thrown.

    `vmodl.fault.NotSupported`_: 
       if called directly on a host.

    `vim.fault.NoHost`_: 
       if unable to contact the host.

    `vim.fault.NotSupportedHost`_: 
       if the software version on the host is not supported.

    `vim.fault.AlreadyConnected`_: 
       if the host is already being managed by this server.

    `vim.fault.SSLDisabledFault`_: 
       if the host has ssl access disabled

    `vim.fault.SSLVerifyFault`_: 
       if the host certificate could not be authenticated


PowerOnMultiVM(vm, option):
   Powers on multiple virtual machines in a data center. If the virtual machines are suspended, this method resumes execution from the suspend point. The virtual machines can belong to different clusters in the data center.If any virtual machine in the list is manually managed by DRS, or DRS has to migrate any manually managed virtual machine or power on any manually managed host in order to power on these virtual machines, a DRS recommendation will be generated, and the users need to manually apply the recommendation for actually powering on these virtual machines. Otherwise, all the virtual machine will be automatically powered on. The virtual machines on stand alone hosts or DRS disabled will be powered-on on the current host. The DRS automatically managed virtual machines will be powered-on on the recommended hosts.When powering on a virtual machine in a cluster, the system might do an implicit relocation of the virtual machine to another host.
  since: `VI API 2.5`_


  Privilege:
               System.View



  Args:
    vm (`vim.VirtualMachine`_):
       The virtual machines to power on.


    option (`vim.option.OptionValue`_, optional, since `vSphere API 4.1`_ ):
       An array of `OptionValue`_ options for this power-on session. The names and values of the options are defined in `ClusterPowerOnVmOption`_ .




  Returns:
     `vim.Task`_:
         An array of Recommendation.

  Raises:

    `vmodl.fault.InvalidArgument`_: 
       for unknown option keys or bad values.


queryDatacenterConfigOptionDescriptor():
   The list of possible choices for `defaultHardwareVersionKey`_ . Descriptors returned by the vCenter implementation do not have `host`_ field populated.
  since: `vSphere API 5.1`_


  Privilege:
               System.View



  Args:


  Returns:
    `vim.vm.ConfigOptionDescriptor`_:
         


ReconfigureDatacenter(spec, modify):
   Change the datacenter configuration.
  since: `vSphere API 5.1`_


  Privilege:
               Datacenter.Reconfigure



  Args:
    spec (`vim.Datacenter.ConfigSpec`_):
       A set of configuration changes to apply to the datacenter. The specification can be a complete set of changes or a partial set of changes, applied incrementally.


    modify (`bool`_):
       Flag to specify whether the specification ("spec") should be applied incrementally. If "modify" is false and the operation succeeds, then the configuration of the datacenter matches the specification exactly; in this case any unset portions of the specification will result in unset or default portions of the configuration.




  Returns:
     `vim.Task`_:
         


