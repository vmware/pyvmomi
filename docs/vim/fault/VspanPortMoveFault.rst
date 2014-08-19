
vim.fault.VspanPortMoveFault
============================
    :extends:

        `vim.fault.DvsFault <vim/fault/DvsFault.rst>`_

  Thrown when moving a port used as tranmistted source or destination ports in vspan session to a promiscuous portgroup if this operation may change the non-promiscuous port to promiscuous mode.

Attributes:

    srcPortgroupName (`str <https://docs.python.org/2/library/stdtypes.html>`_)

    destPortgroupName (`str <https://docs.python.org/2/library/stdtypes.html>`_)

    portKey (`str <https://docs.python.org/2/library/stdtypes.html>`_)




