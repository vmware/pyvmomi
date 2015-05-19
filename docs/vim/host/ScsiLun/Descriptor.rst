.. _str: https://docs.python.org/2/library/stdtypes.html

.. _vSphere API 4.0: ../../../vim/version.rst#vimversionversion5

.. _vmodl.DynamicData: ../../../vmodl/DynamicData.rst


vim.host.ScsiLun.Descriptor
===========================
  A structure that encapsulates an identifier and its properties for the ScsiLun object.
:extends: vmodl.DynamicData_
:since: `vSphere API 4.0`_

Attributes:
    quality (`str`_):

       An indicator of the utility of the descriptor as an identifier that is stable, unique, and correlatable.See DescriptorQuality
    id (`str`_):

       The identifier represented as a string.
