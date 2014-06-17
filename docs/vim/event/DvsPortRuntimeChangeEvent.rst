.. _str: https://docs.python.org/2/library/stdtypes.html

.. _vSphere API 5.1: ../../vim/version.rst#vimversionversion8

.. _vim.event.DvsEvent: ../../vim/event/DvsEvent.rst

.. _vim.dvs.DistributedVirtualPort.RuntimeInfo: ../../vim/dvs/DistributedVirtualPort/RuntimeInfo.rst


vim.event.DvsPortRuntimeChangeEvent
===================================
  A port of which runtime information is changed in the vNetwork Distributed Switch.
:extends: vim.event.DvsEvent_
:since: `vSphere API 5.1`_

Attributes:
    portKey (`str`_):

       The port key.
    runtimeInfo (`vim.dvs.DistributedVirtualPort.RuntimeInfo`_):

       The new port runtime information.
