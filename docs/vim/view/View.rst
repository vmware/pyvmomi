.. _vim.Task: ../../vim/Task.rst

.. _VI API 2.5: ../../vim/version.rst#vimversionversion2


vim.view.View
=============
   `View`_ is the base class for session-specific view objects. A view is a mechanism that supports selection of objects on the server and subsequently, access to those objects. To create a view, use the `ViewManager`_ methods. A view exists until you terminate it by calling the `DestroyView`_ method, or until the end of the session. Access to a view is limited to the session in which it is created.There are three types of views:
   * 
   * `ContainerView`_
   * 
   * 
   * `ListView`_
   * 
   * 
   * `InventoryView`_
   * 
   * 
   * A view maintains a
   * `view`_
   * list that contains managed object references. You can use a view with the
   * `PropertyCollector`_
   * to retrieve data and obtain notification of changes to the virtual environment. For information about using views with the PropertyCollector, see the description of
   * `ViewManager`_
   * .


:since: `VI API 2.5`_


Attributes
----------


Methods
-------


DestroyView():
   Destroy this view.


  Privilege:
               System.View



  Args:


  Returns:
    None
         


