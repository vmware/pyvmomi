
vim.fault.NotSupportedDeviceForFT
=================================
    :extends:

        `vim.fault.VmFaultToleranceIssue <vim/fault/VmFaultToleranceIssue.rst>`_

  VMs with pvscsi or vmxnet3 virtual devices support Fault Tolerance only on 4.1 or later hosts.

Attributes:

    host (`str <https://docs.python.org/2/library/stdtypes.html>`_)

    hostName (`str <https://docs.python.org/2/library/stdtypes.html>`_): is optional.

    vm (`str <https://docs.python.org/2/library/stdtypes.html>`_)

    vmName (`str <https://docs.python.org/2/library/stdtypes.html>`_): is optional.

    deviceType (`str <https://docs.python.org/2/library/stdtypes.html>`_)

    deviceLabel (`str <https://docs.python.org/2/library/stdtypes.html>`_): is optional.




