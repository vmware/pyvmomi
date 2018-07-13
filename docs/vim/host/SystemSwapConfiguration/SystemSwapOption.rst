.. _int: https://docs.python.org/2/library/stdtypes.html

.. _vSphere API 5.1: ../../../vim/version.rst#vimversionversion8

.. _vmodl.DynamicData: ../../../vmodl/DynamicData.rst

.. _SystemSwapConfiguration.option: ../../../vim/host/SystemSwapConfiguration.rst#option


vim.host.SystemSwapConfiguration.SystemSwapOption
=================================================
  Base class for all system swap options. This class is not supposed to be used directly.These values are to be used in a `SystemSwapConfiguration.option`_ array.
:extends: vmodl.DynamicData_
:since: `vSphere API 5.1`_

Attributes:
    key (`int`_):

       Specifies the order the options are preferred among each other. The lower the value the more important.
