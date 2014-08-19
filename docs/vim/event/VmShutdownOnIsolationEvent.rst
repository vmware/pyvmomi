
vim.event.VmShutdownOnIsolationEvent
====================================
  This event records when a virtual machine has been shut down on an isolated host in a HA cluster.
:extends: vim.event.VmPoweredOffEvent_
:since: `vSphere API 4.0 <vim/version.rst#vimversionversion5>`_

Attributes:
    isolatedHost (`vim.event.HostEventArgument <vim/event/HostEventArgument.rst>`_):

       The isolated host on which a virtual machine was shutdown.
    shutdownResult (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Indicates if the shutdown was successful. If the shutdown failed, the virtual machine was powered off. see Operation
