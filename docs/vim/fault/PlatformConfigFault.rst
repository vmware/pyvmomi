
vim.fault.PlatformConfigFault
=============================
    :extends:

        `vim.fault.HostConfigFault <vim/fault/HostConfigFault.rst>`_

  A PlatformConfigFault is a catch-all fault indicating that some error has occurred regarding the configuration of the host. Data about the fault is available and will be presented as a platform specific string.This information carried by this fault cannot be localized. Most likely this information will already have been localized to the locale of the server that generated this fault. Where possible, a more specific fault will be thrown.

Attributes:

    text (`str <https://docs.python.org/2/library/stdtypes.html>`_)




