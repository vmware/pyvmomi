.. _str: https://docs.python.org/2/library/stdtypes.html

.. _vim.Task: ../../vim/Task.rst

.. _vSphere API 5.5: ../../vim/version.rst#vimversionversion9

.. _vim.fault.NotFound: ../../vim/fault/NotFound.rst

.. _vim.fault.ResourceInUse: ../../vim/fault/ResourceInUse.rst

.. _vim.fault.HostConfigFault: ../../vim/fault/HostConfigFault.rst

.. _vim.fault.InaccessibleVFlashSource: ../../vim/fault/InaccessibleVFlashSource.rst

.. _HostVFlashResourceConfigurationResult: ../../vim/host/VFlashResourceConfigurationResult.rst

.. _vim.host.VFlashManager.VFlashConfigInfo: ../../vim/host/VFlashManager/VFlashConfigInfo.rst

.. _vim.host.VFlashResourceConfigurationResult: ../../vim/host/VFlashResourceConfigurationResult.rst

.. _vim.host.VFlashManager.VFlashCacheConfigSpec: ../../vim/host/VFlashManager/VFlashCacheConfigSpec.rst

.. _vim.host.VFlashManager.VFlashResourceConfigSpec: ../../vim/host/VFlashManager/VFlashResourceConfigSpec.rst

.. _vim.vm.device.VirtualDisk.VFlashCacheConfigInfo: ../../vim/vm/device/VirtualDisk/VFlashCacheConfigInfo.rst


vim.host.VFlashManager
======================
  The VFlash Manager object is used to configure vFlash resource and vFlash cache on the ESX host.


:since: `vSphere API 5.5`_


Attributes
----------
    vFlashConfigInfo (`vim.host.VFlashManager.VFlashConfigInfo`_):
       Host vFlash configuration information.


Methods
-------


ConfigureVFlashResourceEx(devicePath):
   Configure vFlash resource on a list of SSD disks. If the host does not have a VFFS volume, host will format the volume first and then extend the volume on the rest of the SSDs; otherwise host will extend the existing VFFS volume on the passed SSDs. Finally host will configure the vFlash resource on the VFFS volume.It will return `HostVFlashResourceConfigurationResult`_ describing success or failure associated with each device.


  Privilege:
               Host.Config.Storage



  Args:
    devicePath (`str`_, optional):
       An array of device path names that identify disks. See `ScsiDisk`_ .




  Returns:
     `vim.Task`_:


  Raises:

    `vim.fault.HostConfigFault`_:
       if batch operation fails on the host. Because the returned VFlashResourceConfigurationResult contains the configuration success or fault for each device, as of vSphere API 5.x, we won't throw fault when batch operation fails.


HostConfigureVFlashResource(spec):
   Configure vFlash resource on the host by attaching to a backend VFFS volume.


  Privilege:
               Host.Config.Storage



  Args:
    spec (`vim.host.VFlashManager.VFlashResourceConfigSpec`_):
       the vFlash resource specification.




  Returns:
    None


  Raises:

    `vim.fault.HostConfigFault`_:
       If vFlash resource cannot be configured on the host

    `vim.fault.ResourceInUse`_:
       The contained VFFS volume is being used.


HostRemoveVFlashResource():
   Remove vFlash resource on the host by destroying the contained VFFS volume.


  Privilege:
               Host.Config.Storage



  Args:


  Returns:
    None


  Raises:

    `vim.fault.NotFound`_:
       If vFlash resource is not configured or the contained VFFS volume cannot be found on the host.

    `vim.fault.HostConfigFault`_:
       If vFlash resource or the contained VFFS volume cannot be removed from the host.

    `vim.fault.ResourceInUse`_:
       The contained VFFS volume is being used.


HostConfigVFlashCache(spec):
   Configure vFlash cache on the host.


  Privilege:
               Host.Config.AdvancedConfig



  Args:
    spec (`vim.host.VFlashManager.VFlashCacheConfigSpec`_):
       Specification for host cache configuration.




  Returns:
    None


  Raises:

    `vim.fault.HostConfigFault`_:
       If the swap cache cannot be configured on the host.

    `vim.fault.InaccessibleVFlashSource`_:
       vFlash resource is not accessible.

    `vim.fault.ResourceInUse`_:
       The contained VFFS volume is being used.


HostGetVFlashModuleDefaultConfig(vFlashModule):
   Retrieve the default supported configuration for a given vFlash module


  Privilege:
               Host.Config.AdvancedConfig



  Args:
    vFlashModule (`str`_):
       Name of the vFlash module




  Returns:
    `vim.vm.device.VirtualDisk.VFlashCacheConfigInfo`_:
         The supported default vFlash cache configuration

  Raises:

    `vim.fault.NotFound`_:
       If vFlash resource is not configured or the contained VFFS volume cannot be found on the host.

    `vim.fault.HostConfigFault`_:
       If the default vFlash module configuration option cannot be retrieved.
