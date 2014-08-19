
vim.fault.LicenseDowngradeDisallowed
====================================
    :extends:

        `vmodl.fault.NotEnoughLicenses <vmodl/fault/NotEnoughLicenses.rst>`_

  A LicenseDowngradeDisallowed fault is thrown if an assignment operation tries to downgrade a license that does have certain licensed features which are in use.

Attributes:

    edition (`str <https://docs.python.org/2/library/stdtypes.html>`_)

    entityId (`str <https://docs.python.org/2/library/stdtypes.html>`_)

    features (`str <https://docs.python.org/2/library/stdtypes.html>`_)




