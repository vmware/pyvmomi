.. _str: https://docs.python.org/2/library/stdtypes.html

.. _vSphere API 4.0: ../../vim/version.rst#vimversionversion5

.. _vim.event.DvsEvent: ../../vim/event/DvsEvent.rst

.. _vim.dvs.DistributedVirtualPort.RuntimeInfo: ../../vim/dvs/DistributedVirtualPort/RuntimeInfo.rst


vim.event.DvsPortUnblockedEvent
===============================
  A port is blocked in the distributed virtual switch.
:extends: vim.event.DvsEvent_
:since: `vSphere API 4.0`_

Attributes:
    portKey (`str`_):

       The port key.
    runtimeInfo (`vim.dvs.DistributedVirtualPort.RuntimeInfo`_, optional):

       The port runtime information.
