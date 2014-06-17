.. _str: https://docs.python.org/2/library/stdtypes.html

.. _vSphere API 4.0: ../../vim/version.rst#vimversionversion5

.. _vim.event.DvsEvent: ../../vim/event/DvsEvent.rst


vim.event.DvsRenamedEvent
=========================
  A distributed virtual switch was renamed.
:extends: vim.event.DvsEvent_
:since: `vSphere API 4.0`_

Attributes:
    oldName (`str`_):

       The old DistributedVirtualSwitch name.
    newName (`str`_):

       The new DistributedVirtualSwitch name.
