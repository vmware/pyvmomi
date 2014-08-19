
vim.Extension.ResourceInfo
==========================
  This data object encapsulates the message resources for all locales.
:extends: vmodl.DynamicData_
:since: `VI API 2.5 <vim/version.rst#vimversionversion2>`_

Attributes:
    locale (`str <https://docs.python.org/2/library/stdtypes.html>`_):

    module (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       Module for a resource type and other message or fault resources. Examples: "task" for task, "event" for event and "auth" for "privilege".
    data ([`vim.KeyValue <vim/KeyValue.rst>`_]):

