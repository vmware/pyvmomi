.. _str: https://docs.python.org/2/library/stdtypes.html

.. _bool: https://docs.python.org/2/library/stdtypes.html

.. _string: ../../str

.. _vim.fault.MigrationFault: ../../vim/fault/MigrationFault.rst


vim.fault.VMotionInterfaceIssue
===============================
    :extends:

        `vim.fault.MigrationFault`_

  A VMotion interface has a problem. This may be an error or warning depending on the specific fault subclass. This is an error or warning only when migrating a powered-on virtual machine.

Attributes:

    atSourceHost (`bool`_)

    failedHost (`str`_)

    failedHostEntity (`str`_): is optional.




