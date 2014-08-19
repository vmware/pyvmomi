
vim.DiagnosticManager
=====================
  Provides an interface to get low-level debugging logs or diagnostic bundles for a server. For VirtualCenter, this includes the log files for the server daemon. For an ESX Server host, this includes detailed log files for the VMkernel.




Attributes
----------


Methods
-------


QueryDescriptions(host):
   Returns a list of diagnostic files for a given system.


  Privilege:
               Global.Diagnostics



  Args:
    host (`vim.HostSystem <vim/HostSystem.rst>`_, optional):
       Specifies the host. If not specified, then it defaults to the server itself. For example, if called on VirtualCenter, then the value defaults to VirtualCenter logs. When called on an ESX server host, the host should not be specified.




  Returns:
    [`vim.DiagnosticManager.LogDescriptor <vim/DiagnosticManager/LogDescriptor.rst>`_]:
         

  Raises:

    `vmodl.fault.InvalidArgument <vmodl/fault/InvalidArgument.rst>`_: 
       if the host does not exist or is specified on a host.


BrowseDiagnosticLog(host, key, start, lines):
   Returns part of a log file. Log entries are always returned chronologically, typically with the newest event last.


  Privilege:
               Global.Diagnostics



  Args:
    host (`vim.HostSystem <vim/HostSystem.rst>`_, optional):
       Specifies the host. If not specified, then it defaults to the default server. For example, if called on VirtualCenter, then the value defaults to VirtualCenter logs.


    key (`str <https://docs.python.org/2/library/stdtypes.html>`_):
       A string key specifying the key for the log file to browse. Keys can be obtained using the queryDescriptions method.


    start (`int <https://docs.python.org/2/library/stdtypes.html>`_, optional):
       The line number for the first entry to be returned. If the parameter is not specified, then the operation returns with lines starting from the top of the log.


    lines (`int <https://docs.python.org/2/library/stdtypes.html>`_, optional):
       The number of lines to return. If not specified, then all lines are returned from the start value to the end of the file.




  Returns:
    `vim.DiagnosticManager.LogHeader <vim/DiagnosticManager/LogHeader.rst>`_:
         A LogHeader that includes the log lines. Sometimes fewer log lines are returned than were requested. For example, fewer lines are returned than expected if the client requests lines that do not exist or if the server limits the number of lines that it returns. If zero lines are returned, then the end of the log file may have been reached.

  Raises:

    `vim.fault.CannotAccessFile <vim/fault/CannotAccessFile.rst>`_: 
       if the key refers to a file that cannot be accessed at the present time.

    `vmodl.fault.InvalidArgument <vmodl/fault/InvalidArgument.rst>`_: 
       if the key refers to a nonexistent log file or the log file is not of type "plain".


GenerateLogBundles(includeDefault, host):
   Instructs the server to generate diagnostic bundles. A diagnostic bundle includes log files and other configuration information that can be used to investigate potential server issues. Virtual machine and guest operation system state is excluded from diagnostic bundles.


  Privilege:
               Global.Diagnostics



  Args:
    includeDefault (`bool <https://docs.python.org/2/library/stdtypes.html>`_):
       Specifies if the bundle should include the default server. If called on a VirtualCenter server, then this means the VirtualCenter diagnostic files. If called directly on a host, then includeDefault must be set to true.


    host (`vim.HostSystem <vim/HostSystem.rst>`_, optional):
       Lists hosts that are included. This is only used when called on VirtualCenter. If called directly on a host, then this parameter must be empty.




  Returns:
     `vim.Task <vim/Task.rst>`_:
         a list of BundleInfo objects for each diagnostic bundle that has been generated. The list may include no information from some requested hosts. For example, hosts that are disconnected or not responding are ignored.

  Raises:

    `vim.fault.LogBundlingFailed <vim/fault/LogBundlingFailed.rst>`_: 
       if generation of support bundle failed.

    `vim.fault.TaskInProgress <vim/fault/TaskInProgress.rst>`_: 
       if there is a pending request to generate a support bundle.The caller can download the bundles using an HTTP GET operation for each returned URL. Bundles are usually available for at least 24 hours, but the caller should not assume that the returned URLs are valid indefinitely. Servers often automatically delete generated diagnostic bundles after some given period of time.


