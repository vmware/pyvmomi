.. _str: https://docs.python.org/2/library/stdtypes.html

.. _vSphere API 4.0: ../../vim/version.rst#vimversionversion5

.. _vim.event.DvsEvent: ../../vim/event/DvsEvent.rst

.. _vim.dvs.PortConnectee: ../../vim/dvs/PortConnectee.rst


vim.event.DvsPortConnectedEvent
===============================
  A port is connected in the distributed virtual switch.
:extends: vim.event.DvsEvent_
:since: `vSphere API 4.0`_

Attributes:
    portKey (`str`_):

       The port key.
    connectee (`vim.dvs.PortConnectee`_, optional):

       The port's connectee.
