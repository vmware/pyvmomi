.. _str: https://docs.python.org/2/library/stdtypes.html

.. _vim.Task: ../../vim/Task.rst

.. _vSphere API 4.0: ../../vim/version.rst#vimversionversion5

.. _vim.fault.HostConfigFault: ../../vim/fault/HostConfigFault.rst

.. _vmodl.fault.InvalidArgument: ../../vmodl/fault/InvalidArgument.rst

.. _vim.ExtensibleManagedObject: ../../vim/ExtensibleManagedObject.rst

.. _vim.host.VirtualNicManagerInfo: ../../vim/host/VirtualNicManagerInfo.rst

.. _vim.host.VirtualNicManager.NetConfig: ../../vim/host/VirtualNicManager/NetConfig.rst


vim.host.VirtualNicManager
==========================
  The VirtualNicManager managed object describes the special Virtual NIC configuration of the host.


:extends: vim.ExtensibleManagedObject_
:since: `vSphere API 4.0`_


Attributes
----------
    info (`vim.host.VirtualNicManagerInfo`_):
       Network configuration.


Methods
-------


QueryNetConfig(nicType):
   Get the NetConfig for the specified nicType


  Privilege:
               Host.Config.Network



  Args:
    nicType (`str`_):
       The NicType




  Returns:
    `vim.host.VirtualNicManager.NetConfig`_:
         

  Raises:

    `vim.fault.HostConfigFault`_: 
       for any other failure.

    `vmodl.fault.InvalidArgument`_: 
       if nicType is invalid


SelectVnicForNicType(nicType, device):
   Select the NicType of the VirtualNic. Selecting a device automatically deselects the previous selection if NetConfig#multiSelectAllowed is false for the specified nicType. Else, the device is added to the list of selected nics.


  Privilege:
               Host.Config.Network



  Args:
    nicType (`str`_):
       The type of VirtualNic that would be selected


    device (`str`_):
       The device that uniquely identifies the VirtualNic.




  Returns:
    None
         

  Raises:

    `vim.fault.HostConfigFault`_: 
       for any other failure.

    `vmodl.fault.InvalidArgument`_: 
       if nicType is invalid, or device represents a nonexistent or invalid VirtualNic


DeselectVnicForNicType(nicType, device):
   Deselect the VirtualNic to be a special type.


  Privilege:
               Host.Config.Network



  Args:
    nicType (`str`_):
       The type of VirtualNic that would be deselected


    device (`str`_):
       The device that uniquely identifies the VirtualNic.




  Returns:
    None
         

  Raises:

    `vim.fault.HostConfigFault`_: 
       for any other failure.

    `vmodl.fault.InvalidArgument`_: 
       if nicType is invalid, device represents a nonexistent or invalid VirtualNic, or the VirtualNic is not selected


