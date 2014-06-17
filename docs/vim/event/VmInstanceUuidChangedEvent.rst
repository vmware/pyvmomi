.. _str: https://docs.python.org/2/library/stdtypes.html

.. _vSphere API 4.0: ../../vim/version.rst#vimversionversion5

.. _vim.event.VmEvent: ../../vim/event/VmEvent.rst


vim.event.VmInstanceUuidChangedEvent
====================================
  This event records a change in a virtual machine's instance UUID.
:extends: vim.event.VmEvent_
:since: `vSphere API 4.0`_

Attributes:
    oldInstanceUuid (`str`_):

       The old instance UUID.
    newInstanceUuid (`str`_):

       The new instance UUID.
