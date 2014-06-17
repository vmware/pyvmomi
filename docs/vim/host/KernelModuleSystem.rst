.. _str: https://docs.python.org/2/library/stdtypes.html

.. _vim.Task: ../../vim/Task.rst

.. _VI API 2.5u2: ../../vim/version.rst#vimversionversion3

.. _vSphere API 4.0: ../../vim/version.rst#vimversionversion5

.. _vim.fault.NotFound: ../../vim/fault/NotFound.rst

.. _vim.host.KernelModuleSystem.ModuleInfo: ../../vim/host/KernelModuleSystem/ModuleInfo.rst


vim.host.KernelModuleSystem
===========================
  The KernelModuleSystem managed object controls the configuration of kernel modules on the host.


:since: `VI API 2.5u2`_


Attributes
----------


Methods
-------


QueryModules():
   Query the set of modules on the host.
  since: `vSphere API 4.0`_


  Privilege:
               Host.Config.Settings



  Args:


  Returns:
    `vim.host.KernelModuleSystem.ModuleInfo`_:
         


UpdateModuleOptionString(name, options):
   Specifies the options to be passed to the kernel module when loaded.


  Privilege:
               Host.Config.Settings



  Args:
    name (`str`_):
       Module name.


    options (`str`_):
       Option string to be passed to the kernel module at load time.




  Returns:
    None
         

  Raises:

    `vim.fault.NotFound`_: 
       if the kernel module does not exist on the host.


QueryConfiguredModuleOptionString(name):
   Query the options configured to be passed to the kernel module when loaded. Note that this is not necessarily the option string currently in use by the kernel module.


  Privilege:
               Host.Config.Settings



  Args:
    name (`str`_):
       Module name.




  Returns:
    `str`_:
         Option string to be passed to the kernel module at load time.

  Raises:

    `vim.fault.NotFound`_: 
       if the kernel module does not exist on the host.


