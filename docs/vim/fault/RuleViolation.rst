
vim.fault.RuleViolation
=======================
    :extends:

        `vim.fault.VmConfigFault <vim/fault/VmConfigFault.rst>`_

  The virtual machine if powered on, would violate an affinity/anti-affinity rule. In this case, the VM can still be powered on manually by a user who knows what they are doing, but VirtualCenter will never automatically move or power on a VM such that it triggers the violation.

Attributes:

    host (`str <https://docs.python.org/2/library/stdtypes.html>`_): is optional.

    rule (`str <https://docs.python.org/2/library/stdtypes.html>`_)




