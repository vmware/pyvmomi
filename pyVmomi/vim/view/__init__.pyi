# Copyright (c) 2006-2026 Broadcom. All Rights Reserved.
# The term "Broadcom" refers to Broadcom Inc. and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

import typing as _typing
import pyVmomi.VmomiSupport
import pyVmomi.vim



class View(pyVmomi.VmomiSupport.ManagedObject):
   """
   `pyVmomi.vim.view.View` is the base class for session-specific view objects.
   
   A view is a mechanism that supports selection of objects on the server
   and subsequently, access to those objects.
   To create a view, use the `pyVmomi.vim.view.ViewManager` methods.
   A view exists until you terminate it by calling the `pyVmomi.vim.view.View.destroy` method,
   or until the end of the session.
   Access to a view is limited to the session in which it is created.
   
   There are three types of views:
   - `pyVmomi.vim.view.ContainerView`
   - `pyVmomi.vim.view.ListView`
   - `pyVmomi.vim.view.InventoryView`
     
   A view maintains a `pyVmomi.vim.view.ManagedObjectView.view` list that contains
   managed object references. You can use a view
   with the `pyVmomi.vmodl.query.PropertyCollector` to retrieve data and
   obtain notification of changes to the virtual environment.
   For information about using views with the PropertyCollector,
   see the description of `pyVmomi.vim.view.ViewManager`.
   """
   def Destroy(self) -> None:
      """Destroy this view."""
      ...


class ManagedObjectView(View):
   """
   `pyVmomi.vim.view.ManagedObjectView` is the base class for view objects that provide access
   to a set of `pyVmomi.vim.ManagedEntity` objects.
   
   `pyVmomi.vim.view.ManagedObjectView` defines
   a view list; the list contains references to objects in the view.
   To create a view use the `pyVmomi.vim.view.ViewManager` methods.
   """
   @property
   def view(self) -> list[pyVmomi.VmomiSupport.ManagedObject]:
      """The list of references to objects mapped by this view."""
      ...


class ContainerView(ManagedObjectView):
   """
   The `pyVmomi.vim.view.ContainerView` managed object provides a means of monitoring the contents of
   a single container and, optionally, other containers.
   
   You can use a `pyVmomi.vim.view.ContainerView` with a `pyVmomi.vmodl.query.PropertyCollector` method
   to retrieve data or receive notification of changes. For information about using views
   with the `pyVmomi.vmodl.query.PropertyCollector`, see the description of `pyVmomi.vim.view.ViewManager`.
   
   When you invoke the `pyVmomi.vim.view.ViewManager.createContainerView` method, you specify
   a managed object instance that provides the starting point for object selection.
   You can use the following managed objects as the basis of a container view:
   - `pyVmomi.vim.Folder`
   - `pyVmomi.vim.Datacenter`
   - `pyVmomi.vim.ComputeResource`
   - `pyVmomi.vim.ResourcePool`
   - `pyVmomi.vim.HostSystem`
     
   Once you have created the view, the `pyVmomi.vim.view.ManagedObjectView.view` list
   always represents the current configuration of the virtual environment and reflects
   any subsequent changes that occur.
   """
   @property
   def container(self) -> pyVmomi.vim.ManagedEntity:
      """
      The Folder, Datacenter, ComputeResource, ResourcePool, or HostSystem instance
      that provides the objects that the view presents.
      """
      ...
   @property
   def type(self) -> list[type]:
      """
      An optional list of types to be applied to the set of objects in the view.
      
      The list of types indicates objects that are included in the view.
      If empty, all types are included.
      """
      ...
   @property
   def recursive(self) -> bool:
      """
      Whether to include only the immediate children of the container instance,
      or to include additional objects by following the paths beyond the
      immediate children.
      
      For information about recursive behavior, see the description of
      `pyVmomi.vim.view.ViewManager.createContainerView`.
      """
      ...


