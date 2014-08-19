vim.host.VirtualNicManager.NicType
==================================
  :contained by: `vim.host.VirtualNicManager <vim/host/VirtualNicManager.rst>`_

  :type: `vim.host.VirtualNicManager.NicType <vim/host/VirtualNicManager/NicType.rst>`_

  :name: vsan

values:
--------

vsan
   The VirtualNic is used for VSAN traffic. To enable or disable a VirtualNic for VSAN networking, use `UpdateVsan_Task <vim/host/VsanSystem.rst#update>`_ .See `HostVsanSystem <vim/host/VsanSystem.rst>`_ See `UpdateVsan_Task <vim/host/VsanSystem.rst#update>`_ See `ReconfigureComputeResource_Task <vim/ComputeResource.rst#reconfigureEx>`_ 

faultToleranceLogging
   The VirtualNic is used for Fault Tolerance logging.

vSphereReplication
   The VirtualNic is used for vSphere Replication LWD traffic (i.e From the primary host to the VR server).

management
   The VirtualNic is used for management network traffic . This nicType is available only when the system does not support service console adapters.See `usesServiceConsoleNic <vim/host/NetCapabilities.rst#usesServiceConsoleNic>`_ 

vmotion
   The VirtualNic is used for VMotion.
