.. _int: https://docs.python.org/2/library/stdtypes.html

.. _str: https://docs.python.org/2/library/stdtypes.html

.. _datetime: https://docs.python.org/2/library/stdtypes.html

.. _vmodl.fault.NotEnoughLicenses: ../../vmodl/fault/NotEnoughLicenses.rst


vim.fault.ExpiredFeatureLicense
===============================
    :extends:

        `vmodl.fault.NotEnoughLicenses`_

  An ExpiredFeatureLicense fault is thrown if an attempt to acquire an Addon license 'feature failed for count 'count'.

Attributes:

    feature (`str`_)

    count (`int`_)

    expirationDate (`datetime`_)




