
vim.host.CacheConfigurationManager
==================================
  Solid state drive Cache Configuration Manager. This is a managed object which provides access to ESX performance tuning features using solid state drive based cache.


:since: `vSphere API 5.0 <vim/version.rst#vimversionversion7>`_


Attributes
----------
    cacheConfigurationInfo ([`vim.host.CacheConfigurationManager.CacheConfigurationInfo <vim/host/CacheConfigurationManager/CacheConfigurationInfo.rst>`_]):
      privilege: Host.Config.AdvancedConfig
       The swap performance configuration for the ESX host. This includes configuration information for each datastore enabled for this purpose.


Methods
-------


ConfigureHostCache(spec):
   Configure host cache/swap performance enhancement.


  Privilege:
               Host.Config.AdvancedConfig



  Args:
    spec (`vim.host.CacheConfigurationManager.CacheConfigurationSpec <vim/host/CacheConfigurationManager/CacheConfigurationSpec.rst>`_):
       Specification for solid state drive cache configuration.




  Returns:
     `vim.Task <vim/Task.rst>`_:
         

  Raises:

    `vmodl.fault.InvalidArgument <vmodl/fault/InvalidArgument.rst>`_: 
       if swap cache is not supported on this datastore, or if swapSize is negative.

    `vmodl.fault.SystemError <vmodl/fault/SystemError.rst>`_: 
       if the operation fails due to unexpected reason, i.e.: out of disk space situation.


