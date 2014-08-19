
vim.event.VmMessageWarningEvent
===============================
  This event records when a warning message (consisting of a collection of "observations") is thrown by the virtual machine. This is a generic event for such messages.
:extends: vim.event.VmEvent_
:since: `vSphere API 4.0 <vim/version.rst#vimversionversion5>`_

Attributes:
    message (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       A raw message returned by the virtualization platform.
    messageInfo ([`vim.vm.Message <vim/vm/Message.rst>`_], optional):