class InventoryView(ManagedObjectView):
   """
   The `pyVmomi.vim.view.InventoryView` managed object provides a means of browsing the inventory and tracking
   changes to open folders.
   
   This managed object is particularly useful for UI clients that
   display a tree-based navigation panel of the inventory.
   
   `pyVmomi.vim.view.InventoryView` maintains the `pyVmomi.vim.view.ManagedObjectView.view` list
   of managed object references to inventory objects. When you create an inventory view
   (`pyVmomi.vim.view.ViewManager.createInventoryView`), the server initializes the view's object
   list with a single folder - the root folder.
   
   `pyVmomi.vim.view.InventoryView` provides methods to open and close folders in the inventory. Use these
   methods to add and subtract objects from the `pyVmomi.vim.view.ManagedObjectView.view` list.
   Use the `pyVmomi.vim.view.InventoryView` together with the `pyVmomi.vmodl.query.PropertyCollector`
   to manage the data resulting from `pyVmomi.vim.view.InventoryView.openFolder`
   and `pyVmomi.vim.view.InventoryView.closeFolder` methods. By using the `pyVmomi.vmodl.query.PropertyCollector`,
   you have access to the modifications to the view, rather than processing the entire view list.
   
   For example, you might use the following sequence of operations with
   an `pyVmomi.vim.view.InventoryView` and the `pyVmomi.vmodl.query.PropertyCollector`:
   1. Create an `pyVmomi.vim.view.InventoryView`.
   2. Create a filter specification for the `pyVmomi.vmodl.query.PropertyCollector`.
      - Use the `pyVmomi.vim.view.InventoryView` as the starting object in the
        `pyVmomi.vmodl.query.PropertyCollector.ObjectSpec` for the filter.
      - Use a set of `pyVmomi.vmodl.query.PropertyCollector.TraversalSpec`
        data objects to identify paths in possible inventory configurations.
      - Use the `pyVmomi.vmodl.query.PropertyCollector.PropertySpec`
        to identify object properties for retrieval.
   3. Use either the `pyVmomi.vmodl.query.PropertyCollector.checkForUpdates` or
      `pyVmomi.vmodl.query.PropertyCollector.waitForUpdates` method to obtain
      `pyVmomi.vim.view.InventoryView` modifications. Both methods return
      an `pyVmomi.vmodl.query.PropertyCollector.UpdateSet` object that describes
      the changes returned by the `pyVmomi.vmodl.query.PropertyCollector`.
   4. Call the `pyVmomi.vim.view.InventoryView.openFolder` or `pyVmomi.vim.view.InventoryView.closeFolder`.
   """
   def OpenFolder(self, entity: list[pyVmomi.vim.ManagedEntity]) -> list[pyVmomi.vim.ManagedEntity]:
      """
      Adds the child objects of a given managed entity to the view.
      
      If a `pyVmomi.vim.Datacenter` is returned as a child, the implicit virtual machine folder and
      host folder objects are also returned. If a `pyVmomi.vim.ComputeResource` is returned,
      the implicit root `pyVmomi.vim.ResourcePool` and `pyVmomi.vim.HostSystem` objects are also returned.
      
      May partially succeed if some entities could not be resolved. The operation
      will still succeed for all entities which could be resolved, and the
      list of those which failed is returned as the result.
      
      Args:
          entity: An array of managed object references. Each array entry is a reference
              to an entity to expand. Expands each entity in the
              order given. If an entity is not in the current view,
              expands the view as needed.
      
      Returns:
          A list containing any entities in the argument could not be resolved.
      """
      ...
   def CloseFolder(self, entity: list[pyVmomi.vim.ManagedEntity]) -> list[pyVmomi.vim.ManagedEntity]:
      """
      Notify the server that folder(s) have been closed, and changes for all
      its contained objects should no longer be sent.
      
      The associated child
      objects are removed from the view. The containers themselves
      will still be retained as open objects until their parent is closed.
      
      May partially succeed if some entities could not be resolved. The operation
      will still succeed for all entities that could be resolved, and the
      list of those that failed is returned as the result.
      
      Args:
          entity: An array of managed object references. Each array entry is a
              reference to an entity to collapse.
      
      Returns:
          A list containing any entities in the argument could not be resolved.
      """
      ...


