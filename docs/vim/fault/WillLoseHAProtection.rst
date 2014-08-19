
vim.fault.WillLoseHAProtection
==============================
    :extends:

        `vim.fault.MigrationFault <vim/fault/MigrationFault.rst>`_

  This fault is reported when the execution of a storage vmotion or relocate operation would impact vSphere HA's ability to restart a VM. For storage vmotion, this fault is reported when HA protection will be lost after the vmotion completes. Consequently, HA would not restart the VM if it subsequently failed. For relocate, relocate is not supported on VMs that failed before the operation is attempted and are in the process of being restarted at the time the operation is performed.

Attributes:

    resolution (`str <https://docs.python.org/2/library/stdtypes.html>`_)




