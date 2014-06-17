.. _vim.Task: ../../vim/Task.rst

.. _Datacenter: ../../vim/Datacenter.rst

.. _VI API 2.5: ../../vim/version.rst#vimversionversion2

.. _HostSystem: ../../vim/HostSystem.rst

.. _ResourcePool: ../../vim/ResourcePool.rst

.. _ComputeResource: ../../vim/ComputeResource.rst

.. _vim.ManagedEntity: ../../vim/ManagedEntity.rst

.. _vim.view.ManagedObjectView: ../../vim/view/ManagedObjectView.rst


vim.view.InventoryView
======================
  The `InventoryView`_ managed object provides a means of browsing the inventory and tracking changes to open folders. This managed object is particularly useful for UI clients that display a tree-based navigation panel of the inventory. `InventoryView`_ maintains the `view`_ list of managed object references to inventory objects. When you create an inventory view ( `CreateInventoryView`_ ), the server initializes the view's object list with a single folder - the root folder. `InventoryView`_ provides methods to open and close folders in the inventory. Use these methods to add and subtract objects from the `view`_ list. Use the `InventoryView`_ together with the `PropertyCollector`_ to manage the data resulting from `OpenInventoryViewFolder`_ and `CloseInventoryViewFolder`_ methods. By using the `PropertyCollector`_ , you have access to the modifications to the view, rather than processing the entire view list.For example, you might use the following sequence of operations with an `InventoryView`_ and the `PropertyCollector`_ :
   * Create an
   * `InventoryView`_
   * .
   * Create a filter specification for the
   * `PropertyCollector`_
   * .
   * 
   * Use the
   * `InventoryView`_
   * as the starting object in the
   * `ObjectSpec`_
   * for the filter.
   * Use a set of
   * `TraversalSpec`_
   * data objects to identify paths in possible inventory configurations.
   * Use the
   * `PropertySpec`_
   * to identify object properties for retrieval.
   * 
   * Use either the
   * `CheckForUpdates`_
   * or
   * `WaitForUpdates`_
   * method to obtain
   * `InventoryView`_
   * modifications. Both methods return an
   * `UpdateSet`_
   * object that describes the changes returned by the
   * `PropertyCollector`_
   * .
   * Call the
   * `OpenInventoryViewFolder`_
   * or
   * `method`_
   * .
   * 


:extends: vim.view.ManagedObjectView_
:since: `VI API 2.5`_


Attributes
----------


Methods
-------


OpenInventoryViewFolder(entity):
   Adds the child objects of a given managed entity to the view.If a `Datacenter`_ is returned as a child, the implicit virtual machine folder and host folder objects are also returned. If a `ComputeResource`_ is returned, the implicit root `ResourcePool`_ and `HostSystem`_ objects are also returned.May partially succeed if some entities could not be resolved. The operation will still succeed for all entities which could be resolved, and the list of those which failed is returned as the result.


  Privilege:



  Args:
    entity (`vim.ManagedEntity`_):
       An array of managed object references. Each array entry is a reference to an entity to expand. Expands each entity in the order given. If an entity is not in the current view, expands the view as needed.




  Returns:
    `vim.ManagedEntity`_:
         A list containing any entities in the argument could not be resolved.


CloseInventoryViewFolder(entity):
   Notify the server that folder(s) have been closed, and changes for all its contained objects should no longer be sent. The associated child objects are removed from the view. The containers themselves will still be retained as open objects until their parent is closed.May partially succeed if some entities could not be resolved. The operation will still succeed for all entities that could be resolved, and the list of those that failed is returned as the result.


  Privilege:



  Args:
    entity (`vim.ManagedEntity`_):
       An array of managed object references. Each array entry is a reference to an entity to collapse.




  Returns:
    `vim.ManagedEntity`_:
         A list containing any entities in the argument could not be resolved.


