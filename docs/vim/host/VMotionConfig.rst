.. _str: https://docs.python.org/2/library/stdtypes.html

.. _bool: https://docs.python.org/2/library/stdtypes.html

.. _VMotionInfo: ../../vim/host/VMotionInfo.rst

.. _vmodl.DynamicData: ../../vmodl/DynamicData.rst


vim.host.VMotionConfig
======================
  This data object configuring VMotion on the host. The runtime information is available from the `VMotionInfo`_ data object type.
:extends: vmodl.DynamicData_

Attributes:
    vmotionNicKey (`str`_, optional):

       Key of the VirtualNic used for VMotion.
    enabled (`bool`_):

       Flag to indicate whether or not VMotion is enabled.
