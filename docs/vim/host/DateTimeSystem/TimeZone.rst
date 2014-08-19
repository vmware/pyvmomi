
vim.host.DateTimeSystem.TimeZone
================================
  
:extends: vmodl.DynamicData_
:since: `VI API 2.5 <vim/version.rst#vimversionversion2>`_

Attributes:
    key (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       The identifier for the time zone.
    name (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       The time zone name.
    description (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       Description of the time zone.
    gmtOffset (`int <https://docs.python.org/2/library/stdtypes.html>`_):

       The GMT offset in seconds that is currently applicable to the timezone (with respect to the current time on the host).
