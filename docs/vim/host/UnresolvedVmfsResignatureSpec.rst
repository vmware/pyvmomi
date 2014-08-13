.. _str: https://docs.python.org/2/library/stdtypes.html

.. _vSphere API 4.0: ../../vim/version.rst#vimversionversion5

.. _vmodl.DynamicData: ../../vmodl/DynamicData.rst


vim.host.UnresolvedVmfsResignatureSpec
======================================
  Specification to resignature an Unresolved VMFS volume.
:extends: vmodl.DynamicData_
:since: `vSphere API 4.0`_

Attributes:
    extentDevicePath ([`str`_]):

       List of device path each specifying VMFS extents.
