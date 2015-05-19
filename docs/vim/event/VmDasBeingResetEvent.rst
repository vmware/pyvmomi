.. _str: https://docs.python.org/2/library/stdtypes.html

.. _vSphere API 4.0: ../../vim/version.rst#vimversionversion5

.. _vim.event.VmEvent: ../../vim/event/VmEvent.rst


vim.event.VmDasBeingResetEvent
==============================
  This event records when a virtual machine is reset by HA VM Health Monitoring on hosts that do not support the create screenshot api or if the createscreenshot api fails.
:extends: vim.event.VmEvent_
:since: `vSphere API 4.0`_

Attributes:
    reason (`str`_, optional):

       The reason why this vm is being reset
