.. _str: https://docs.python.org/2/library/stdtypes.html

.. _string: ../../str

.. _vim.fault.ResourceInUse: ../../vim/fault/ResourceInUse.rst


vim.fault.QuiesceDatastoreIOForHAFailed
=======================================
    :extends:

        `vim.fault.ResourceInUse`_

  A QuiesceDatastoreIOForHAFailed fault occurs when the HA agent on a host cannot quiesce file activity on a datastore to be unmouonted or removed.

Attributes:

    host (`str`_)

    hostName (`str`_)

    ds (`str`_)

    dsName (`str`_)




