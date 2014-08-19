
vim.fault.HAErrorsAtDest
========================
    :extends:

        `vim.fault.MigrationFault <vim/fault/MigrationFault.rst>`_

  The destination compute resource is HA-enabled, and HA is not running properly. This will cause the following problems: 1) The VM will not have HA protection. 2) If this is an intracluster VMotion, HA will not be properly informed that the migration completed. This can have serious consequences to the functioning of HA.

Attributes:




