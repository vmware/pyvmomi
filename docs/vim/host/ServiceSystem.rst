
vim.host.ServiceSystem
======================
  The `HostServiceSystem <vim/host/ServiceSystem.rst>`_ managed object describes the configuration of host services. This managed object operates in conjunction with the `HostFirewallSystem <vim/host/FirewallSystem.rst>`_ managed object.


:extends: vim.ExtensibleManagedObject_


Attributes
----------
    serviceInfo (`vim.host.ServiceInfo <vim/host/ServiceInfo.rst>`_):
       Service configuration.


Methods
-------


UpdateServicePolicy(id, policy):
   Updates the activation policy of the service.


  Privilege:
               Host.Config.NetService



  Args:
    id (`str <https://docs.python.org/2/library/stdtypes.html>`_):
       Service identifier ( `serviceInfo <vim/host/ServiceSystem.rst#serviceInfo>`_ . `service <vim/host/ServiceInfo.rst#service>`_ . `key <vim/host/Service.rst#key>`_ ).


    policy (`str <https://docs.python.org/2/library/stdtypes.html>`_):
       Specifies the condition for service activation. Use one of the `HostServicePolicy <vim/host/Service/Policy.rst>`_ values.




  Returns:
    None
         

  Raises:

    `vim.fault.NotFound <vim/fault/NotFound.rst>`_: 
       if the service ID is unknown.

    `vim.fault.HostConfigFault <vim/fault/HostConfigFault.rst>`_: 
       for all other failures.

    `vmodl.fault.InvalidArgument <vmodl/fault/InvalidArgument.rst>`_: 
       if the service ID represents a required service, or if the specified policy is undefined.


StartService(id):
   Starts the service.


  Privilege:
               Host.Config.NetService



  Args:
    id (`str <https://docs.python.org/2/library/stdtypes.html>`_):
       Service identifier ( `serviceInfo <vim/host/ServiceSystem.rst#serviceInfo>`_ . `service <vim/host/ServiceInfo.rst#service>`_ . `key <vim/host/Service.rst#key>`_ ).




  Returns:
    None
         

  Raises:

    `vim.fault.InvalidState <vim/fault/InvalidState.rst>`_: 
       if the service is already running. Only hosts with ESX/ESXi 4.1 or earlier software use this fault. Hosts running later versions of ESXi do not throw a fault in this case.

    `vim.fault.NotFound <vim/fault/NotFound.rst>`_: 
       if the service ID is unknown.

    `vim.fault.HostConfigFault <vim/fault/HostConfigFault.rst>`_: 
       for all other failures.


StopService(id):
   Stops the service.


  Privilege:
               Host.Config.NetService



  Args:
    id (`str <https://docs.python.org/2/library/stdtypes.html>`_):
       Service identifier ( `serviceInfo <vim/host/ServiceSystem.rst#serviceInfo>`_ . `service <vim/host/ServiceInfo.rst#service>`_ . `key <vim/host/Service.rst#key>`_ ).




  Returns:
    None
         

  Raises:

    `vim.fault.InvalidState <vim/fault/InvalidState.rst>`_: 
       if the service is not running. Only hosts with ESX/ESXi 4.1 or earlier software use this fault. Hosts running later versions of ESXi do not throw a fault in this case.

    `vim.fault.NotFound <vim/fault/NotFound.rst>`_: 
       if the service ID is unknown.

    `vim.fault.HostConfigFault <vim/fault/HostConfigFault.rst>`_: 
       for all other failures.


RestartService(id):
   Restarts the service.


  Privilege:
               Host.Config.NetService



  Args:
    id (`str <https://docs.python.org/2/library/stdtypes.html>`_):
       Service identifier ( `serviceInfo <vim/host/ServiceSystem.rst#serviceInfo>`_ . `service <vim/host/ServiceInfo.rst#service>`_ . `key <vim/host/Service.rst#key>`_ ).




  Returns:
    None
         

  Raises:

    `vim.fault.InvalidState <vim/fault/InvalidState.rst>`_: 
       if the service is not running. Only hosts with ESX/ESXi 4.1 or earlier software use this fault. Hosts running later versions of ESXi do not throw a fault in this case.

    `vim.fault.NotFound <vim/fault/NotFound.rst>`_: 
       if the service ID is unknown.

    `vim.fault.HostConfigFault <vim/fault/HostConfigFault.rst>`_: 
       for all other failures.


UninstallService(id):
   Uninstalls the service. If the service is running, it is stopped before being uninstalled.


  Privilege:
               Host.Config.NetService



  Args:
    id (`str <https://docs.python.org/2/library/stdtypes.html>`_):
       Service identifier ( `serviceInfo <vim/host/ServiceSystem.rst#serviceInfo>`_ . `service <vim/host/ServiceInfo.rst#service>`_ . `key <vim/host/Service.rst#key>`_ ).




  Returns:
    None
         

  Raises:

    `vim.fault.NotFound <vim/fault/NotFound.rst>`_: 
       if the service ID is unknown.

    `vim.fault.HostConfigFault <vim/fault/HostConfigFault.rst>`_: 
       for all other failures.

    `vmodl.fault.InvalidArgument <vmodl/fault/InvalidArgument.rst>`_: 
       if the service is a required service.

    `vmodl.fault.NotSupported <vmodl/fault/NotSupported.rst>`_: 
       if the service doesn't support uninstallation.


RefreshServices():
   Refresh the service information and settings to pick up any changes made directly on the host.


  Privilege:
               Host.Config.NetService



  Args:


  Returns:
    None
         


