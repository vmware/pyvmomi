
vim.host.CpuPackage
===================
  Information about a physical CPU package.
:extends: vmodl.DynamicData_

Attributes:
    index (`short <https://docs.python.org/2/library/stdtypes.html>`_):

       Package index, starting from zero.
    vendor (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       CPU vendor name, possible names currently are "Intel", "AMD", or "unknown".
    hz (`long <https://docs.python.org/2/library/stdtypes.html>`_):

       CPU speed in HZ.
    busHz (`long <https://docs.python.org/2/library/stdtypes.html>`_):

       Bus speed in HZ.
    description (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       String summary description of CPU (for display purposes).
    threadId ([`short <https://docs.python.org/2/library/stdtypes.html>`_]):

       The logical CPU threads on this package.
    cpuFeature ([`vim.host.CpuIdInfo <vim/host/CpuIdInfo.rst>`_], optional):

       The CPU feature bit on this particular CPU. This is independent of the product and licensing capabilities.
