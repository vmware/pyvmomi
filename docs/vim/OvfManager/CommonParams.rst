.. _str: https://docs.python.org/2/library/stdtypes.html

.. _vim.KeyValue: ../../vim/KeyValue.rst

.. _ovfImportOption: ../../vim/OvfManager.rst#ovfImportOption

.. _vSphere API 4.0: ../../vim/version.rst#vimversionversion5

.. _vmodl.DynamicData: ../../vmodl/DynamicData.rst


vim.OvfManager.CommonParams
===========================
  A common super-class for basic OVF descriptor parameters
:extends: vmodl.DynamicData_
:since: `vSphere API 4.0`_

Attributes:
    locale (`str`_):

       The locale-identifier to choose from the descriptor. If empty, the default locale on the server is used.
    deploymentOption (`str`_):

       The key of the chosen deployment option. If empty, the default option is chosen. The list of possible deployment options is returned in the result of parseDescriptor.
    msgBundle ([`vim.KeyValue`_], optional):

       An optional set of localization strings to be used. The server will use these message strings to localize information in the result and in error and warning messages.This argument allows a client to pass messages from external string bundles. The client is responsible for selecting the right string bundle (based on locale) and parsing the external string bundle. The passed in key/value pairs are looked up before any messages included in the OVF descriptor itself.
    importOption ([`str`_], optional):

       An optional argument for modifing the OVF parsing. When the server parses an OVF descriptor a set of options can be used to modify the parsing. The argument is a list of keywords.To get a list of supported keywords see `ovfImportOption`_ . Unknown options will be ignored by the server.
