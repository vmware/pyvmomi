.. _vim.Task: ../../vim/Task.rst

.. _vSphere API 4.0: ../../vim/version.rst#vimversionversion5

.. _vim.host.PciPassthruInfo: ../../vim/host/PciPassthruInfo.rst

.. _vim.fault.HostConfigFault: ../../vim/fault/HostConfigFault.rst

.. _vim.host.PciPassthruConfig: ../../vim/host/PciPassthruConfig.rst

.. _vim.ExtensibleManagedObject: ../../vim/ExtensibleManagedObject.rst


vim.host.PciPassthruSystem
==========================
  This managed object manages the PciPassthru state of the host.


:extends: vim.ExtensibleManagedObject_
:since: `vSphere API 4.0`_


Attributes
----------
    pciPassthruInfo (`vim.host.PciPassthruInfo`_):
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
    config (`vim.host.PciPassthruConfig`_):
       The new PciPassthru configuration information.




  Returns:
    None
         

  Raises:

    `vim.fault.HostConfigFault`_: 
       if an error occurs.


