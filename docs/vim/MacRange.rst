.. _str: https://docs.python.org/2/library/stdtypes.html

.. _mask: ../vim/MacRange.rst#mask

.. _address: ../vim/MacRange.rst#address

.. _vim.MacAddress: ../vim/MacAddress.rst

.. _vSphere API 5.5: ../vim/version.rst#vimversionversion9


vim.MacRange
============
  This class defines a range of MAC address.
:extends: vim.MacAddress_
:since: `vSphere API 5.5`_

Attributes:
    address (`str`_):

       MAC address.
    mask (`str`_):

       Mask that is used in matching the MAC address. A MAC address is considered matched if the "and" operation of the mask on the MAC address and `address`_ yields the same result. For example, a MAC of "00:A0:FF:14:FF:29" is considered matched for a `address`_ of "00:A0:C9:14:C8:29" and a `mask`_ of "FF:FF:00:FF:00:FF".
