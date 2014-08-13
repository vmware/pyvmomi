.. _vnic: ../../../vim/host/NetworkInfo.rst#vnic

.. _vmodl.DynamicData: ../../../vmodl/DynamicData.rst

.. _vim.host.VirtualNic: ../../../vim/host/VirtualNic.rst


vim.host.VMotionSystem.NetConfig
================================
  The NetConfig data object type contains the networking configuration for VMotion operations.
:extends: vmodl.DynamicData_

Attributes:
    candidateVnic ([`vim.host.VirtualNic`_], optional):

       List of VirtualNic objects that may be used for VMotion. This will be a subset of the list of VirtualNics in `vnic`_ .
    selectedVnic (`vim.host.VirtualNic`_, optional):

       VirtualNic that is selected for use in VMotion operations.
