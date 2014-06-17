.. _str: https://docs.python.org/2/library/stdtypes.html

.. _vim.vm.Message: ../../vim/vm/Message.rst

.. _vim.event.VmEvent: ../../vim/event/VmEvent.rst


vim.event.VmMessageEvent
========================
  This event records when an informational message (consisting of a collection of "observations") is thrown by the virtual machine. This is a generic event for such messages.
:extends: vim.event.VmEvent_

Attributes:
    message (`str`_):

       A raw message returned by the virtualization platform.
    messageInfo (`vim.vm.Message`_, optional):

