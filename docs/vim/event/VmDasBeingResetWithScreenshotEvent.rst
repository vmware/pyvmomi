
vim.event.VmDasBeingResetWithScreenshotEvent
============================================
  This event records when a virtual machine is reset by HA VM Health Monitoring on hosts that support the create screenshot api
:extends: vim.event.VmDasBeingResetEvent_
:since: `vSphere API 4.0 <vim/version.rst#vimversionversion5>`_

Attributes:
    screenshotFilePath (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       The datastore path of the screenshot taken before resetting.
