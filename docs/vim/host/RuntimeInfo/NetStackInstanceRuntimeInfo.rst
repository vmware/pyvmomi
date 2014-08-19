
vim.host.RuntimeInfo.NetStackInstanceRuntimeInfo
================================================
  This data type describes network stack instance runtime info
:extends: vmodl.DynamicData_
:since: `vSphere API 5.5 <vim/version.rst#vimversionversion9>`_

Attributes:
    netStackInstanceKey (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       Key of the instance
    state (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       State of the instance See State for valid values.
    vmknicKeys ([`str <https://docs.python.org/2/library/stdtypes.html>`_], optional):

       The keys of vmknics that are using this stack
    maxNumberOfConnections (`int <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       The maximum number of socket connections can be worked on this instance currently after booting up.
    currentIpV6Enabled (`bool <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       If true then dual IPv4/IPv6 stack enabled else IPv4 only.
