.. _vim.Task: ../vim/Task.rst

.. _vSphere API 4.0: ../vim/version.rst#vimversionversion5

.. _vmodl.fault.InvalidArgument: ../vmodl/fault/InvalidArgument.rst

.. _vim.ResourcePlanningManager.DatabaseSizeParam: ../vim/ResourcePlanningManager/DatabaseSizeParam.rst

.. _vim.ResourcePlanningManager.DatabaseSizeEstimate: ../vim/ResourcePlanningManager/DatabaseSizeEstimate.rst


vim.ResourcePlanningManager
===========================
  


:since: `vSphere API 4.0`_


Attributes
----------


Methods
-------


EstimateDatabaseSize(dbSizeParam):
   Estimates the database size required to store VirtualCenter data.


  Privilege:
               System.Read



  Args:
    dbSizeParam (`vim.ResourcePlanningManager.DatabaseSizeParam`_):
        `DatabaseSizeParam`_ Contains the summary of an inventory for which the database size requirements are to be computed. It also contains the historic interval setting for which the database computations are to be done. This is an optional parameter and the current virtual center historical settings are used by default. There are many other optional fields in the dbSizeParam structure that are appropriately filled up based on some heuristics.




  Returns:
    `vim.ResourcePlanningManager.DatabaseSizeEstimate`_:
          `DatabaseSizeEstimate`_ Returns the size required in MB of the database and the number of database rows.

  Raises:

    `vmodl.fault.InvalidArgument`_: 
       if the set of arguments passed to the function is not specified correctly.


