.. _str: https://docs.python.org/2/library/stdtypes.html

.. _vSphere API 4.0: ../../vim/version.rst#vimversionversion5

.. _vim.event.DvsEvent: ../../vim/event/DvsEvent.rst


vim.event.DvsPortLeavePortgroupEvent
====================================
  A port was moved out of the distributed virtual portgroup.
:extends: vim.event.DvsEvent_
:since: `vSphere API 4.0`_

Attributes:
    portKey (`str`_):

       The port key.
    portgroupKey (`str`_):

       The portgroup key.
    portgroupName (`str`_):

       The portgroup name.
