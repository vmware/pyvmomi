.. _str: https://docs.python.org/2/library/stdtypes.html

.. _vim.vm.Message: ../../vim/vm/Message.rst

.. _vSphere API 4.0: ../../vim/version.rst#vimversionversion5

.. _vim.event.VmEvent: ../../vim/event/VmEvent.rst


vim.event.VmMessageWarningEvent
===============================
  This event records when a warning message (consisting of a collection of "observations") is thrown by the virtual machine. This is a generic event for such messages.
:extends: vim.event.VmEvent_
:since: `vSphere API 4.0`_

Attributes:
    message (`str`_):

       A raw message returned by the virtualization platform.
    messageInfo (`vim.vm.Message`_, optional):

