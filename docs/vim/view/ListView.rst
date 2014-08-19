
vim.view.ListView
=================
  The `ListView <vim/view/ListView.rst>`_ managed object provides access to updates on a specific set of objects. You can use a `ListView <vim/view/ListView.rst>`_ with a `PropertyCollector <vmodl/query/PropertyCollector.rst>`_ method to retrieve data or receive notification of changes. For information about using views with the `PropertyCollector <vmodl/query/PropertyCollector.rst>`_ , see the description of `ViewManager <vim/view/ViewManager.rst>`_ .When you invoke the `CreateListView <vim/view/ViewManager.rst#createListView>`_ method, you specify a list of objects. The `view <vim/view/ManagedObjectView.rst#view>`_ list always represents the current configuration of the virtual environment and reflects any subsequent changes that occur.


:extends: vim.view.ManagedObjectView_
:since: `VI API 2.5 <vim/version.rst#vimversionversion2>`_


Attributes
----------


Methods
-------


ModifyListView(add, remove):
   Modify the list by giving a delta of entities to add and entities to remove.May partially succeed if some objects could not be resolved. The operation will still succeed for all objects which could be resolved, and the list of those which failed is returned as the result.


  Privilege:



  Args:
    add (`vmodl.ManagedObject <vim.ExtensibleManagedObject.rst>`_, optional):
       Optional list of objects to add to the view.


    remove (`vmodl.ManagedObject <vim.ExtensibleManagedObject.rst>`_, optional):
       Optional list of objects to remove from the view.




  Returns:
    [`vmodl.ManagedObject <vim.ExtensibleManagedObject.rst>`_]:
         A list containing any objects in 'add' that could not be resolved.


ResetListView(obj):
   Replaces the list with an entirely new set of objects. If the entire set is changing, this is less data to send than a delta.May partially succeed if some objects could not be resolved. The operation will still succeed for all objects which could be resolved, and the list of those which failed is as the result.


  Privilege:



  Args:
    obj (`vmodl.ManagedObject <vim.ExtensibleManagedObject.rst>`_, optional):
       The new list of objects.




  Returns:
    [`vmodl.ManagedObject <vim.ExtensibleManagedObject.rst>`_]:
         A list containing any objects in 'obj' that could not be resolved.


ResetListViewFromView(view):
   Replaces the list with the set of objects in a given view.


  Privilege:



  Args:
    view (`vim.view.View <vim/view/View.rst>`_):
       The view to copy objects from.




  Returns:
    None
         


