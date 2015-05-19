.. _str: https://docs.python.org/2/library/stdtypes.html

.. _vSphere API 4.0: ../../vim/version.rst#vimversionversion5

.. _vim.event.DVPortgroupEvent: ../../vim/event/DVPortgroupEvent.rst


vim.event.DVPortgroupRenamedEvent
=================================
  Two distributed virtual portgroup was renamed.
:extends: vim.event.DVPortgroupEvent_
:since: `vSphere API 4.0`_

Attributes:
    oldName (`str`_):

       The old portgroup name.
    newName (`str`_):

       The new portgroup name.
