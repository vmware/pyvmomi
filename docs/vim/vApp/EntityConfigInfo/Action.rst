vim.vApp.EntityConfigInfo.Action
================================
  :contained by: `vim.vApp.EntityConfigInfo <vim/vApp/EntityConfigInfo.rst>`_

  :type: `vim.vApp.EntityConfigInfo.Action <vim/vApp/EntityConfigInfo/Action.rst>`_

  :name: suspend

values:
--------

suspend
   This virtual machine is suspended when it is next in the auto-stop order.

none
   No action is taken for this virtual machine. This virtual machine is not a part of the auto-start sequence. This can be used for both auto-start and auto-start settings.

powerOn
   This virtual machine is powered on when it is next in the auto-start order.

powerOff
   This virtual machine is powered off when it is next in the auto-stop order. This is the default stopAction.

guestShutdown
   The guest operating system for a virtual machine is shut down when that virtual machine in next in the auto-stop order.
