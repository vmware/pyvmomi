.. _str: https://docs.python.org/2/library/stdtypes.html

.. _VI API 2.5: ../../vim/version.rst#vimversionversion2

.. _vmodl.DynamicData: ../../vmodl/DynamicData.rst

.. _vim.ElementDescription: ../../vim/ElementDescription.rst

.. _HostSystemIdentificationInfoIdentifier: ../../vim/host/SystemIdentificationInfo/Identifier.rst


vim.host.SystemIdentificationInfo
=================================
  This data object describes system identifying information of the host. This information may be vendor specific.
:extends: vmodl.DynamicData_
:since: `VI API 2.5`_

Attributes:
    identifierValue (`str`_):

       The system identification information
    identifierType (`vim.ElementDescription`_):

       The description of the identifying information.See `HostSystemIdentificationInfoIdentifier`_ 