class ListView(ManagedObjectView):
   """
   The `pyVmomi.vim.view.ListView` managed object provides access to updates on a specific set of objects.
   
   You can use a `pyVmomi.vim.view.ListView` with a `pyVmomi.vmodl.query.PropertyCollector` method
   to retrieve data or receive notification of changes. For information about using views
   with the `pyVmomi.vmodl.query.PropertyCollector`, see the description of `pyVmomi.vim.view.ViewManager`.
   
   When you invoke the `pyVmomi.vim.view.ViewManager.createListView` method, you specify
   a list of objects. The `pyVmomi.vim.view.ManagedObjectView.view` list
   always represents the current configuration of the virtual environment
   and reflects any subsequent changes that occur.
   """
   def Modify(self, add: list[pyVmomi.VmomiSupport.ManagedObject], remove: list[pyVmomi.VmomiSupport.ManagedObject]) -> list[pyVmomi.VmomiSupport.ManagedObject]:
      """
      Modify the list by giving a delta of entities to add and
      entities to remove.
      
      May partially succeed if some objects could not be resolved. The operation
      will still succeed for all objects which could be resolved, and the
      list of those which failed is returned as the result.
      
      Args:
          add: Optional list of objects to add to the view.
          remove: Optional list of objects to remove from the view.
      
      Returns:
          A list containing any objects in 'add' that could not be resolved.
      """
      ...
   def Reset(self, obj: list[pyVmomi.VmomiSupport.ManagedObject]) -> list[pyVmomi.VmomiSupport.ManagedObject]:
      """
      Replaces the list with an entirely new set of objects.
      
      If
      the entire set is changing, this is less data to send than a delta.
      
      May partially succeed if some objects could not be resolved. The operation
      will still succeed for all objects which could be resolved, and the
      list of those which failed is as the result.
      
      Args:
          obj: The new list of objects.
      
      Returns:
          A list containing any objects in 'obj' that could not be resolved.
      """
      ...
   def ResetFromView(self, view: View) -> None:
      """
      Replaces the list with the set of objects in a given view.
      
      Args:
          view: The view to copy objects from.
      """
      ...


