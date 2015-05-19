.. _int: https://docs.python.org/2/library/stdtypes.html

.. _long: https://docs.python.org/2/library/stdtypes.html

.. _vmodl.DynamicData: ../../../vmodl/DynamicData.rst


vim.host.DiskDimensions.Chs
===========================
  This data object type describes dimensions using the cylinder, head, sector (CHS) coordinate system. This coordinate system is generally needed for partitioning for legacy reasons. When defining partitions, many partitioning utilities do not function correctly when certain CHS constraints are not met.
:extends: vmodl.DynamicData_

Attributes:
    cylinder (`long`_):

       The number of cylinders.
    head (`int`_):

       The number of heads per cylinders.
    sector (`int`_):

       The number of sectors per head.
