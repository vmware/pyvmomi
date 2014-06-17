.. _str: https://docs.python.org/2/library/stdtypes.html

.. _string: ../../str

.. _vmodl.RuntimeFault: ../../vmodl/RuntimeFault.rst


vim.fault.ThirdPartyLicenseAssignmentFailed
===========================================
    :extends:

        `vmodl.RuntimeFault`_

  A ThirdPartyLicenseAssignmentFailed fault is thrown when the license assignment to a 3rd party module fails. The 3rd-party modules are installed and ran on ESX hosts, so this fault provides both host and module IDs.

Attributes:

    host (`str`_)

    module (`str`_)

    reason (`str`_): is optional.




