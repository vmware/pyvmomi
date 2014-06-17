.. _str: https://docs.python.org/2/library/stdtypes.html

.. _vSphere API 4.1: ../../vim/version.rst#vimversionversion6

.. _vim.event.DvsEvent: ../../vim/event/DvsEvent.rst

.. _vim.dvs.DistributedVirtualPort.RuntimeInfo: ../../vim/dvs/DistributedVirtualPort/RuntimeInfo.rst


vim.event.DvsPortExitedPassthruEvent
====================================
  A port has exited passthrough mode on the distributed virtual switch.
:extends: vim.event.DvsEvent_
:since: `vSphere API 4.1`_

Attributes:
    portKey (`str`_):

       The port key.
    runtimeInfo (`vim.dvs.DistributedVirtualPort.RuntimeInfo`_, optional):

       The port runtime information.
