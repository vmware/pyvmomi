
vim.host.SystemIdentificationInfo
=================================
  This data object describes system identifying information of the host. This information may be vendor specific.
:extends: vmodl.DynamicData_
:since: `VI API 2.5 <vim/version.rst#vimversionversion2>`_

Attributes:
    identifierValue (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       The system identification information
    identifierType (`vim.ElementDescription <vim/ElementDescription.rst>`_):

       The description of the identifying information.See `HostSystemIdentificationInfoIdentifier <vim/host/SystemIdentificationInfo/Identifier.rst>`_ 