class ViewManager(pyVmomi.VmomiSupport.ManagedObject):
   """
   The `pyVmomi.vim.view.ViewManager` managed object provides methods to create `pyVmomi.vim.view.ContainerView`,
   `pyVmomi.vim.view.InventoryView`, and `pyVmomi.vim.view.ListView` managed objects.
   
   The `pyVmomi.vim.view.ViewManager` also maintains a list of managed object references
   to the views that you have created. Use the `pyVmomi.vim.view.ViewManager.viewList`
   property to access the views.
   
   A `pyVmomi.vim.view.View` is a mechanism that supports selection of objects on the server
   and subsequently, access to those objects. Views can simplify the task of
   retrieving data from the server. When you use a view, you can use a single
   invocation of a `pyVmomi.vmodl.query.PropertyCollector` method
   to retrieve data or receive notification of changes instead of multiple invocations
   involving multiple filter specifications. A view exists until you destroy it
   or until the end of the session.
   
   The `pyVmomi.vim.view.ViewManager` supports the following views:
   - A `pyVmomi.vim.view.ContainerView` is based on `pyVmomi.vim.Folder`,
     `pyVmomi.vim.Datacenter`, `pyVmomi.vim.ComputeResource`,
     `pyVmomi.vim.ResourcePool`, or `pyVmomi.vim.HostSystem` managed objects.
     Use a container view to monitor the container contents and optionally,
     its descendants.
   - A `pyVmomi.vim.view.ListView` managed object is based on an arbitrary but
     specific set of objects. When you create a list view, you provide
     a list of objects to populate the view
     (`pyVmomi.vim.view.ViewManager.createListView`),
     or you provide an existing view from which the new view is created
     (`pyVmomi.vim.view.ViewManager.createListViewFromView`).
   - An `pyVmomi.vim.view.InventoryView` managed object is based on the entire inventory.
     Use an inventory view as a general mechanism to monitor the inventory
     or portions of the inventory.
     
   For example, you might use the following sequence of operations to get the
   names of all the virtual machines on a server:
   1. Create a `pyVmomi.vim.view.ContainerView` for the root folder in the server inventory.
      For the `pyVmomi.vim.view.ContainerView`, use the `pyVmomi.vim.view.ContainerView.type` property
      to include only virtual machines.
   2. Create a filter specification for the `pyVmomi.vmodl.query.PropertyCollector`.
      - Use the `pyVmomi.vim.view.ContainerView` as the starting object in the
        `pyVmomi.vmodl.query.PropertyCollector.ObjectSpec` for the filter.
      - Use the `pyVmomi.vmodl.query.PropertyCollector.TraversalSpec`
        to select all objects in the view list (all the virtual machines).
      - Use the `pyVmomi.vmodl.query.PropertyCollector.PropertySpec`
        to retrieve the name property from each virtual machine.
   3. Invoke the `pyVmomi.vmodl.query.PropertyCollector`
      `pyVmomi.vmodl.query.PropertyCollector.retrieveContents` method.
   """
   @property
   def viewList(self) -> list[View]:
      """
      An array of view references.
      
      Each array entry is a managed object reference
      to a view created by this ViewManager.
      """
      ...

   def CreateInventoryView(self) -> InventoryView:
      """Create a new `pyVmomi.vim.view.InventoryView` managed object for this session."""
      ...
   def CreateContainerView(self, container: pyVmomi.vim.ManagedEntity, type: list[type], recursive: bool) -> ContainerView:
      """
      Create a `pyVmomi.vim.view.ContainerView` managed object for this session.
      
      The method returns
      a reference to a `pyVmomi.vim.view.ContainerView` object that has a list of managed object references.
      The list references objects in the container and may include references to objects from
      additional containers. You can configure the resulting list of objects by specifying
      a type list and recursion. Once you have created the view, the object list always
      represents the current configuration of the virtual environment and reflects any
      subsequent changes that occur.
      
      Args:
          container: A reference to an instance of a `pyVmomi.vim.Folder`,
              `pyVmomi.vim.Datacenter`, `pyVmomi.vim.ComputeResource`,
              `pyVmomi.vim.ResourcePool`, or `pyVmomi.vim.HostSystem` object.
          type: An optional list of managed entity types. The server
              associates only objects of the specified type(s) with the view.
              If you specify an empty array, the server uses all types.
          recursive: Whether to include only the immediate children of the
              container instance, or to include additional objects by
              following paths beyond the immediate children.
              
              When recursive is false, the list of objects contains
              only immediate children.
              When recursive is true, the server populates the list
              by following references beyond the immediate children
              (using a child's references, and then references in the
              resulting objects, and so on).
              
              Depending on the container type, the server will use the following
              properties of the container instance to obtain objects for the
              view's object list:
              - `pyVmomi.vim.Folder` object - `pyVmomi.vim.Folder.childEntity`
                property.
                If recursive is false, the container list includes the reference
                to the child entity in the folder instance.
                If recursive is true, the server will follow the child
                folder path(s) to collect additional childEntity references.
              - `pyVmomi.vim.ResourcePool` object - `pyVmomi.vim.ResourcePool.vm`
                and `pyVmomi.vim.ResourcePool.resourcePool` properties.
                If recursive is false, the object list will contain references
                to the virtual machines associated with this resource pool,
                and references to virtual machines associated with the
                immediate child resource pools. If recursive is true,
                the server will follow all child resource pool paths
                extending from the immediate children (and their children,
                and so on) to collect additional references to virtual machines.
              - `pyVmomi.vim.ComputeResource` object - `pyVmomi.vim.ComputeResource.host`
                and `pyVmomi.vim.ComputeResource.resourcePool` properties.
                If recursive is false, the object list will contain references
                to the host systems associated with this compute resource,
                references to virtual machines associated with the
                host systems, and references to virtual machines associated
                with the immediate child resource pools.
                If recursive is true, the server will follow the child
                resource pool paths (and their child resource pool paths,
                and so on) to collect additional references to virtual machines.
              - `pyVmomi.vim.Datacenter` object - `pyVmomi.vim.Datacenter.vmFolder`,
                `pyVmomi.vim.Datacenter.hostFolder`,
                `pyVmomi.vim.Datacenter.datastoreFolder`, and
                `pyVmomi.vim.Datacenter.networkFolder` properties.
                If recursive is set to false, the server uses the
                immediate child folders for the virtual machines,
                hosts, datastores, and networks associated with this
                datacenter. If recursive is set to true, the server
                will follow the folder paths to collect references
                to additional objects.
              - `pyVmomi.vim.HostSystem` object - `pyVmomi.vim.HostSystem.vm`
                property.
                The view object list contains references to the virtual machines
                associated with this host system. The value of recursive does not
                affect this behavior.
      """
      ...
   def CreateListView(self, obj: list[pyVmomi.VmomiSupport.ManagedObject]) -> ListView:
      """
      Create a `pyVmomi.vim.view.ListView` object for this session.
      
      The method returns
      a session object that has a list of managed object references. The list
      of references corresponds to the input object list.
      You can modify the resulting list after you have created the object.
      
      Args:
          obj: The initial list of objects in the view.
      """
      ...
   def CreateListViewFromView(self, view: View) -> ListView:
      """
      Create a `pyVmomi.vim.view.ListView` object for this session.
      
      This method uses an existing
      view to construct the object list for the new view.
      
      Args:
          view: The view that will provide the object list for the
              new ListView object.
      """
      ...
