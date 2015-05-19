.. _str: https://docs.python.org/2/library/stdtypes.html

.. _vim.Task: ../../vim/Task.rst

.. _VI API 2.5: ../../vim/version.rst#vimversionversion2

.. _vim.host.BootDeviceInfo: ../../vim/host/BootDeviceInfo.rst

.. _vmodl.fault.NotSupported: ../../vmodl/fault/NotSupported.rst


vim.host.BootDeviceSystem
=========================
  The `HostBootDeviceSystem`_ managed object provides methods to query and update a host boot device configuration.


:since: `VI API 2.5`_


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
    `vim.host.BootDeviceInfo`_:
         The boot device information for the host. The returned object has a list of `HostBootDevice`_ data objects; each boot device object defines a description and a key to identify the device. The order of devices in the list is unpredictable. The returned `HostBootDeviceInfo`_ data object also contains the key of the current boot device.


UpdateBootDevice(key):
   Sets the current boot device for the host system.


  Privilege:
               Host.Config.Maintenance



  Args:
    key (`str`_):
       The `key`_ of the `HostBootDevice`_ from which the host will boot.




  Returns:
    None
         

  Raises:

    `vmodl.fault.NotSupported`_: 
       if the host does not support updating bootDevices.


