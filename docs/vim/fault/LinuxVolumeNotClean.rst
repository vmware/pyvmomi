.. _vim.fault.CustomizationFault: ../../vim/fault/CustomizationFault.rst


vim.fault.LinuxVolumeNotClean
=============================
    :extends:

        `vim.fault.CustomizationFault`_

  Customization operation is performed on a linux source vm that was not shut down properly. If the filesystem has significant fsck errors on it, customization process cannot make changes to it.

Attributes:




