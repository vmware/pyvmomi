
vim.fault.VspanPortgroupTypeChangeFault
=======================================
    :extends:

        `vim.fault.DvsFault <vim/fault/DvsFault.rst>`_

  Thrown when changing a portgroup from static/dynamic binding to ephemeral(no binding) if any ports in this portgroup participate in Distributed Port Mirroring session.

Attributes:

    portgroupName (`str <https://docs.python.org/2/library/stdtypes.html>`_)




