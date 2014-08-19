
vim.fault.EightHostLimitViolated
================================
    :extends:

        `vim.fault.VmConfigFault <vim/fault/VmConfigFault.rst>`_

  Only virtual machines on eight different hosts can have a single virtual disk backing opened for read at once.This fault occurs when moving or powering on this virtual machine would cause a violation of the above constraint. This only occurs when multiple virtual machines are sharing a single disk backing.Note that there is no limit on the number of virtual machines who share a disk backings, so long as they are running on eight or fewer hosts.

Attributes:




