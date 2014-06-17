.. _vim.fault.VmConfigFault: ../../vim/fault/VmConfigFault.rst


vim.fault.UnsupportedVmxLocation
================================
    :extends:

        `vim.fault.VmConfigFault`_

  ESX 3 Server products requires the .vmx file to be stored on NAS or VMFS3 storage. If attempting to power on a virtual machine with the .vmx file stored on the service console, this fault will be thrown.

Attributes:




