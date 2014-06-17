.. _str: https://docs.python.org/2/library/stdtypes.html

.. _datetime: https://docs.python.org/2/library/stdtypes.html

.. _VI API 2.5: ../../vim/version.rst#vimversionversion2

.. _vmodl.DynamicData: ../../vmodl/DynamicData.rst


vim.host.BIOSInfo
=================
  
:extends: vmodl.DynamicData_
:since: `VI API 2.5`_

Attributes:
    biosVersion (`str`_, optional):

       The current BIOS version of the physical chassis
    releaseDate (`datetime`_, optional):

       The release date for the BIOS.
