
vim.host.SystemSwapConfiguration.SystemSwapOption
=================================================
  Base class for all system swap options. This class is not supposed to be used directly.These values are to be used in a `SystemSwapConfiguration.option <vim/host/SystemSwapConfiguration.rst#option>`_ array.
:extends: vmodl.DynamicData_
:since: `vSphere API 5.1 <vim/version.rst#vimversionversion8>`_

Attributes:
    key (`int <https://docs.python.org/2/library/stdtypes.html>`_):

       Specifies the order the options are prefered among each other. The lower the value the more important.
