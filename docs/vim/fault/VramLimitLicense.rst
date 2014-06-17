.. _int: https://docs.python.org/2/library/stdtypes.html

.. _vmodl.fault.NotEnoughLicenses: ../../vmodl/fault/NotEnoughLicenses.rst


vim.fault.VramLimitLicense
==========================
    :extends:

        `vmodl.fault.NotEnoughLicenses`_

  A VramLimitLicense fault is thrown if executing an operation would result in exceeding maximum allowed vRAM amount. For example, this could happen when powering on a VM, hot-plugging memory into a running VMm, etc.

Attributes:

    limit (`int`_)




