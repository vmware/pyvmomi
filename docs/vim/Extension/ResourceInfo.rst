.. _str: https://docs.python.org/2/library/stdtypes.html

.. _VI API 2.5: ../../vim/version.rst#vimversionversion2

.. _vim.KeyValue: ../../vim/KeyValue.rst

.. _vmodl.DynamicData: ../../vmodl/DynamicData.rst


vim.Extension.ResourceInfo
==========================
  This data object encapsulates the message resources for all locales.
:extends: vmodl.DynamicData_
:since: `VI API 2.5`_

Attributes:
    locale (`str`_):

    module (`str`_):

       Module for a resource type and other message or fault resources. Examples: "task" for task, "event" for event and "auth" for "privilege".
    data ([`vim.KeyValue`_]):

