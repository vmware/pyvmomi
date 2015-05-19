.. _str: https://docs.python.org/2/library/stdtypes.html

.. _vim.Task: ../../vim/Task.rst

.. _vim.host.IpConfig: ../../vim/host/IpConfig.rst

.. _vim.fault.NotFound: ../../vim/fault/NotFound.rst

.. _vim.fault.HostConfigFault: ../../vim/fault/HostConfigFault.rst

.. _vmodl.fault.InvalidArgument: ../../vmodl/fault/InvalidArgument.rst

.. _vim.ExtensibleManagedObject: ../../vim/ExtensibleManagedObject.rst

.. _vim.host.VMotionSystem.NetConfig: ../../vim/host/VMotionSystem/NetConfig.rst


vim.host.VMotionSystem
======================
  The VMotionSystem managed object describes the VMotion configuration of the host.


:extends: vim.ExtensibleManagedObject_


Attributes
----------
    netConfig (`vim.host.VMotionSystem.NetConfig`_):
       VMotion network configuration.
    ipConfig (`vim.host.IpConfig`_):
       IP configuration of the VMotion VirtualNic.


Methods
-------


UpdateIpConfig(ipConfig):
   Update the IP configuration of VMotion VirtualNic.


  Privilege:
               Host.Config.Network



  Args:
    ipConfig (`vim.host.IpConfig`_):




  Returns:
    None
         

  Raises:

    `vim.fault.NotFound`_: 
       if no VirtualNic is selected for VMotion.

    `vim.fault.HostConfigFault`_: 
       for any other failure

    `vmodl.fault.InvalidArgument`_: 
       if the IpConfig is invalid or cannot be used.


SelectVnic(device):
   Select the VirtualNic to be used for VMotion.


  Privilege:
               Host.Config.Network



  Args:
    device (`str`_):
       The device that uniquely identifies the VirtualNic.




  Returns:
    None
         

  Raises:

    `vim.fault.HostConfigFault`_: 
       for any other failure

    `vmodl.fault.InvalidArgument`_: 
       if key represents a nonexistent or invalid VirtualNic.


DeselectVnic():
   Indicate that no VirtualNic should be used for VMotion.


  Privilege:
               Host.Config.Network



  Args:


  Returns:
    None
         

  Raises:

    `vim.fault.HostConfigFault`_: 
       is a failure occurred


