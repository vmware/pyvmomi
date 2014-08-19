
vim.host.DateTimeSystem
=======================
  This managed object provides for NTP and date/time related configuration on a host. Information regarding the running status of the NTP daemon and functionality to start and stop the daemon is provided by the `HostServiceSystem <vim/host/ServiceSystem.rst>`_ object.


:since: `VI API 2.5 <vim/version.rst#vimversionversion2>`_


Attributes
----------
    dateTimeInfo (`vim.host.DateTimeInfo <vim/host/DateTimeInfo.rst>`_):
      privilege: System.Read
       The DateTime configuration of the host.


Methods
-------


UpdateDateTimeConfig(config):
   Update the DateTime configuration of the host.


  Privilege:
               Host.Config.DateTime



  Args:
    config (`vim.host.DateTimeConfig <vim/host/DateTimeConfig.rst>`_):
       The new DateTime configuration information.




  Returns:
    None
         

  Raises:

    `vim.fault.HostConfigFault <vim/fault/HostConfigFault.rst>`_: 
       if an error occurs.


QueryAvailableTimeZones():
   Retrieves the list of available timezones on the host. The API works off the public domain 'tz' timezone database.


  Privilege:
               System.Read



  Args:


  Returns:
    [`vim.host.DateTimeSystem.TimeZone <vim/host/DateTimeSystem/TimeZone.rst>`_]:
         List of available timezones on the host.


QueryDateTime():
   Get the current DateTime on the host.


  Privilege:
               System.Read



  Args:


  Returns:
    `datetime <https://docs.python.org/2/library/stdtypes.html>`_:
         Current DateTime on the host.


UpdateDateTime(dateTime):
   Update the date/time on the host. This method should be used with caution since network delays, execution delays can result in time skews.


  Privilege:
               Host.Config.DateTime



  Args:
    dateTime (`datetime <https://docs.python.org/2/library/stdtypes.html>`_):
       DateTime to update the host to.




  Returns:
    None
         

  Raises:

    `vim.fault.HostConfigFault <vim/fault/HostConfigFault.rst>`_: 
       if an error occurs.


RefreshDateTimeSystem():
   Refresh the DateTime related settings to pick up any changes that might have occurred.


  Privilege:
               Host.Config.DateTime



  Args:


  Returns:
    None
         


