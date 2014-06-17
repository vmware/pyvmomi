.. _str: https://docs.python.org/2/library/stdtypes.html

.. _vSphere API 4.0: ../../vim/version.rst#vimversionversion5

.. _vim.event.LicenseEvent: ../../vim/event/LicenseEvent.rst


vim.event.LicenseNonComplianceEvent
===================================
  This event records that the inventory is not license compliant.
:extends: vim.event.LicenseEvent_
:since: `vSphere API 4.0`_

Attributes:
    url (`str`_):

       Gives the url at which more details about non-compliance can be found.
