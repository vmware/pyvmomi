
vim.host.NetworkPolicy.SecurityPolicy
=====================================
  This data object type describes security policy governing ports.
:extends: vmodl.DynamicData_

Attributes:
    allowPromiscuous (`bool <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       The flag to indicate whether or not all traffic is seen on the port.
    macChanges (`bool <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       The flag to indicate whether or not the Media Access Control (MAC) address can be changed.
    forgedTransmits (`bool <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       The flag to indicate whether or not the virtual network adapter should be allowed to send network traffic with a different MAC address than that of the virtual network adapter.
