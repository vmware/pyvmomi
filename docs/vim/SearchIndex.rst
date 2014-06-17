.. _str: https://docs.python.org/2/library/stdtypes.html

.. _bool: https://docs.python.org/2/library/stdtypes.html

.. _vim.Task: ../vim/Task.rst

.. _hostName: ../vim/vm/GuestInfo.rst#hostName

.. _ipAddress: ../vim/vm/GuestInfo.rst#ipAddress

.. _Datacenter: ../vim/Datacenter.rst

.. _ResourcePool: ../vim/ResourcePool.rst

.. _vim.Datacenter: ../vim/Datacenter.rst

.. _vSphere API 4.0: ../vim/version.rst#vimversionversion5

.. _ComputeResource: ../vim/ComputeResource.rst

.. _vim.ManagedEntity: ../vim/ManagedEntity.rst

.. _vim.VirtualMachine: ../vim/VirtualMachine.rst

.. _vim.fault.InvalidDatastore: ../vim/fault/InvalidDatastore.rst


vim.SearchIndex
===============
  The SearchIndex service allows a client to efficiently query the inventory for a specific managed entity by attributes such as UUID, IP address, DNS name, or datastore path. Such searches typically return a VirtualMachine or a HostSystem. While searching, only objects for which the user has sufficient privileges are considered. The findByInventoryPath and findChild operations only search on entities for which the user has view privileges; all other SearchIndex find operations only search virtual machines and hosts for which the user has read privileges. If the user does not have sufficient privileges for an object that matches the search criteria, that object is not returned.




Attributes
----------


Methods
-------


FindByUuid(datacenter, uuid, vmSearch, instanceUuid):
   Finds a virtual machine or host by BIOS or instance UUID.


  Privilege:
               System.View



  Args:
    datacenter (`vim.Datacenter`_, optional):
       If specified, restricts the query to entities in a particular datacenter. If not specified, the entire inventory is searched.


    uuid (`str`_):
       The UUID to find. If vmSearch is true, the uuid can be either BIOS or instance UUID.


    vmSearch (`bool`_):
       If true, search for virtual machines, otherwise search for hosts.


    instanceUuid (`bool`_, optional, since `vSphere API 4.0`_ ):
       Should only be set when vmSearch is true. If specified, search for virtual machines whose instance UUID matches the given uuid. Otherwise, search for virtual machines whose BIOS UUID matches the given uuid.




  Returns:
    `vim.ManagedEntity`_:
         The virtual machine or host managed entity that is found. If no managed entities are found, null is returned. Only a single entity is returned, even if there are multiple matches.


FindByDatastorePath(datacenter, path):
   Finds a virtual machine by its location on a datastore.


  Privilege:
               System.View



  Args:
    datacenter (`vim.Datacenter`_):
       Specifies the datacenter to which the datastore path belongs.


    path (`str`_):
       A datastore path to the .vmx file for the virtual machine.




  Returns:
    `vim.VirtualMachine`_:
         The virtual machine that is found. If no virtual machine is found, null is returned. Only a single entity is returned, even if there are multiple matches.

  Raises:

    `vim.fault.InvalidDatastore`_: 
       if a datastore has not been specified in the path or if the specified datastore does not exist on the specified datacenter.


FindByDnsName(datacenter, dnsName, vmSearch):
   Finds a virtual machine or host by DNS name. The DNS name for a virtual machine is the one returned from VMware tools, `hostName`_ .


  Privilege:
               System.View



  Args:
    datacenter (`vim.Datacenter`_, optional):
       If specified, restricts the query to entities in a particular datacenter. If not specified, the entire inventory is searched.


    dnsName (`str`_):
       The fully qualified domain name to find.


    vmSearch (`bool`_):
       if true, search for virtual machines, otherwise search for hosts.




  Returns:
    `vim.ManagedEntity`_:
         The virtual machine or host managed entity that is found. If no managed entities are found, null is returned. Only a single entity is returned, even if there are multiple matches.


FindByIp(datacenter, ip, vmSearch):
   Finds a virtual machine or host by IP address, where the IP address is in dot-decimal notation. For example, 10.17.12.12. The IP address for a virtual machine is the one returned from VMware tools, `ipAddress`_ .


  Privilege:
               System.View



  Args:
    datacenter (`vim.Datacenter`_, optional):
       If specified, restricts the query to entities in a particular datacenter. If not specified, the entire inventory is searched.


    ip (`str`_):
       The dot-decimal notation formatted IP address to find.


    vmSearch (`bool`_):
       if true, search for virtual machines, otherwise search for hosts.




  Returns:
    `vim.ManagedEntity`_:
         The virtual machine or host managed entity that is found. If no managed entities are found, null is returned. Only a single entity is returned, even if there are multiple matches. If called directly on an ESX server with vmSearch set to false, returns the host managed entity if the address matches any of the Console OS IP addresses.


FindByInventoryPath(inventoryPath):
   Finds a managed entity based on its location in the inventory. The path is separated by slashes ('/'). For example, a path should be of the form "My Folder/My Datacenter/vm/Discovered VM/VM1". A leading slash or trailing slash is ignored. Thus, the following paths all represents the same object: "a/b", "/a/b", "a/b/", and '/a/b/'. Slashes in names must be represented using %2f, following the standard URL syntax. Any object in the inventory can be retrieved using this method, including resource pools and hosts.


  Privilege:
               System.View



  Args:
    inventoryPath (`str`_):
       The path to the entity.




  Returns:
    `vim.ManagedEntity`_:
         The managed entity that is found. If no match is found, null is returned.


FindChild(entity, name):
   Finds a particular child based on a managed entity name. This only searches the immediate children of a managed entity. For a `Datacenter`_ , the host and vm folders are considered children. For a `ComputeResource`_ , the hosts and root `ResourcePool`_ are considered children.


  Privilege:
               System.View



  Args:
    entity (`vim.ManagedEntity`_):
       A reference to a managed entity.


    name (`str`_):
       The name of the child object.




  Returns:
    `vim.ManagedEntity`_:
         The managed entity that is found, or null if no match is found.


FindAllByUuid(datacenter, uuid, vmSearch, instanceUuid):
   Finds all virtual machines or hosts by UUID.
  since: `vSphere API 4.0`_


  Privilege:
               System.View



  Args:
    datacenter (`vim.Datacenter`_, optional):
       If specified, restricts the query to entities in a particular datacenter. If not specified, the entire inventory is searched.


    uuid (`str`_):
       The UUID to find. If vmSearch is true, the UUID can be either BIOS or instance UUID.


    vmSearch (`bool`_):
       If true, search for virtual machines, otherwise search for hosts.


    instanceUuid (`bool`_, optional):
       Should only be set when vmSearch is true. If specified, search for virtual machines whose instance UUID matches the given uuid. Otherwise, search for virtual machines whose BIOS UUID matches the given uuid.




  Returns:
    `vim.ManagedEntity`_:
         The list of all virtual machines or hosts that are matching with the given UUID. If no managed entities are found, an empty list is returned. If there are multiple matches, all matching entities are returned.


FindAllByDnsName(datacenter, dnsName, vmSearch):
   Finds all virtual machines or hosts by DNS name. The DNS name for a virtual machine is the one returned from VMware tools, `hostName`_ .
  since: `vSphere API 4.0`_


  Privilege:
               System.View



  Args:
    datacenter (`vim.Datacenter`_, optional):
       If specified, restricts the query to entities in a particular datacenter. If not specified, the entire inventory is searched.


    dnsName (`str`_):
       The fully qualified domain name to find.


    vmSearch (`bool`_):
       If true, search for virtual machines, otherwise search for hosts.




  Returns:
    `vim.ManagedEntity`_:
         The list of all virtual machines or hosts that are found. If no managed entities are found, an empty list is returned. If there are multiple matches, all matching entities are returned.


FindAllByIp(datacenter, ip, vmSearch):
   Finds all virtual machines or hosts by IP address, where the IP address is in dot-decimal notation. For example, 10.17.12.12. The IP address for a virtual machine is the one returned from VMware tools, `ipAddress`_ .
  since: `vSphere API 4.0`_


  Privilege:
               System.View



  Args:
    datacenter (`vim.Datacenter`_, optional):
       If specified, restricts the query to entities in a particular datacenter. If not specified, the entire inventory is searched.


    ip (`str`_):
       The dot-decimal notation formatted IP address to find.


    vmSearch (`bool`_):
       If true, search for virtual machines, otherwise search for hosts.




  Returns:
    `vim.ManagedEntity`_:
         The list of all virtual machines or hosts that are found. If no managed entities are found, an empty list is returned. If there are multiple matches, all matching entities are returned.


