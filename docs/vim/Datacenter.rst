
vim.Datacenter
==============
  The `Datacenter <vim/Datacenter.rst>`_ managed object provides the interface to the common container object for hosts, virtual machines, networks, and datastores. These entities must be under a distinct datacenter in the inventory, and datacenters may not be nested under other datacenters.Every `Datacenter <vim/Datacenter.rst>`_ has the following set of dedicated folders. These folders are empty until you create entities for the Datacenter.
   * A folder for
   * `VirtualMachine <vim/VirtualMachine.rst>`_
   * , template, and
   * `VirtualApp <vim/VirtualApp.rst>`_
   * objects.
   * A folder for a
   * `ComputeResource <vim/ComputeResource.rst>`_
   * hierarchy.
   * A folder for
   * `Network <vim/Network.rst>`_
   * ,
   * `DistributedVirtualSwitch <vim/DistributedVirtualSwitch.rst>`_
   * , and
   * `DistributedVirtualPortgroup <vim/dvs/DistributedVirtualPortgroup.rst>`_
   * objects.
   * A folder for
   * `Datastore <vim/Datastore.rst>`_
   * objects.
   * 
   * For a visual representation of the organization of objects in a vCenter hierarchy, see the description of the
   * `ServiceInstance <vim/ServiceInstance.rst>`_
   * object.


:extends: vim.ManagedEntity_


