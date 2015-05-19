.. _bool: https://docs.python.org/2/library/stdtypes.html

.. _vSphere API 5.0: ../../../../vim/version.rst#vimversionversion7

.. _StartProgramInGuest: ../../../../vim/vm/guest/ProcessManager.rst#startProgram

.. _vim.vm.guest.ProcessManager.ProgramSpec: ../../../../vim/vm/guest/ProcessManager/ProgramSpec.rst


vim.vm.guest.ProcessManager.WindowsProgramSpec
==============================================
  This describes the arguments to `StartProgramInGuest`_ that apply only for Windows guests.
:extends: vim.vm.guest.ProcessManager.ProgramSpec_
:since: `vSphere API 5.0`_

Attributes:
    startMinimized (`bool`_):

       Makes any program window start minimized.
