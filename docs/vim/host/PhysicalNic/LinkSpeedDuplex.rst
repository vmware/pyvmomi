.. _int: https://docs.python.org/2/library/stdtypes.html

.. _bool: https://docs.python.org/2/library/stdtypes.html

.. _vmodl.DynamicData: ../../../vmodl/DynamicData.rst

.. _PhysicalNicLinkInfo: ../../../vim/host/PhysicalNic/LinkSpeedDuplex.rst


vim.host.PhysicalNic.LinkSpeedDuplex
====================================
  The `PhysicalNicLinkInfo`_ data object describes the link speed and the type of duplex communication. The link speed indicates the bit rate in megabits per second. The duplex boolean indicates if the link is capable of full-duplex or half-duplex communication.
:extends: vmodl.DynamicData_

Attributes:
    speedMb (`int`_):

       Bit rate on the link.
    duplex (`bool`_):

       Flag to indicate whether or not the link is capable of full-duplex ("true") or only half-duplex ("false").
