.. _vim.Task: ../../vim/Task.rst

.. _vim.host.AutoStartManager.Config: ../../vim/host/AutoStartManager/Config.rst


vim.host.AutoStartManager
=========================
  The AutoStartManager allows clients to invoke and set up the auto-start/auto-stop order of virtual machines on a single host. Virtual machines configured to use auto-start are automatically started or stopped when the host is started or shut down. The AutoStartManager is available when clients connect directly to a host, such as an ESX Server machine or through VirtualCenter.




Attributes
----------
    config (`vim.host.AutoStartManager.Config`_):
       


Methods
-------


ReconfigureAutostart(spec):
   Changes the power-on or power-off sequence and system defaults. The specification is an incremental change to the current configuration.If systemDefaults are included, only values that are specified in the specification are changed.For the spec.powerInfo array, each element is interpreted as an incremental change and the changes are processed sequentially. It is not an error to remove a non-existing virtual machine. If both startAction and stopAction are set to none, then the virtual machine is removed from the configuration.A virtual machine's position in the order can be changed either by assigning the virtual machine a different position in the order or removing the machine from the order. When a virtual machine's position changes, all other virtual machines' positions may be affected as they move to new positions relative to each other.


  Privilege:
               Host.Config.AutoStart



  Args:
    spec (`vim.host.AutoStartManager.Config`_):
       List of changes to defaults and auto-start/auto-stop order.




  Returns:
    None
         


AutoStartPowerOn():
   Powers-on virtual machines according to the current AutoStart configuration.See the description of the (@link vim.host.AutoStartManager.AutoPowerInfo) data object type for more information on Auto power-on behavior.


  Privilege:
               Host.Config.AutoStart



  Args:


  Returns:
    None
         


AutoStartPowerOff():
   Powers-off virtual machines according to the current AutoStart configuration.See the description of the (@link vim.host.AutoStartManager.AutoPowerInfo) data object type for more information on Auto power-off behavior.


  Privilege:
               Host.Config.AutoStart



  Args:


  Returns:
    None
         


