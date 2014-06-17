.. _str: https://docs.python.org/2/library/stdtypes.html

.. _vim.fault.VMotionInterfaceIssue: ../../vim/fault/VMotionInterfaceIssue.rst


vim.fault.VMotionLinkCapacityLow
================================
    :extends:

        `vim.fault.VMotionInterfaceIssue`_

  The VMotion interface does not have the recommended capacity to support VMotion. VMotion is supported on links that have a speed of at least 1000 Mbps and are full duplex. This is a warning for migrating powered-on virtual machines.

Attributes:

    network (`str`_)




