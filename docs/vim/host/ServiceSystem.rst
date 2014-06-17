.. _str: https://docs.python.org/2/library/stdtypes.html

.. _vim.Task: ../../vim/Task.rst

.. _vim.fault.NotFound: ../../vim/fault/NotFound.rst

.. _vim.host.ServiceInfo: ../../vim/host/ServiceInfo.rst

.. _vim.fault.InvalidState: ../../vim/fault/InvalidState.rst

.. _vmodl.fault.NotSupported: ../../vmodl/fault/NotSupported.rst

.. _vim.fault.HostConfigFault: ../../vim/fault/HostConfigFault.rst

.. _vmodl.fault.InvalidArgument: ../../vmodl/fault/InvalidArgument.rst

.. _vim.ExtensibleManagedObject: ../../vim/ExtensibleManagedObject.rst


vim.host.ServiceSystem
======================
  The `HostServiceSystem`_ managed object describes the configuration of host services. This managed object operates in conjunction with the `HostFirewallSystem`_ managed object.


:extends: vim.ExtensibleManagedObject_


Attributes
----------
    serviceInfo (`vim.host.ServiceInfo`_):
       Service configuration.


Methods
-------


UpdateServicePolicy(id, policy):
   Updates the activation policy of the service.


  Privilege:
               Host.Config.NetService



  Args:
    id (`str`_):
       Service identifier ( `serviceInfo`_ . `service`_ . `key`_ ).


    policy (`str`_):
       Specifies the condition for service activation. Use one of the `HostServicePolicy`_ values.




  Returns:
    None
         

  Raises:

    `vim.fault.NotFound`_: 
       if the service ID is unknown.

    `vim.fault.HostConfigFault`_: 
       for all other failures.

    `vmodl.fault.InvalidArgument`_: 
       if the service ID represents a required service, or if the specified policy is undefined.


StartService(id):
   Starts the service.


  Privilege:
               Host.Config.NetService



  Args:
    id (`str`_):
       Service identifier ( `serviceInfo`_ . `service`_ . `key`_ ).




  Returns:
    None
         

  Raises:

    `vim.fault.InvalidState`_: 
       if the service is already running. Only hosts with ESX/ESXi 4.1 or earlier software use this fault. Hosts running later versions of ESXi do not throw a fault in this case.

    `vim.fault.NotFound`_: 
       if the service ID is unknown.

    `vim.fault.HostConfigFault`_: 
       for all other failures.


StopService(id):
   Stops the service.


  Privilege:
               Host.Config.NetService



  Args:
    id (`str`_):
       Service identifier ( `serviceInfo`_ . `service`_ . `key`_ ).




  Returns:
    None
         

  Raises:

    `vim.fault.InvalidState`_: 
       if the service is not running. Only hosts with ESX/ESXi 4.1 or earlier software use this fault. Hosts running later versions of ESXi do not throw a fault in this case.

    `vim.fault.NotFound`_: 
       if the service ID is unknown.

    `vim.fault.HostConfigFault`_: 
       for all other failures.


RestartService(id):
   Restarts the service.


  Privilege:
               Host.Config.NetService



  Args:
    id (`str`_):
       Service identifier ( `serviceInfo`_ . `service`_ . `key`_ ).




  Returns:
    None
         

  Raises:

    `vim.fault.InvalidState`_: 
       if the service is not running. Only hosts with ESX/ESXi 4.1 or earlier software use this fault. Hosts running later versions of ESXi do not throw a fault in this case.

    `vim.fault.NotFound`_: 
       if the service ID is unknown.

    `vim.fault.HostConfigFault`_: 
       for all other failures.


UninstallService(id):
   Uninstalls the service. If the service is running, it is stopped before being uninstalled.


  Privilege:
               Host.Config.NetService



  Args:
    id (`str`_):
       Service identifier ( `serviceInfo`_ . `service`_ . `key`_ ).




  Returns:
    None
         

  Raises:

    `vim.fault.NotFound`_: 
       if the service ID is unknown.

    `vim.fault.HostConfigFault`_: 
       for all other failures.

    `vmodl.fault.InvalidArgument`_: 
       if the service is a required service.

    `vmodl.fault.NotSupported`_: 
       if the service doesn't support uninstallation.


RefreshServices():
   Refresh the service information and settings to pick up any changes made directly on the host.


  Privilege:
               Host.Config.NetService



  Args:


  Returns:
    None
         


