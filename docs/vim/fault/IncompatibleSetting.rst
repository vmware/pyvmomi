.. _str: https://docs.python.org/2/library/stdtypes.html

.. _vmodl.fault.InvalidArgument: ../../vmodl/fault/InvalidArgument.rst


vim.fault.IncompatibleSetting
=============================
    :extends:

        `vmodl.fault.InvalidArgument`_

  Thrown when two parameters in the customization settings conflict with each other. For example, a client may not specify both a Workgroup and a DomainName.

Attributes:

    conflictingProperty (`str`_)




