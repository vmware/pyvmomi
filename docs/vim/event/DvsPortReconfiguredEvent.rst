.. _str: https://docs.python.org/2/library/stdtypes.html

.. _vSphere API 4.0: ../../vim/version.rst#vimversionversion5

.. _vim.event.DvsEvent: ../../vim/event/DvsEvent.rst


vim.event.DvsPortReconfiguredEvent
==================================
  Existing ports are reconfigured in the distributed virtual switch.
:extends: vim.event.DvsEvent_
:since: `vSphere API 4.0`_

Attributes:
    portKey (`str`_):

       The key of the ports that are reconfigured.
