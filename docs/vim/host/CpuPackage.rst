.. _str: https://docs.python.org/2/library/stdtypes.html

.. _long: https://docs.python.org/2/library/stdtypes.html

.. _short: https://docs.python.org/2/library/stdtypes.html

.. _vmodl.DynamicData: ../../vmodl/DynamicData.rst

.. _vim.host.CpuIdInfo: ../../vim/host/CpuIdInfo.rst


vim.host.CpuPackage
===================
  Information about a physical CPU package.
:extends: vmodl.DynamicData_

Attributes:
    index (`short`_):

       Package index, starting from zero.
    vendor (`str`_):

       CPU vendor name, possible names currently are "Intel", "AMD", or "unknown".
    hz (`long`_):

       CPU speed in HZ.
    busHz (`long`_):

       Bus speed in HZ.
    description (`str`_):

       String summary description of CPU (for display purposes).
    threadId (`short`_):

       The logical CPU threads on this package.
    cpuFeature (`vim.host.CpuIdInfo`_, optional):

       The CPU feature bit on this particular CPU. This is independent of the product and licensing capabilities.
