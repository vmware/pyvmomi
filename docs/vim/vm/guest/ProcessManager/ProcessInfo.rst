.. _int: https://docs.python.org/2/library/stdtypes.html

.. _str: https://docs.python.org/2/library/stdtypes.html

.. _long: https://docs.python.org/2/library/stdtypes.html

.. _datetime: https://docs.python.org/2/library/stdtypes.html

.. _vSphere API 5.0: ../../../../vim/version.rst#vimversionversion7

.. _vmodl.DynamicData: ../../../../vmodl/DynamicData.rst

.. _StartProgramInGuest: ../../../../vim/vm/guest/ProcessManager.rst#startProgram


vim.vm.guest.ProcessManager.ProcessInfo
=======================================
  
:extends: vmodl.DynamicData_
:since: `vSphere API 5.0`_

Attributes:
    name (`str`_):

       The process name
    pid (`long`_):

       The process ID
    owner (`str`_):

       The process owner
    cmdLine (`str`_):

       The full command line
    startTime (`datetime`_):

       The start time of the process
    endTime (`datetime`_, optional):

       If the process was started using `StartProgramInGuest`_ then the process completion time will be available if queried within 5 minutes after it completes.
    exitCode (`int`_, optional):

       If the process was started using `StartProgramInGuest`_ then the process exit code will be available if queried within 5 minutes after it completes.
