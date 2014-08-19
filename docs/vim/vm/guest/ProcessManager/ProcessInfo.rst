
vim.vm.guest.ProcessManager.ProcessInfo
=======================================
  
:extends: vmodl.DynamicData_
:since: `vSphere API 5.0 <vim/version.rst#vimversionversion7>`_

Attributes:
    name (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       The process name
    pid (`long <https://docs.python.org/2/library/stdtypes.html>`_):

       The process ID
    owner (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       The process owner
    cmdLine (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       The full command line
    startTime (`datetime <https://docs.python.org/2/library/stdtypes.html>`_):

       The start time of the process
    endTime (`datetime <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       If the process was started using `StartProgramInGuest <vim/vm/guest/ProcessManager.rst#startProgram>`_ then the process completion time will be available if queried within 5 minutes after it completes.
    exitCode (`int <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       If the process was started using `StartProgramInGuest <vim/vm/guest/ProcessManager.rst#startProgram>`_ then the process exit code will be available if queried within 5 minutes after it completes.
