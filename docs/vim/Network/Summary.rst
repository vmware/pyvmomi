
vim.Network.Summary
===================
  General information about a network.
:extends: vmodl.DynamicData_

Attributes:
    network (`vim.Network <vim/Network.rst>`_, optional):

       Reference to the associated managed object.
    name (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       Name of the network.
    accessible (`bool <https://docs.python.org/2/library/stdtypes.html>`_):

       At least one host is configured to provide this network.
    ipPoolName (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       Name of the associated IP pool. Empty if the network is not associated with an IP pool.
    ipPoolId (`int <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Identifier of the associated IP pool. Zero if the network is not associated with an IP pool.
