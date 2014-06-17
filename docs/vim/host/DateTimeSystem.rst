.. _vim.Task: ../../vim/Task.rst

.. _datetime: https://docs.python.org/2/library/stdtypes.html

.. _VI API 2.5: ../../vim/version.rst#vimversionversion2

.. _vim.host.DateTimeInfo: ../../vim/host/DateTimeInfo.rst

.. _vim.host.DateTimeConfig: ../../vim/host/DateTimeConfig.rst

.. _vim.fault.HostConfigFault: ../../vim/fault/HostConfigFault.rst

.. _vim.host.DateTimeSystem.TimeZone: ../../vim/host/DateTimeSystem/TimeZone.rst


vim.host.DateTimeSystem
=======================
  This managed object provides for NTP and date/time related configuration on a host. Information regarding the running status of the NTP daemon and functionality to start and stop the daemon is provided by the `HostServiceSystem`_ object.


:since: `VI API 2.5`_


Attributes
----------
    dateTimeInfo (`vim.host.DateTimeInfo`_):
      privilege: System.Read
       The DateTime configuration of the host.


Methods
-------


UpdateDateTimeConfig(config):
   Update the DateTime configuration of the host.


  Privilege:
               Host.Config.DateTime



  Args:
    config (`vim.host.DateTimeConfig`_):
       The new DateTime configuration information.




  Returns:
    None
         

  Raises:

    `vim.fault.HostConfigFault`_: 
       if an error occurs.


QueryAvailableTimeZones():
   Retrieves the list of available timezones on the host. The API works off the public domain 'tz' timezone database.


  Privilege:
               System.Read



  Args:


  Returns:
    `vim.host.DateTimeSystem.TimeZone`_:
         List of available timezones on the host.


QueryDateTime():
   Get the current DateTime on the host.


  Privilege:
               System.Read



  Args:


  Returns:
    `datetime`_:
         Current DateTime on the host.


UpdateDateTime(dateTime):
   Update the date/time on the host. This method should be used with caution since network delays, execution delays can result in time skews.


  Privilege:
               Host.Config.DateTime



  Args:
    dateTime (`datetime`_):
       DateTime to update the host to.




  Returns:
    None
         

  Raises:

    `vim.fault.HostConfigFault`_: 
       if an error occurs.


RefreshDateTimeSystem():
   Refresh the DateTime related settings to pick up any changes that might have occurred.


  Privilege:
               Host.Config.DateTime



  Args:


  Returns:
    None
         


