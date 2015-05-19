.. _int: https://docs.python.org/2/library/stdtypes.html

.. _str: https://docs.python.org/2/library/stdtypes.html

.. _bool: https://docs.python.org/2/library/stdtypes.html

.. _vim.Network: ../../vim/Network.rst

.. _vmodl.DynamicData: ../../vmodl/DynamicData.rst


vim.Network.Summary
===================
  General information about a network.
:extends: vmodl.DynamicData_

Attributes:
    network (`vim.Network`_, optional):

       Reference to the associated managed object.
    name (`str`_):

       Name of the network.
    accessible (`bool`_):

       At least one host is configured to provide this network.
    ipPoolName (`str`_):

       Name of the associated IP pool. Empty if the network is not associated with an IP pool.
    ipPoolId (`int`_, optional):

       Identifier of the associated IP pool. Zero if the network is not associated with an IP pool.
