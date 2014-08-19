
vim.fault.OperationDisallowedOnHost
===================================
    :extends:

        `vmodl.RuntimeFault <vmodl/RuntimeFault.rst>`_

  An OperationDisallowedOnHost is thrown if an operation is diasllowed on host when a direct connection is used. Examples for such operations include VM powering on / memory hot-plug which could potentially violate hard-enforcement licenses if allowed on host. The functionality these operations provide is still available, but only through calls to an external entity.

Attributes:




