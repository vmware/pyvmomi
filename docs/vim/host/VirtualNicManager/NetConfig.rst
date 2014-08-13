.. _str: https://docs.python.org/2/library/stdtypes.html

.. _vnic: ../../../vim/host/NetworkInfo.rst#vnic

.. _bool: https://docs.python.org/2/library/stdtypes.html

.. _vSphere API 4.0: ../../../vim/version.rst#vimversionversion5

.. _vmodl.DynamicData: ../../../vmodl/DynamicData.rst

.. _vim.host.VirtualNic: ../../../vim/host/VirtualNic.rst


vim.host.VirtualNicManager.NetConfig
====================================
  The NetConfig data object type contains the networking configuration.
:extends: vmodl.DynamicData_
:since: `vSphere API 4.0`_

Attributes:
    nicType (`str`_):

       The NicType of this NetConfig.
    multiSelectAllowed (`bool`_):

       Whether multiple nics can be selected for this nicType.
    candidateVnic ([`vim.host.VirtualNic`_], optional):

       List of VirtualNic objects that may be used. This will be a subset of the list of VirtualNics in `vnic`_ .
    selectedVnic ([`vim.host.VirtualNic`_], optional):

       List of VirtualNic objects that are selected for use.
