.. _str: https://docs.python.org/2/library/stdtypes.html

.. _vmodl.DynamicData: ../../../vmodl/DynamicData.rst

.. _UpdateNetworkConfig: ../../../vim/host/NetworkSystem.rst#updateNetworkConfig


vim.host.NetworkConfig.Result
=============================
  The result returned by updateNetworkConfig call.See `UpdateNetworkConfig`_ 
:extends: vmodl.DynamicData_

Attributes:
    vnicDevice ([`str`_], optional):

       Virtual network adapter keys.
    consoleVnicDevice ([`str`_], optional):

       Service console virtual network adapter keys.
