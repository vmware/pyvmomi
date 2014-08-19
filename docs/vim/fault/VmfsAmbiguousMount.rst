
vim.fault.VmfsAmbiguousMount
============================
    :extends:

        `vim.fault.VmfsMountFault <vim/fault/VmfsMountFault.rst>`_

  An 'VmfsAmbiguousMount' fault occurs when ESX is unable to resolve the extents of a VMFS volume unambiguously. This is thrown only when a VMFS volume has multiple extents and multiple copies of VMFS volumes are available. VMFS layer will not be able to determine how to re-construct the VMFS volume as multiple choices are available.

Attributes:




