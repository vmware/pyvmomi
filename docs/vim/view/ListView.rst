.. _vim.Task: ../../vim/Task.rst

.. _VI API 2.5: ../../vim/version.rst#vimversionversion2

.. _vim.view.View: ../../vim/view/View.rst

.. _vmodl.ManagedObject: ../../vim.ExtensibleManagedObject.rst

.. _vim.view.ManagedObjectView: ../../vim/view/ManagedObjectView.rst


vim.view.ListView
=================
  The `ListView`_ managed object provides access to updates on a specific set of objects. You can use a `ListView`_ with a `PropertyCollector`_ method to retrieve data or receive notification of changes. For information about using views with the `PropertyCollector`_ , see the description of `ViewManager`_ .When you invoke the `CreateListView`_ method, you specify a list of objects. The `view`_ list always represents the current configuration of the virtual environment and reflects any subsequent changes that occur.


:extends: vim.view.ManagedObjectView_
:since: `VI API 2.5`_


Attributes
----------


Methods
-------


ModifyListView(add, remove):
   Modify the list by giving a delta of entities to add and entities to remove.May partially succeed if some objects could not be resolved. The operation will still succeed for all objects which could be resolved, and the list of those which failed is returned as the result.


  Privilege:



  Args:
    add (`vmodl.ManagedObject`_, optional):
       Optional list of objects to add to the view.


    remove (`vmodl.ManagedObject`_, optional):
       Optional list of objects to remove from the view.




  Returns:
    [`vmodl.ManagedObject`_]:
         A list containing any objects in 'add' that could not be resolved.


ResetListView(obj):
   Replaces the list with an entirely new set of objects. If the entire set is changing, this is less data to send than a delta.May partially succeed if some objects could not be resolved. The operation will still succeed for all objects which could be resolved, and the list of those which failed is as the result.


  Privilege:



  Args:
    obj (`vmodl.ManagedObject`_, optional):
       The new list of objects.




  Returns:
    [`vmodl.ManagedObject`_]:
         A list containing any objects in 'obj' that could not be resolved.


ResetListViewFromView(view):
   Replaces the list with the set of objects in a given view.


  Privilege:



  Args:
    view (`vim.view.View`_):
       The view to copy objects from.




  Returns:
    None
         


