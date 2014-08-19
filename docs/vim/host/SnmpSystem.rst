
vim.host.SnmpSystem
===================
  Provision the SNMP Version 1,2c agent. This object is accessed through the `HostConfigManager <vim/host/ConfigManager.rst>`_ object.




Attributes
----------
    configuration (`vim.host.SnmpSystem.SnmpConfigSpec <vim/host/SnmpSystem/SnmpConfigSpec.rst>`_):
      privilege: Global.Settings
       
    limits (`vim.host.SnmpSystem.AgentLimits <vim/host/SnmpSystem/AgentLimits.rst>`_):
      privilege: Global.Settings
       


Methods
-------


ReconfigureSnmpAgent(spec):
   
  since: `VI API 2.5 <vim/version.rst#vimversionversion2>`_


  Privilege:
               Global.Settings



  Args:
    spec (`vim.host.SnmpSystem.SnmpConfigSpec <vim/host/SnmpSystem/SnmpConfigSpec.rst>`_):




  Returns:
    None
         

  Raises:

    `vim.fault.NotFound <vim/fault/NotFound.rst>`_: 
       vim.fault.NotFound

    `vim.fault.InsufficientResourcesFault <vim/fault/InsufficientResourcesFault.rst>`_: 
       vim.fault.InsufficientResourcesFault


SendTestNotification():
   
  since: `VI API 2.5 <vim/version.rst#vimversionversion2>`_


  Privilege:
               Global.Settings



  Args:


  Returns:
    None
         

  Raises:

    `vim.fault.NotFound <vim/fault/NotFound.rst>`_: 
       vim.fault.NotFound

    `vim.fault.InsufficientResourcesFault <vim/fault/InsufficientResourcesFault.rst>`_: 
       vim.fault.InsufficientResourcesFault


