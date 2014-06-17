.. _vSphere API 4.1: ../vim/version.rst#vimversionversion6

.. _vmodl.DynamicData: ../vmodl/DynamicData.rst

.. _ResourceConfigSpec: ../vim/ResourceConfigSpec.rst

.. _ResourceAllocationInfo: ../vim/ResourceAllocationInfo.rst

.. _vim.ResourceAllocationOption: ../vim/ResourceAllocationOption.rst


vim.ResourceConfigOption
========================
  This data object type is a default value and value range specification for `ResourceConfigSpec`_ object.
:extends: vmodl.DynamicData_
:since: `vSphere API 4.1`_

Attributes:
    cpuAllocationOption (`vim.ResourceAllocationOption`_):

       Resource allocation options for CPU.See `ResourceAllocationInfo`_ 
    memoryAllocationOption (`vim.ResourceAllocationOption`_):

       Resource allocation options for memory.See `ResourceAllocationInfo`_ 
