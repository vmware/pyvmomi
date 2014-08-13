.. _str: https://docs.python.org/2/library/stdtypes.html

.. _vSphere API 4.0: ../vim/version.rst#vimversionversion5

.. _vim.Description: ../vim/Description.rst

.. _vmodl.KeyAnyValue: ../vmodl/KeyAnyValue.rst


vim.ExtendedDescription
=======================
  
:extends: vim.Description_
:since: `vSphere API 4.0`_

Attributes:
    messageCatalogKeyPrefix (`str`_):

       Key to the localized message string in the catalog. If the localized string contains parameters, values to the parameters will be provided in #messageArg. E.g: If the message in the catalog is "IP address is {address}", value for "address" will be provided by #messageArg. Both summary and label in Description will have a corresponding entry in the message catalog with the keys.summary and.label respectively. Description.summary and Description.label will contain the strings in server locale.
    messageArg ([`vmodl.KeyAnyValue`_], optional):

       Provides named arguments that can be used to localize the message in the catalog.
