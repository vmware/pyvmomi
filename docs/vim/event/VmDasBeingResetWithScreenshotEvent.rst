.. _str: https://docs.python.org/2/library/stdtypes.html

.. _vSphere API 4.0: ../../vim/version.rst#vimversionversion5

.. _vim.event.VmDasBeingResetEvent: ../../vim/event/VmDasBeingResetEvent.rst


vim.event.VmDasBeingResetWithScreenshotEvent
============================================
  This event records when a virtual machine is reset by HA VM Health Monitoring on hosts that support the create screenshot api
:extends: vim.event.VmDasBeingResetEvent_
:since: `vSphere API 4.0`_

Attributes:
    screenshotFilePath (`str`_):

       The datastore path of the screenshot taken before resetting.
