.. _vim.Task: ../../vim/Task.rst

.. _VI API 2.5: ../../vim/version.rst#vimversionversion2

.. _vim.view.View: ../../vim/view/View.rst

.. _vmodl.ManagedObject: ../../vim.ExtensibleManagedObject.rst


vim.view.ManagedObjectView
==========================
   `ManagedObjectView`_ is the base class for view objects that provide access to a set of `ManagedEntity`_ objects. `ManagedObjectView`_ defines a view list; the list contains references to objects in the view. To create a view use the `ViewManager`_ methods.


:extends: vim.view.View_
:since: `VI API 2.5`_


Attributes
----------
    view (`vmodl.ManagedObject`_):
       The list of references to objects mapped by this view.


Methods
-------


