
vim.fault.VmWwnConflict
=======================
    :extends:

        `vim.fault.InvalidVmConfig <vim/fault/InvalidVmConfig.rst>`_

  Thrown if a user attempts to assign a WWN that is currently being used by other virtual machine or host.

Attributes:

    vm (`str <https://docs.python.org/2/library/stdtypes.html>`_): is optional.

    host (`str <https://docs.python.org/2/library/stdtypes.html>`_): is optional.

    name (`str <https://docs.python.org/2/library/stdtypes.html>`_): is optional.

    wwn (`long <https://docs.python.org/2/library/stdtypes.html>`_): is optional.




