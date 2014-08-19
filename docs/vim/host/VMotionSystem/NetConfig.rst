
vim.host.VMotionSystem.NetConfig
================================
  The NetConfig data object type contains the networking configuration for VMotion operations.
:extends: vmodl.DynamicData_

Attributes:
    candidateVnic ([`vim.host.VirtualNic <vim/host/VirtualNic.rst>`_], optional):

       List of VirtualNic objects that may be used for VMotion. This will be a subset of the list of VirtualNics in `vnic <vim/host/NetworkInfo.rst#vnic>`_ .
    selectedVnic (`vim.host.VirtualNic <vim/host/VirtualNic.rst>`_, optional):

       VirtualNic that is selected for use in VMotion operations.
