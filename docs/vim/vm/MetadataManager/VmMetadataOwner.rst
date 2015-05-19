.. _str: https://docs.python.org/2/library/stdtypes.html

.. _vSphere API 5.5: ../../../vim/version.rst#vimversionversion9

.. _vmodl.DynamicData: ../../../vmodl/DynamicData.rst


vim.vm.MetadataManager.VmMetadataOwner
======================================
  VmMetadataOwner defines the namespace for an owner
:extends: vmodl.DynamicData_
:since: `vSphere API 5.5`_

Attributes:
    name (`str`_):

       A string representing the owner. Valid values come from Owner for vSAN datastores. Otherwise, the owner field is interpreted by the implementation based on the datastore type.