Attributes
----------
    vmFolder (`vim.Folder <vim/Folder.rst>`_):
      privilege: System.View
       A reference to the folder hierarchy that contains `VirtualMachine <vim/VirtualMachine.rst>`_ virtual machine templates (identified by the `template <vim/vm/ConfigInfo.rst#template>`_ property, and `VirtualApp <vim/VirtualApp.rst>`_ objects for this datacenter.Note that a VirtualApp that is a child of a `ResourcePool <vim/ResourcePool.rst>`_ may also be visible in this folder. VirtualApp objects can be nested, but only the parent VirtualApp can be visible in the folder.This folder is guaranteed to exist.
    hostFolder (`vim.Folder <vim/Folder.rst>`_):
      privilege: System.View
       A reference to the folder hierarchy that contains the compute resources, including hosts and clusters, for this datacenter.This folder is guaranteed to exist.
    datastoreFolder (`vim.Folder <vim/Folder.rst>`_):
      privilege: System.View
       A reference to the folder hierarchy that contains the datastores for this datacenter.This folder is guaranteed to exist.
    networkFolder (`vim.Folder <vim/Folder.rst>`_):
      privilege: System.View
       A reference to the folder hierarchy that contains the network entities for this datacenter. The folder can include `Network <vim/Network.rst>`_ , `DistributedVirtualSwitch <vim/DistributedVirtualSwitch.rst>`_ , and `DistributedVirtualPortgroup <vim/dvs/DistributedVirtualPortgroup.rst>`_ objects.This folder is guaranteed to exist.
    datastore ([`vim.Datastore <vim/Datastore.rst>`_]):
       A collection of references to the datastore objects available in this datacenter.
    network ([`vim.Network <vim/Network.rst>`_]):
       A collection of references to the network objects available in this datacenter.
    configuration (`vim.Datacenter.ConfigInfo <vim/Datacenter/ConfigInfo.rst>`_):
      privilege: System.View
       Configuration of the datacenter.


Methods
-------


QueryConnectionInfo(hostname, port, username, password, sslThumbprint):
   This method provides a way of getting basic information about a host without adding it to a datacenter. Connection wizards typically use this method to show information about a host so a user can confirm a set of changes before applying them.


  Privilege:
               System.View



  Args:
    hostname (`str <https://docs.python.org/2/library/stdtypes.html>`_):
       The target of the query.


    port (`int <https://docs.python.org/2/library/stdtypes.html>`_):
       The port number of the target host. For ESX 2.x this is the authd port (902 by default). For ESX 3.x and above and for VMware Server hosts this is the https port (443 by default). You can specify -1 to have the vCenter Server try the default ports.


    username (`str <https://docs.python.org/2/library/stdtypes.html>`_):
       The name of the user.


    password (`str <https://docs.python.org/2/library/stdtypes.html>`_):
       The password of the user.


    sslThumbprint (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional, since `VI API 2.5 <vim/version.rst#vimversionversion2>`_ ):
       The expected SSL thumbprint of the host's certificate




  Returns:
    `vim.host.ConnectInfo <vim/host/ConnectInfo.rst>`_:
         

  Raises:

    `vim.fault.InvalidLogin <vim/fault/InvalidLogin.rst>`_: 
       if unable to authenticate with the host.

    `vim.fault.HostConnectFault <vim/fault/HostConnectFault.rst>`_: 
       if an error occurred when querying about a host. Typically, a more specific subclass, such as AlreadyBeingManaged, is thrown.

    `vmodl.fault.NotSupported <vmodl/fault/NotSupported.rst>`_: 
       if called directly on a host.

    `vim.fault.NoHost <vim/fault/NoHost.rst>`_: 
       if unable to contact the host.

    `vim.fault.NotSupportedHost <vim/fault/NotSupportedHost.rst>`_: 
       if the software version on the host is not supported.

    `vim.fault.AlreadyConnected <vim/fault/AlreadyConnected.rst>`_: 
       if the host is already being managed by this server.

    `vim.fault.SSLDisabledFault <vim/fault/SSLDisabledFault.rst>`_: 
       if the host has ssl access disabled

    `vim.fault.SSLVerifyFault <vim/fault/SSLVerifyFault.rst>`_: 
       if the host certificate could not be authenticated


PowerOnMultiVM(vm, option):
   Powers on multiple virtual machines in a data center. If the virtual machines are suspended, this method resumes execution from the suspend point. The virtual machines can belong to different clusters in the data center.If any virtual machine in the list is manually managed by DRS, or DRS has to migrate any manually managed virtual machine or power on any manually managed host in order to power on these virtual machines, a DRS recommendation will be generated, and the users need to manually apply the recommendation for actually powering on these virtual machines. Otherwise, all the virtual machine will be automatically powered on. The virtual machines on stand alone hosts or DRS disabled will be powered-on on the current host. The DRS automatically managed virtual machines will be powered-on on the recommended hosts.When powering on a virtual machine in a cluster, the system might do an implicit relocation of the virtual machine to another host.
  since: `VI API 2.5 <vim/version.rst#vimversionversion2>`_


  Privilege:
               System.View



  Args:
    vm (`vim.VirtualMachine <vim/VirtualMachine.rst>`_):
       The virtual machines to power on.


    option (`vim.option.OptionValue <vim/option/OptionValue.rst>`_, optional, since `vSphere API 4.1 <vim/version.rst#vimversionversion6>`_ ):
       An array of `OptionValue <vim/option/OptionValue.rst>`_ options for this power-on session. The names and values of the options are defined in `ClusterPowerOnVmOption <vim/cluster/PowerOnVmOption.rst>`_ .




  Returns:
     `vim.Task <vim/Task.rst>`_:
         An array of Recommendation.

  Raises:

    `vmodl.fault.InvalidArgument <vmodl/fault/InvalidArgument.rst>`_: 
       for unknown option keys or bad values.


queryDatacenterConfigOptionDescriptor():
   The list of possible choices for `defaultHardwareVersionKey <vim/Datacenter/ConfigSpec.rst#defaultHardwareVersionKey>`_ . Descriptors returned by the vCenter implementation do not have `host <vim/vm/ConfigOptionDescriptor.rst#host>`_ field populated.
  since: `vSphere API 5.1 <vim/version.rst#vimversionversion8>`_


  Privilege:
               System.View



  Args:


  Returns:
    [`vim.vm.ConfigOptionDescriptor <vim/vm/ConfigOptionDescriptor.rst>`_]:
         


ReconfigureDatacenter(spec, modify):
   Change the datacenter configuration.
  since: `vSphere API 5.1 <vim/version.rst#vimversionversion8>`_


  Privilege:
               Datacenter.Reconfigure



  Args:
    spec (`vim.Datacenter.ConfigSpec <vim/Datacenter/ConfigSpec.rst>`_):
       A set of configuration changes to apply to the datacenter. The specification can be a complete set of changes or a partial set of changes, applied incrementally.


    modify (`bool <https://docs.python.org/2/library/stdtypes.html>`_):
       Flag to specify whether the specification ("spec") should be applied incrementally. If "modify" is false and the operation succeeds, then the configuration of the datacenter matches the specification exactly; in this case any unset portions of the specification will result in unset or default portions of the configuration.




  Returns:
     `vim.Task <vim/Task.rst>`_:
         


