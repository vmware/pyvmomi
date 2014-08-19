
vim.host.PhysicalNic.LinkSpeedDuplex
====================================
  The `PhysicalNicLinkInfo <vim/host/PhysicalNic/LinkSpeedDuplex.rst>`_ data object describes the link speed and the type of duplex communication. The link speed indicates the bit rate in megabits per second. The duplex boolean indicates if the link is capable of full-duplex or half-duplex communication.
:extends: vmodl.DynamicData_

Attributes:
    speedMb (`int <https://docs.python.org/2/library/stdtypes.html>`_):

       Bit rate on the link.
    duplex (`bool <https://docs.python.org/2/library/stdtypes.html>`_):

       Flag to indicate whether or not the link is capable of full-duplex ("true") or only half-duplex ("false").
