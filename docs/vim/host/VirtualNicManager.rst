
vim.host.VirtualNicManager
==========================
  The VirtualNicManager managed object describes the special Virtual NIC configuration of the host.


:extends: vim.ExtensibleManagedObject_
:since: `vSphere API 4.0 <vim/version.rst#vimversionversion5>`_


Attributes
----------
    info (`vim.host.VirtualNicManagerInfo <vim/host/VirtualNicManagerInfo.rst>`_):
       Network configuration.


Methods
-------


QueryNetConfig(nicType):
   Get the NetConfig for the specified nicType


  Privilege:
               Host.Config.Network



  Args:
    nicType (`str <https://docs.python.org/2/library/stdtypes.html>`_):
       The NicType




  Returns:
    `vim.host.VirtualNicManager.NetConfig <vim/host/VirtualNicManager/NetConfig.rst>`_:
         

  Raises:

    `vim.fault.HostConfigFault <vim/fault/HostConfigFault.rst>`_: 
       for any other failure.

    `vmodl.fault.InvalidArgument <vmodl/fault/InvalidArgument.rst>`_: 
       if nicType is invalid


SelectVnicForNicType(nicType, device):
   Select the NicType of the VirtualNic. Selecting a device automatically deselects the previous selection if NetConfig#multiSelectAllowed is false for the specified nicType. Else, the device is added to the list of selected nics.


  Privilege:
               Host.Config.Network



  Args:
    nicType (`str <https://docs.python.org/2/library/stdtypes.html>`_):
       The type of VirtualNic that would be selected


    device (`str <https://docs.python.org/2/library/stdtypes.html>`_):
       The device that uniquely identifies the VirtualNic.




  Returns:
    None
         

  Raises:

    `vim.fault.HostConfigFault <vim/fault/HostConfigFault.rst>`_: 
       for any other failure.

    `vmodl.fault.InvalidArgument <vmodl/fault/InvalidArgument.rst>`_: 
       if nicType is invalid, or device represents a nonexistent or invalid VirtualNic


DeselectVnicForNicType(nicType, device):
   Deselect the VirtualNic to be a special type.


  Privilege:
               Host.Config.Network



  Args:
    nicType (`str <https://docs.python.org/2/library/stdtypes.html>`_):
       The type of VirtualNic that would be deselected


    device (`str <https://docs.python.org/2/library/stdtypes.html>`_):
       The device that uniquely identifies the VirtualNic.




  Returns:
    None
         

  Raises:

    `vim.fault.HostConfigFault <vim/fault/HostConfigFault.rst>`_: 
       for any other failure.

    `vmodl.fault.InvalidArgument <vmodl/fault/InvalidArgument.rst>`_: 
       if nicType is invalid, device represents a nonexistent or invalid VirtualNic, or the VirtualNic is not selected


