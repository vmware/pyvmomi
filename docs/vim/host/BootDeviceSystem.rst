
vim.host.BootDeviceSystem
=========================
  The `HostBootDeviceSystem <vim/host/BootDeviceSystem.rst>`_ managed object provides methods to query and update a host boot device configuration.


:since: `VI API 2.5 <vim/version.rst#vimversionversion2>`_


Attributes
----------


Methods
-------


QueryBootDevices():
   Retrieves a list of the available boot devices for the host system.


  Privilege:
               System.Read



  Args:


  Returns:
    `vim.host.BootDeviceInfo <vim/host/BootDeviceInfo.rst>`_:
         The boot device information for the host. The returned object has a list of `HostBootDevice <vim/host/BootDeviceSystem/BootDevice.rst>`_ data objects; each boot device object defines a description and a key to identify the device. The order of devices in the list is unpredictable. The returned `HostBootDeviceInfo <vim/host/BootDeviceInfo.rst>`_ data object also contains the key of the current boot device.


UpdateBootDevice(key):
   Sets the current boot device for the host system.


  Privilege:
               Host.Config.Maintenance



  Args:
    key (`str <https://docs.python.org/2/library/stdtypes.html>`_):
       The `key <vim/host/BootDeviceSystem/BootDevice.rst#key>`_ of the `HostBootDevice <vim/host/BootDeviceSystem/BootDevice.rst>`_ from which the host will boot.




  Returns:
    None
         

  Raises:

    `vmodl.fault.NotSupported <vmodl/fault/NotSupported.rst>`_: 
       if the host does not support updating bootDevices.


