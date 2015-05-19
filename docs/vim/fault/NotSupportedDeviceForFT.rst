.. _str: https://docs.python.org/2/library/stdtypes.html

.. _string: ../../str

.. _vim.fault.VmFaultToleranceIssue: ../../vim/fault/VmFaultToleranceIssue.rst


vim.fault.NotSupportedDeviceForFT
=================================
    :extends:

        `vim.fault.VmFaultToleranceIssue`_

  VMs with pvscsi or vmxnet3 virtual devices support Fault Tolerance only on 4.1 or later hosts.

Attributes:

    host (`str`_)

    hostName (`str`_): is optional.

    vm (`str`_)

    vmName (`str`_): is optional.

    deviceType (`str`_)

    deviceLabel (`str`_): is optional.




