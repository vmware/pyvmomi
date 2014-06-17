.. _int: https://docs.python.org/2/library/stdtypes.html

.. _str: https://docs.python.org/2/library/stdtypes.html

.. _VI API 2.5: ../../../vim/version.rst#vimversionversion2

.. _vmodl.DynamicData: ../../../vmodl/DynamicData.rst


vim.host.DateTimeSystem.TimeZone
================================
  
:extends: vmodl.DynamicData_
:since: `VI API 2.5`_

Attributes:
    key (`str`_):

       The identifier for the time zone.
    name (`str`_):

       The time zone name.
    description (`str`_):

       Description of the time zone.
    gmtOffset (`int`_):

       The GMT offset in seconds that is currently applicable to the timezone (with respect to the current time on the host).
