
vim.host.EsxAgentHostManager
============================
  This managed object type is used to configure agent virtual machine resource configuration, such as what network and datastore to use for agent virtual machines.


:since: `vSphere API 5.0 <vim/version.rst#vimversionversion7>`_


Attributes
----------
    configInfo (`vim.host.EsxAgentHostManager.ConfigInfo <vim/host/EsxAgentHostManager/ConfigInfo.rst>`_):
      privilege: Host.Config.Settings
       Configuration of agent virtual machine resources


Methods
-------


EsxAgentHostManagerUpdateConfig(configInfo):
   Update the host's ESX agent configuration. The entire configuration must be set each time since all values are overwritten. E.g. a field set to null clears the value on the host.


  Privilege:
               Host.Config.Settings



  Args:
    configInfo (`vim.host.EsxAgentHostManager.ConfigInfo <vim/host/EsxAgentHostManager/ConfigInfo.rst>`_):
       configuration of agent virtual machine resources




  Returns:
    None
         

  Raises:

    `vim.fault.HostConfigFault <vim/fault/HostConfigFault.rst>`_: 
       if an error occurs.


