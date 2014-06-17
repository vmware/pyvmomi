.. _str: https://docs.python.org/2/library/stdtypes.html

.. _VI API 2.5: ../../../vim/version.rst#vimversionversion2

.. _vmodl.DynamicData: ../../../vmodl/DynamicData.rst

.. _vim.ElementDescription: ../../../vim/ElementDescription.rst

.. _HostHardwareElementStatus: ../../../vim/host/HardwareStatusInfo/Status.rst


vim.host.HardwareStatusInfo.HardwareElementInfo
===============================================
  Data object describing the operational status of a physical element.
:extends: vmodl.DynamicData_
:since: `VI API 2.5`_

Attributes:
    name (`str`_):

       The name of the physical element
    status (`vim.ElementDescription`_):

       The operational status of the physical element. The status is one of the values specified in HostHardwareElementStatus.See `HostHardwareElementStatus`_ 
