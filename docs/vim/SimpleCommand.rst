.. _str: https://docs.python.org/2/library/stdtypes.html

.. _vim.Task: ../vim/Task.rst

.. _VI API 2.5: ../vim/version.rst#vimversionversion2

.. _vim.SimpleCommand.Encoding: ../vim/SimpleCommand/Encoding.rst

.. _vim.ServiceManager.ServiceInfo: ../vim/ServiceManager/ServiceInfo.rst


vim.SimpleCommand
=================
  A managed object that wraps the execution of a single arbitrary command. The specific command executed is assumed to be known from the service name by the client invoking this command. This object presents a generic interface for such services.


:since: `VI API 2.5`_


Attributes
----------
    encodingType (`vim.SimpleCommand.Encoding`_):
       The encoding type used in the result.
    entity (`vim.ServiceManager.ServiceInfo`_):
       A description of the service.


Methods
-------


ExecuteSimpleCommand(arguments):
   The single function execution point for this simple command. The actual effects of this command depend upon the service handler registered for this instance.


  Privilege:
               Global.ServiceManagers



  Args:
    arguments (`str`_, optional):
       An arbitrary collection of arguments.




  Returns:
    `str`_:
         


