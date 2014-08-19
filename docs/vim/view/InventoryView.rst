
vim.view.InventoryView
======================
  The `InventoryView <vim/view/InventoryView.rst>`_ managed object provides a means of browsing the inventory and tracking changes to open folders. This managed object is particularly useful for UI clients that display a tree-based navigation panel of the inventory. `InventoryView <vim/view/InventoryView.rst>`_ maintains the `view <vim/view/ManagedObjectView.rst#view>`_ list of managed object references to inventory objects. When you create an inventory view ( `CreateInventoryView <vim/view/ViewManager.rst#createInventoryView>`_ ), the server initializes the view's object list with a single folder - the root folder. `InventoryView <vim/view/InventoryView.rst>`_ provides methods to open and close folders in the inventory. Use these methods to add and subtract objects from the `view <vim/view/ManagedObjectView.rst#view>`_ list. Use the `InventoryView <vim/view/InventoryView.rst>`_ together with the `PropertyCollector <vmodl/query/PropertyCollector.rst>`_ to manage the data resulting from `OpenInventoryViewFolder <vim/view/InventoryView.rst#openFolder>`_ and `CloseInventoryViewFolder <vim/view/InventoryView.rst#closeFolder>`_ methods. By using the `PropertyCollector <vmodl/query/PropertyCollector.rst>`_ , you have access to the modifications to the view, rather than processing the entire view list.For example, you might use the following sequence of operations with an `InventoryView <vim/view/InventoryView.rst>`_ and the `PropertyCollector <vmodl/query/PropertyCollector.rst>`_ :
   * Create an
   * `InventoryView <vim/view/InventoryView.rst>`_
   * .
   * Create a filter specification for the
   * `PropertyCollector <vmodl/query/PropertyCollector.rst>`_
   * .
   * 
   * Use the
   * `InventoryView <vim/view/InventoryView.rst>`_
   * as the starting object in the
   * `ObjectSpec <vmodl/query/PropertyCollector/ObjectSpec.rst>`_
   * for the filter.
   * Use a set of
   * `TraversalSpec <vmodl/query/PropertyCollector/TraversalSpec.rst>`_
   * data objects to identify paths in possible inventory configurations.
   * Use the
   * `PropertySpec <vmodl/query/PropertyCollector/PropertySpec.rst>`_
   * to identify object properties for retrieval.
   * 
   * Use either the
   * `CheckForUpdates <vmodl/query/PropertyCollector.rst#checkForUpdates>`_
   * or
   * `WaitForUpdates <vmodl/query/PropertyCollector.rst#waitForUpdates>`_
   * method to obtain
   * `InventoryView <vim/view/InventoryView.rst>`_
   * modifications. Both methods return an
   * `UpdateSet <vmodl/query/PropertyCollector/UpdateSet.rst>`_
   * object that describes the changes returned by the
   * `PropertyCollector <vmodl/query/PropertyCollector.rst>`_
   * .
   * Call the
   * `OpenInventoryViewFolder <vim/view/InventoryView.rst#openFolder>`_
   * or
   * `method <vim/view/InventoryView.rst#closeFolder>`_
   * .
   * 


:extends: vim.view.ManagedObjectView_
:since: `VI API 2.5 <vim/version.rst#vimversionversion2>`_


Attributes
----------


Methods
-------


OpenInventoryViewFolder(entity):
   Adds the child objects of a given managed entity to the view.If a `Datacenter <vim/Datacenter.rst>`_ is returned as a child, the implicit virtual machine folder and host folder objects are also returned. If a `ComputeResource <vim/ComputeResource.rst>`_ is returned, the implicit root `ResourcePool <vim/ResourcePool.rst>`_ and `HostSystem <vim/HostSystem.rst>`_ objects are also returned.May partially succeed if some entities could not be resolved. The operation will still succeed for all entities which could be resolved, and the list of those which failed is returned as the result.


  Privilege:



  Args:
    entity (`vim.ManagedEntity <vim/ManagedEntity.rst>`_):
       An array of managed object references. Each array entry is a reference to an entity to expand. Expands each entity in the order given. If an entity is not in the current view, expands the view as needed.




  Returns:
    [`vim.ManagedEntity <vim/ManagedEntity.rst>`_]:
         A list containing any entities in the argument could not be resolved.


CloseInventoryViewFolder(entity):
   Notify the server that folder(s) have been closed, and changes for all its contained objects should no longer be sent. The associated child objects are removed from the view. The containers themselves will still be retained as open objects until their parent is closed.May partially succeed if some entities could not be resolved. The operation will still succeed for all entities that could be resolved, and the list of those that failed is returned as the result.


  Privilege:



  Args:
    entity (`vim.ManagedEntity <vim/ManagedEntity.rst>`_):
       An array of managed object references. Each array entry is a reference to an entity to collapse.




  Returns:
    [`vim.ManagedEntity <vim/ManagedEntity.rst>`_]:
         A list containing any entities in the argument could not be resolved.


