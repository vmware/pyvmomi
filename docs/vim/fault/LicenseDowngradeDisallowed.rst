.. _str: https://docs.python.org/2/library/stdtypes.html

.. _string: ../../str

.. _vmodl.fault.NotEnoughLicenses: ../../vmodl/fault/NotEnoughLicenses.rst


vim.fault.LicenseDowngradeDisallowed
====================================
    :extends:

        `vmodl.fault.NotEnoughLicenses`_

  A LicenseDowngradeDisallowed fault is thrown if an assignment operation tries to downgrade a license that does have certain licensed features which are in use.

Attributes:

    edition (`str`_)

    entityId (`str`_)

    features (`str`_)




