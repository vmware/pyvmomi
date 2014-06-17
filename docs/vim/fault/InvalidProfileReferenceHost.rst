.. _str: https://docs.python.org/2/library/stdtypes.html

.. _string: ../../str

.. _vmodl.RuntimeFault: ../../vmodl/RuntimeFault.rst


vim.fault.InvalidProfileReferenceHost
=====================================
    :extends:

        `vmodl.RuntimeFault`_

  A InvalidProfileReferenceHost fault is thrown when a valid host is not associated with a profile in the Virtual Center inventory. This could be because there is no host assciated with the profile or because the associated host is incompatible with the profile.

Attributes:

    reason (`str`_): is optional.

    host (`str`_): is optional.

    profile (`str`_): is optional.




