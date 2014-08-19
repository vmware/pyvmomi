
vim.view.ManagedObjectView
==========================
   `ManagedObjectView <vim/view/ManagedObjectView.rst>`_ is the base class for view objects that provide access to a set of `ManagedEntity <vim/ManagedEntity.rst>`_ objects. `ManagedObjectView <vim/view/ManagedObjectView.rst>`_ defines a view list; the list contains references to objects in the view. To create a view use the `ViewManager <vim/view/ViewManager.rst>`_ methods.


:extends: vim.view.View_
:since: `VI API 2.5 <vim/version.rst#vimversionversion2>`_


Attributes
----------
    view ([`vmodl.ManagedObject <vim.ExtensibleManagedObject.rst>`_]):
       The list of references to objects mapped by this view.


Methods
-------


