.. _vim.vm.GuestInfo: ../../../vim/vm/GuestInfo.rst

.. _vim.vm.GuestInfo.AppStateType: ../../../vim/vm/GuestInfo/AppStateType.rst

vim.vm.GuestInfo.AppStateType
=============================
  Application state type.
  :contained by: `vim.vm.GuestInfo`_

  :type: `vim.vm.GuestInfo.AppStateType`_

  :name: appStateNeedReset

values:
--------

appStateOk
   The guest's application agent declared its state as normal and doesn't require any action

none
   The application state wasn't set from the guest by the application agent. This is the default.

appStateNeedReset
   Guest's application agent asks for immediate reset
