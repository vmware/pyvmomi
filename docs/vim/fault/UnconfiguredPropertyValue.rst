.. _vim.fault.InvalidPropertyValue: ../../vim/fault/InvalidPropertyValue.rst


vim.fault.UnconfiguredPropertyValue
===================================
    :extends:

        `vim.fault.InvalidPropertyValue`_

  The property value has not been configured by the user, so the application cannot be started. This is thrown if a property value is the empty string and the types does not allow it. For example, for an integer type or a string where the minimum length is 1, and so forth.

Attributes:




