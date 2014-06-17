.. _str: https://docs.python.org/2/library/stdtypes.html

.. _VI API 2.5: ../../vim/version.rst#vimversionversion2

.. _vim.event.CustomizationFailed: ../../vim/event/CustomizationFailed.rst


vim.event.CustomizationSysprepFailed
====================================
  Sysprep failed to run in the guest during customization. This will most like have been caused by the fact that the wrong sysprep was used for the guest, so we include the version information in the event.
:extends: vim.event.CustomizationFailed_
:since: `VI API 2.5`_

Attributes:
    sysprepVersion (`str`_):

       The version string for the sysprep files that were included in the customization package.
    systemVersion (`str`_):

       The version string for the system
