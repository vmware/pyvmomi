.. _str: https://docs.python.org/2/library/stdtypes.html

.. _vmodl.RuntimeFault: ../../vmodl/RuntimeFault.rst


vim.fault.ConflictingDatastoreFound
===================================
    :extends:

        `vmodl.RuntimeFault`_

  ConflictingDatastoreFound is thrown when the conflicting datastores with the same url but backed by different disks are found in the host and the target datacenter.

Attributes:

    name (`str`_)

    url (`str`_)




