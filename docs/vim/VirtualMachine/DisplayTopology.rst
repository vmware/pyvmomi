.. _int: https://docs.python.org/2/library/stdtypes.html

.. _vSphere API 4.0: ../../vim/version.rst#vimversionversion4

.. _vmodl.DynamicData: ../../vmodl/DynamicData.rst


vim.VirtualMachine.DisplayTopology
==================================
  This data object defines a two-dimensional, rectangular display area.
:extends: vmodl.DynamicData_
:since: `vSphere API 4.0`_

Attributes:
    x (`int`_):

       The x co-ordinate defining the start of the display rectangle.
    y (`int`_):

       The y co-ordinate defining the start of the display rectangle.
    width (`int`_):

       The width of the display rectangle.
    height (`int`_):

       The height of the display rectangle.
