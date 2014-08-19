
vim.vm.guest.ProcessManager.ProgramSpec
=======================================
  This describes the arguments to `StartProgramInGuest <vim/vm/guest/ProcessManager.rst#startProgram>`_ .
:extends: vmodl.DynamicData_
:since: `vSphere API 5.0 <vim/version.rst#vimversionversion7>`_

Attributes:
    programPath (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       The absolute path to the program to start.For Linux guest operating systems, /bin/bash is used to start the program.For Solaris guest operating systems, /bin/bash is used to start the program if it exists. Otherwise /bin/sh is used. If /bin/sh is used, then the process ID returned by `StartProgramInGuest <vim/vm/guest/ProcessManager.rst#startProgram>`_ will be that of the shell used to start the program, rather than the program itself, due to the differences in how /bin/sh and /bin/bash work. This PID will still be usable for watching the process with `ListProcessesInGuest <vim/vm/guest/ProcessManager.rst#listProcesses>`_ to find its exit code and elapsed time.
    arguments (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       The arguments to the program. In Linux and Solaris guest operating systems, the program will be executed by a guest shell. This allows stdio redirection, but may also require that characters which must be escaped to the shell also be escaped on the command line provided.For Windows guest operating systems, prefixing the command with "cmd /c" can provide stdio redirection.
    workingDirectory (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       The absolute path of the working directory for the program to be run. VMware recommends explicitly setting the working directory for the program to be run. If this value is unset or is an empty string, the behavior depends on the guest operating system. For Linux guest operating systems, if this value is unset or is an empty string, the working directory will be the home directory of the user associated with the guest authentication. For other guest operating systems, if this value is unset, the behavior is unspecified.
    envVariables ([`str <https://docs.python.org/2/library/stdtypes.html>`_], optional):

       An array of environment variables, specified in the guest OS notation (eg PATH=c:\bin;c:\windows\system32 or LD_LIBRARY_PATH=/usr/lib:/lib), to be set for the program being run. Note that these are not additions to the default environment variables; they define the complete set available to the program. If none are specified the values are guest dependent.
