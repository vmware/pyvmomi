
vim.view.View
=============
   `View <vim/view/View.rst>`_ is the base class for session-specific view objects. A view is a mechanism that supports selection of objects on the server and subsequently, access to those objects. To create a view, use the `ViewManager <vim/view/ViewManager.rst>`_ methods. A view exists until you terminate it by calling the `DestroyView <vim/view/View.rst#destroy>`_ method, or until the end of the session. Access to a view is limited to the session in which it is created.There are three types of views:
   * 
   * `ContainerView <vim/view/ContainerView.rst>`_
   * 
   * 
   * `ListView <vim/view/ListView.rst>`_
   * 
   * 
   * `InventoryView <vim/view/InventoryView.rst>`_
   * 
   * 
   * A view maintains a
   * `view <vim/view/ManagedObjectView.rst#view>`_
   * list that contains managed object references. You can use a view with the
   * `PropertyCollector <vmodl/query/PropertyCollector.rst>`_
   * to retrieve data and obtain notification of changes to the virtual environment. For information about using views with the PropertyCollector, see the description of
   * `ViewManager <vim/view/ViewManager.rst>`_
   * .


:since: `VI API 2.5 <vim/version.rst#vimversionversion2>`_


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
         


