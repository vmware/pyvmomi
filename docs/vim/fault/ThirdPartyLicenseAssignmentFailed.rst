
vim.fault.ThirdPartyLicenseAssignmentFailed
===========================================
    :extends:

        `vmodl.RuntimeFault <vmodl/RuntimeFault.rst>`_

  A ThirdPartyLicenseAssignmentFailed fault is thrown when the license assignment to a 3rd party module fails. The 3rd-party modules are installed and ran on ESX hosts, so this fault provides both host and module IDs.

Attributes:

    host (`str <https://docs.python.org/2/library/stdtypes.html>`_)

    module (`str <https://docs.python.org/2/library/stdtypes.html>`_)

    reason (`str <https://docs.python.org/2/library/stdtypes.html>`_): is optional.




