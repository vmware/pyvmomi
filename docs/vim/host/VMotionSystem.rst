
vim.host.VMotionSystem
======================
  The VMotionSystem managed object describes the VMotion configuration of the host.


:extends: vim.ExtensibleManagedObject_


Attributes
----------
    netConfig (`vim.host.VMotionSystem.NetConfig <vim/host/VMotionSystem/NetConfig.rst>`_):
       VMotion network configuration.
    ipConfig (`vim.host.IpConfig <vim/host/IpConfig.rst>`_):
       IP configuration of the VMotion VirtualNic.


Methods
-------


UpdateIpConfig(ipConfig):
   Update the IP configuration of VMotion VirtualNic.


  Privilege:
               Host.Config.Network



  Args:
    ipConfig (`vim.host.IpConfig <vim/host/IpConfig.rst>`_):




  Returns:
    None
         

  Raises:

    `vim.fault.NotFound <vim/fault/NotFound.rst>`_: 
       if no VirtualNic is selected for VMotion.

    `vim.fault.HostConfigFault <vim/fault/HostConfigFault.rst>`_: 
       for any other failure

    `vmodl.fault.InvalidArgument <vmodl/fault/InvalidArgument.rst>`_: 
       if the IpConfig is invalid or cannot be used.


SelectVnic(device):
   Select the VirtualNic to be used for VMotion.


  Privilege:
               Host.Config.Network



  Args:
    device (`str <https://docs.python.org/2/library/stdtypes.html>`_):
       The device that uniquely identifies the VirtualNic.




  Returns:
    None
         

  Raises:

    `vim.fault.HostConfigFault <vim/fault/HostConfigFault.rst>`_: 
       for any other failure

    `vmodl.fault.InvalidArgument <vmodl/fault/InvalidArgument.rst>`_: 
       if key represents a nonexistent or invalid VirtualNic.


DeselectVnic():
   Indicate that no VirtualNic should be used for VMotion.


  Privilege:
               Host.Config.Network



  Args:


  Returns:
    None
         

  Raises:

    `vim.fault.HostConfigFault <vim/fault/HostConfigFault.rst>`_: 
       is a failure occurred


