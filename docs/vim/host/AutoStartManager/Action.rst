vim.host.AutoStartManager.Action
================================
  :contained by: `vim.host.AutoStartManager <vim/host/AutoStartManager.rst>`_

  :type: `vim.host.AutoStartManager.Action <vim/host/AutoStartManager/Action.rst>`_

  :name: suspend

values:
--------

none
   No action is taken for this virtual machine. This virtual machine is not a part of the auto-start sequence. This can be used for both auto-start and auto-start settings.

suspend
   This virtual machine is suspended when it is next in the auto-stop order.

systemDefault
   The default system action is taken for this virtual machine when it is next in the auto-start order. This can be used for both auto-start and auto-start settings.

powerOff
   This virtual machine is powered off when it is next in the auto-stop order. This is the default stopAction.

guestShutdown
   The guest operating system for a virtual machine is shut down when that virtual machine in next in the auto-stop order.

powerOn
   This virtual machine is powered on when it is next in the auto-start order.
