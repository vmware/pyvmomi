
vim.MacRange
============
  This class defines a range of MAC address.
:extends: vim.MacAddress_
:since: `vSphere API 5.5 <vim/version.rst#vimversionversion9>`_

Attributes:
    address (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       MAC address.
    mask (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       Mask that is used in matching the MAC address. A MAC address is considered matched if the "and" operation of the mask on the MAC address and `address <vim/MacRange.rst#address>`_ yields the same result. For example, a MAC of "00:A0:FF:14:FF:29" is considered matched for a `address <vim/MacRange.rst#address>`_ of "00:A0:C9:14:C8:29" and a `mask <vim/MacRange.rst#mask>`_ of "FF:FF:00:FF:00:FF".
