.. _str: https://docs.python.org/2/library/stdtypes.html

.. _bool: https://docs.python.org/2/library/stdtypes.html

.. _vim.Task: ../../vim/Task.rst

.. _VI API 2.5: ../../vim/version.rst#vimversionversion2

.. _vim.fault.FileFault: ../../vim/fault/FileFault.rst

.. _vim.fault.InvalidState: ../../vim/fault/InvalidState.rst

.. _vim.fault.InvalidBundle: ../../vim/fault/InvalidBundle.rst

.. _vim.fault.MismatchedBundle: ../../vim/fault/MismatchedBundle.rst

.. _RestoreFirmwareConfiguration: ../../vim/host/FirmwareSystem.rst#restoreConfiguration

.. _QueryFirmwareConfigUploadURL: ../../vim/host/FirmwareSystem.rst#queryConfigUploadURL


vim.host.FirmwareSystem
=======================
  The `HostFirmwareSystem`_ managed object type provides access to the firmware of an embedded ESX host. It provides operations to backup, restore, and reset the configuration of an embedded ESX host.


:since: `VI API 2.5`_


Attributes
----------


Methods
-------


ResetFirmwareToFactoryDefaults():
   Reset the configuration to factory defaults.This method will reset all configuration options, including the "admin" password, to the factory defaults. The host will be rebooted immediately. The host needs to be in maintenance mode before this operation can be performed.


  Privilege:
               Host.Config.Firmware



  Args:


  Returns:
    None
         

  Raises:

    `vim.fault.InvalidState`_: 
       if the host is not in maintenance mode.


BackupFirmwareConfiguration():
   Backup the configuration of the host.The method generates a bundle containing the host configuration. You can use an HTTP GET operation to download the bundle from the returned URL.


  Privilege:
               Host.Config.Firmware



  Args:


  Returns:
    `str`_:
         URL that identifies the location of the backup bundle.


QueryFirmwareConfigUploadURL():
   Return the URL on the host to which the configuration bundle must be uploaded for a restore operation. See `RestoreFirmwareConfiguration`_ .


  Privilege:
               Host.Config.Firmware



  Args:


  Returns:
    `str`_:
         URL that identifies the location for the restore operation.


RestoreFirmwareConfiguration(force):
   Restore the configuration of the host to that specified in the bundle.Upload the bundle to the URL returned by the `QueryFirmwareConfigUploadURL`_ method. The `RestoreFirmwareConfiguration`_ method will restore all configuration options, including the "admin" password, to the values in the bundle. The host will be rebooted immediately. The host must be in maintenance mode before this operation can be performed.


  Privilege:
               Host.Config.Firmware



  Args:
    force (`bool`_):
       Forces application of the configuration even if the bundle is mismatched.




  Returns:
    None
         

  Raises:

    `vim.fault.InvalidState`_: 
       if the host is not in maintenance mode.

    `vim.fault.FileFault`_: 
       if the file was not accessible.

    `vim.fault.MismatchedBundle`_: 
       if the uuid / build number in the bundle does not match the uuid / build number of the host and parameter 'force' is set to false.

    `vim.fault.InvalidBundle`_: 
       if the bundle does not have the expected contents.


