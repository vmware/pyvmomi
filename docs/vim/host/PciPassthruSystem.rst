
vim.host.PciPassthruSystem
==========================
  This managed object manages the PciPassthru state of the host.


:extends: vim.ExtensibleManagedObject_
:since: `vSphere API 4.0 <vim/version.rst#vimversionversion5>`_


Attributes
----------
    pciPassthruInfo ([`vim.host.PciPassthruInfo <vim/host/PciPassthruInfo.rst>`_]):
      privilege: System.Read
       Array of PciPassthru information


Methods
-------


Refresh():
   Refresh the available PciPassthru information.


  Privilege:
               Host.Config.Settings



  Args:


  Returns:
    None
         


UpdatePassthruConfig(config):
   Updates the PciPassthru configuration, this will get called for the dependent device with the enabled bool set


  Privilege:
               Host.Config.PciPassthru



  Args:
    config (`vim.host.PciPassthruConfig <vim/host/PciPassthruConfig.rst>`_):
       The new PciPassthru configuration information.




  Returns:
    None
         

  Raises:

    `vim.fault.HostConfigFault <vim/fault/HostConfigFault.rst>`_: 
       if an error occurs.


