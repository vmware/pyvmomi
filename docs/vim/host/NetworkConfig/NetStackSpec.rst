.. _str: https://docs.python.org/2/library/stdtypes.html

.. _vSphere API 5.5: ../../../vim/version.rst#vimversionversion9

.. _vmodl.DynamicData: ../../../vmodl/DynamicData.rst

.. _ConfigSpecOperation: ../../../vim/ConfigSpecOperation.rst

.. _vim.host.NetStackInstance: ../../../vim/host/NetStackInstance.rst


vim.host.NetworkConfig.NetStackSpec
===================================
  This data type describes Network Stack Spec
:extends: vmodl.DynamicData_
:since: `vSphere API 5.5`_

Attributes:
    netStackInstance (`vim.host.NetStackInstance`_):

       Network stack instance
    operation (`str`_, optional):

       Operation type, see `ConfigSpecOperation`_ for valid values. Only edit operation is supported currently.
