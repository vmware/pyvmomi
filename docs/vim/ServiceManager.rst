.. _str: https://docs.python.org/2/library/stdtypes.html

.. _vim.Task: ../vim/Task.rst

.. _VI API 2.5: ../vim/version.rst#vimversionversion2

.. _vmodl.fault.InvalidArgument: ../vmodl/fault/InvalidArgument.rst

.. _vim.ServiceManager.ServiceInfo: ../vim/ServiceManager/ServiceInfo.rst


vim.ServiceManager
==================
  The ServiceManager managed object is a singleton object that is used to present services that are optional and not necessarily formally defined. This directory makes available a list of such services and provides an easy way to locate them. The service being represented can take arbitrary form here and is thus represented by a generic ManagedObject. The expectation is that the client side is knowledgeable of the instance type of the specific service it is interested in using.


:since: `VI API 2.5`_


Attributes
----------
    service (`vim.ServiceManager.ServiceInfo`_):
      privilege: Global.ServiceManagers
       The full list of services available in this directory.


Methods
-------


QueryServiceList(serviceName, location):
   A query interface that returns a list of services that match certain criteria. Besides a basic service name entry, an arbitrary list of matching locations can also be specified. The location array is assumed to be a list of AND expressions, ie, all locations must match for an entry to be considered a match. Regular expressions are not allowed in the query service.


  Privilege:
               Global.ServiceManagers



  Args:
    serviceName (`str`_, optional):
       The name of the service to be located.


    location (`str`_, optional):
       The list of location information that needs to match for a service to be considered a match.




  Returns:
    `vim.ServiceManager.ServiceInfo`_:
         

  Raises:

    `vmodl.fault.InvalidArgument`_: 
       if both serviceName and location are not specified.


