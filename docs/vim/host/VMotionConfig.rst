
vim.host.VMotionConfig
======================
  This data object configuring VMotion on the host. The runtime information is available from the `VMotionInfo <vim/host/VMotionInfo.rst>`_ data object type.
:extends: vmodl.DynamicData_

Attributes:
    vmotionNicKey (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Key of the VirtualNic used for VMotion.
    enabled (`bool <https://docs.python.org/2/library/stdtypes.html>`_):

       Flag to indicate whether or not VMotion is enabled.
