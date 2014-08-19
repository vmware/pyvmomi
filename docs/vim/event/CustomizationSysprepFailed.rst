
vim.event.CustomizationSysprepFailed
====================================
  Sysprep failed to run in the guest during customization. This will most like have been caused by the fact that the wrong sysprep was used for the guest, so we include the version information in the event.
:extends: vim.event.CustomizationFailed_
:since: `VI API 2.5 <vim/version.rst#vimversionversion2>`_

Attributes:
    sysprepVersion (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       The version string for the sysprep files that were included in the customization package.
    systemVersion (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       The version string for the system
