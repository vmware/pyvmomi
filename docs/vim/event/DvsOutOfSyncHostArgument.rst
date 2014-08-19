
vim.event.DvsOutOfSyncHostArgument
==================================
  The host on which the DVS configuration is different from that of Virtual Center server.
:extends: vmodl.DynamicData_
:since: `vSphere API 4.0 <vim/version.rst#vimversionversion5>`_

Attributes:
    outOfSyncHost (`vim.event.HostEventArgument <vim/event/HostEventArgument.rst>`_):

       The host.
    configParamters ([`str <https://docs.python.org/2/library/stdtypes.html>`_]):

       The DVS configuration parameters that are different between Virtual Center server and the host.
