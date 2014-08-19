
vim.fault.VMotionInterfaceIssue
===============================
    :extends:

        `vim.fault.MigrationFault <vim/fault/MigrationFault.rst>`_

  A VMotion interface has a problem. This may be an error or warning depending on the specific fault subclass. This is an error or warning only when migrating a powered-on virtual machine.

Attributes:

    atSourceHost (`bool <https://docs.python.org/2/library/stdtypes.html>`_)

    failedHost (`str <https://docs.python.org/2/library/stdtypes.html>`_)

    failedHostEntity (`str <https://docs.python.org/2/library/stdtypes.html>`_): is optional.




