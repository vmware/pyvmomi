.. _int: https://docs.python.org/2/library/stdtypes.html

.. _str: https://docs.python.org/2/library/stdtypes.html

.. _bool: https://docs.python.org/2/library/stdtypes.html

.. _vSphere API 5.5: ../../../vim/version.rst#vimversionversion9

.. _vmodl.DynamicData: ../../../vmodl/DynamicData.rst


vim.host.RuntimeInfo.NetStackInstanceRuntimeInfo
================================================
  This data type describes network stack instance runtime info
:extends: vmodl.DynamicData_
:since: `vSphere API 5.5`_

Attributes:
    netStackInstanceKey (`str`_):

       Key of the instance
    state (`str`_, optional):

       State of the instance See State for valid values.
    vmknicKeys (`str`_, optional):

       The keys of vmknics that are using this stack
    maxNumberOfConnections (`int`_, optional):

       The maximum number of socket connections can be worked on this instance currently after booting up.
    currentIpV6Enabled (`bool`_, optional):

       If true then dual IPv4/IPv6 stack enabled else IPv4 only.
