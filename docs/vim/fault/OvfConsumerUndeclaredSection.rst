.. _str: https://docs.python.org/2/library/stdtypes.html

.. _vim.fault.OvfConsumerCallbackFault: ../../vim/fault/OvfConsumerCallbackFault.rst


vim.fault.OvfConsumerUndeclaredSection
======================================
    :extends:

        `vim.fault.OvfConsumerCallbackFault`_

  A fault type indicating that an OVF consumer appended an undeclared section to an OST.An undeclared section means a section with a qualified type that the OVF consumer was not registered as a handler of.

Attributes:

    qualifiedSectionType (`str`_)




