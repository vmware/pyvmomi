.. _vim.Task: ../../vim/Task.rst

.. _VI API 2.5: ../../vim/version.rst#vimversionversion2

.. _vim.fault.NotFound: ../../vim/fault/NotFound.rst

.. _vim.host.SnmpSystem.AgentLimits: ../../vim/host/SnmpSystem/AgentLimits.rst

.. _vim.host.SnmpSystem.SnmpConfigSpec: ../../vim/host/SnmpSystem/SnmpConfigSpec.rst

.. _vim.fault.InsufficientResourcesFault: ../../vim/fault/InsufficientResourcesFault.rst


vim.host.SnmpSystem
===================
  Provision the SNMP Version 1,2c agent. This object is accessed through the `HostConfigManager`_ object.




Attributes
----------
    configuration (`vim.host.SnmpSystem.SnmpConfigSpec`_):
      privilege: Global.Settings
       
    limits (`vim.host.SnmpSystem.AgentLimits`_):
      privilege: Global.Settings
       


Methods
-------


ReconfigureSnmpAgent(spec):
   
  since: `VI API 2.5`_


  Privilege:
               Global.Settings



  Args:
    spec (`vim.host.SnmpSystem.SnmpConfigSpec`_):




  Returns:
    None
         

  Raises:

    `vim.fault.NotFound`_: 
       vim.fault.NotFound

    `vim.fault.InsufficientResourcesFault`_: 
       vim.fault.InsufficientResourcesFault


SendTestNotification():
   
  since: `VI API 2.5`_


  Privilege:
               Global.Settings



  Args:


  Returns:
    None
         

  Raises:

    `vim.fault.NotFound`_: 
       vim.fault.NotFound

    `vim.fault.InsufficientResourcesFault`_: 
       vim.fault.InsufficientResourcesFault


