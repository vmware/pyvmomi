
vim.vm.ProfileRawData
=====================
  The extensible data object type encapsulates additional data specific to Virtual Machine and its devices.This data is provided by vSphere Extensions which are integral part of vSphere.The data is not persisted in Virtual Machine configuration file but is stored and managed by extensions.Storage Profile Based Management (SPBM) will be one of the consumers of this data structure. SPBM will provide detailed information about Virtual Machine storage requirements.
:extends: vmodl.DynamicData_
:since: `vSphere API 5.5 <vim/version.rst#vimversionversion9>`_

Attributes:
    extensionKey (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       vSphere Extension Identifier
    objectData (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Extension-specific additional data to be associated with Virtual machine and its devices.
