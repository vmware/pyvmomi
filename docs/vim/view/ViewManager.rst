
vim.view.ViewManager
====================
  The `ViewManager <vim/view/ViewManager.rst>`_ managed object provides methods to create `ContainerView <vim/view/ContainerView.rst>`_ , `InventoryView <vim/view/InventoryView.rst>`_ , and `ListView <vim/view/ListView.rst>`_ managed objects. The `ViewManager <vim/view/ViewManager.rst>`_ also maintains a list of managed object references to the views that you have created. Use the `viewList <vim/view/ViewManager.rst#viewList>`_ property to access the views.A `View <vim/view/View.rst>`_ is a mechanism that supports selection of objects on the server and subsequently, access to those objects. Views can simplify the task of retrieving data from the server. When you use a view, you can use a single invocation of a `PropertyCollector <vmodl/query/PropertyCollector.rst>`_ method to retrieve data or receive notification of changes instead of multiple invocations involving multiple filter specifications. A view exists until you destroy it or until the end of the session.The `ViewManager <vim/view/ViewManager.rst>`_ supports the following views:
   * A
   * `ContainerView <vim/view/ContainerView.rst>`_
   * is based on
   * `Folder <vim/Folder.rst>`_
   * ,
   * `Datacenter <vim/Datacenter.rst>`_
   * ,
   * `ComputeResource <vim/ComputeResource.rst>`_
   * ,
   * `ResourcePool <vim/ResourcePool.rst>`_
   * , or
   * `HostSystem <vim/HostSystem.rst>`_
   * managed objects. Use a container view to monitor the container contents and optionally, its descendants.
   * A
   * `ListView <vim/view/ListView.rst>`_
   * managed object is based on an arbitrary but specific set of objects. When you create a list view, you provide a list of objects to populate the view (
   * `CreateListView <vim/view/ViewManager.rst#createListView>`_
   * ), or you provide an existing view from which the new view is created (
   * `CreateListViewFromView <vim/view/ViewManager.rst#createListViewFromView>`_
   * ).
   * An
   * `InventoryView <vim/view/InventoryView.rst>`_
   * managed object is based on the entire inventory. Use an inventory view as a general mechanism to monitor the inventory or portions of the inventory.
   * 
   * For example, you might use the following sequence of operations to get the names of all the virtual machines on a server:
   * 
   * Create a
   * `ContainerView <vim/view/ContainerView.rst>`_
   * for the root folder in the server inventory. For the
   * `ContainerView <vim/view/ContainerView.rst>`_
   * , use the
   * `type <vim/view/ContainerView.rst#type>`_
   * property to include only virtual machines.
   * Create a filter specification for the
   * `PropertyCollector <vmodl/query/PropertyCollector.rst>`_
   * .
   * 
   * Use the
   * `ContainerView <vim/view/ContainerView.rst>`_
   * as the starting object in the
   * `ObjectSpec <vmodl/query/PropertyCollector/ObjectSpec.rst>`_
   * for the filter.
   * Use the
   * `TraversalSpec <vmodl/query/PropertyCollector/TraversalSpec.rst>`_
   * to select all objects in the view list (all the virtual machines).
   * Use the
   * `PropertySpec <vmodl/query/PropertyCollector/PropertySpec.rst>`_
   * to retrieve the name property from each virtual machine.
   * 
   * Invoke the
   * `PropertyCollector <vmodl/query/PropertyCollector.rst>`_
   * 
   * `RetrieveProperties <vmodl/query/PropertyCollector.rst#retrieveContents>`_
   * method.
   * 


:since: `VI API 2.5 <vim/version.rst#vimversionversion2>`_


Attributes
----------
    viewList ([`vim.view.View <vim/view/View.rst>`_]):
      privilege: System.View
       An array of view references. Each array entry is a managed object reference to a view created by this ViewManager.


Methods
-------


CreateInventoryView():
   Create a new `InventoryView <vim/view/InventoryView.rst>`_ managed object for this session.


  Privilege:
               System.View



  Args:


  Returns:
    `vim.view.InventoryView <vim/view/InventoryView.rst>`_:
         


CreateContainerView(container, type, recursive):
   Create a `ContainerView <vim/view/ContainerView.rst>`_ managed object for this session. The method returns a reference to a `ContainerView <vim/view/ContainerView.rst>`_ object that has a list of managed object references. The list references objects in the container and may include references to objects from additional containers. You can configure the resulting list of objects by specifying a type list and recursion. Once you have created the view, the object list always represents the current configuration of the virtual environment and reflects any subsequent changes that occur.


  Privilege:
               System.View



  Args:
    container (`vim.ManagedEntity <vim/ManagedEntity.rst>`_):
       A reference to an instance of a `Folder <vim/Folder.rst>`_ , `Datacenter <vim/Datacenter.rst>`_ , `ComputeResource <vim/ComputeResource.rst>`_ , `ResourcePool <vim/ResourcePool.rst>`_ , or `HostSystem <vim/HostSystem.rst>`_ object.


    type (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):
       An optional list of managed entity types. The server associates only objects of the specified type(s) with the view. If you specify an empty array, the server uses all types.


    recursive (`bool <https://docs.python.org/2/library/stdtypes.html>`_):
       Whether to include only the immediate children of the container instance, or to include additional objects by following paths beyond the immediate children.When recursive is false, the list of objects contains only immediate children. When recursive is true, the server populates the list by following references beyond the immediate children (using a child's references, and then references in the resulting objects, and so on).Depending on the container type, the server will use the following properties of the container instance to obtain objects for the view's object list:
        * 
        * `Folder <vim/Folder.rst>`_
        * object -
        * `childEntity <vim/Folder.rst#childEntity>`_
        * property. If recursive is false, the container list includes the reference to the child entity in the folder instance. If recursive is true, the server will follow the child folder path(s) to collect additional childEntity references.
        * 
        * `ResourcePool <vim/ResourcePool.rst>`_
        * object -
        * `vm <vim/ResourcePool.rst#vm>`_
        * and
        * `resourcePool <vim/ResourcePool.rst#resourcePool>`_
        * properties. If recursive is false, the object list will contain references to the virtual machines associated with this resource pool, and references to virtual machines associated with the immediate child resource pools. If recursive is true, the server will follow all child resource pool paths extending from the immediate children (and their children, and so on) to collect additional references to virtual machines.
        * 
        * `ComputeResource <vim/ComputeResource.rst>`_
        * object -
        * `host <vim/ComputeResource.rst#host>`_
        * and
        * `resourcePool <vim/ComputeResource.rst#resourcePool>`_
        * properties. If recursive is false, the object list will contain references to the host systems associated with this compute resource, references to virtual machines associated with the host systems, and references to virtual machines associated with the immediate child resource pools. If recursive is true, the server will follow the child resource pool paths (and their child resource pool paths, and so on) to collect additional references to virtual machines.
        * 
        * `Datacenter <vim/Datacenter.rst>`_
        * object -
        * `vmFolder <vim/Datacenter.rst#vmFolder>`_
        * ,
        * `hostFolder <vim/Datacenter.rst#hostFolder>`_
        * ,
        * `datastoreFolder <vim/Datacenter.rst#datastoreFolder>`_
        * , and
        * `networkFolder <vim/Datacenter.rst#networkFolder>`_
        * properties. If recursive is set to false, the server uses the immediate child folders for the virtual machines, hosts, datastores, and networks associated with this datacenter. If recursive is set to true, the server will follow the folder paths to collect references to additional objects.
        * 
        * `HostSystem <vim/HostSystem.rst>`_
        * object -
        * `vm <vim/HostSystem.rst#vm>`_
        * property. The view object list contains references to the virtual machines associated with this host system. The value of recursive does not affect this behavior.
        * 




  Returns:
    `vim.view.ContainerView <vim/view/ContainerView.rst>`_:
         


CreateListView(obj):
   Create a `ListView <vim/view/ListView.rst>`_ object for this session. The method returns a session object that has a list of managed object references. The list of references corresponds to the input object list. You can modify the resulting list after you have created the object.


  Privilege:
               System.View



  Args:
    obj (`vmodl.ManagedObject <vim.ExtensibleManagedObject.rst>`_, optional):
       The initial list of objects in the view.




  Returns:
    `vim.view.ListView <vim/view/ListView.rst>`_:
         


CreateListViewFromView(view):
   Create a `ListView <vim/view/ListView.rst>`_ object for this session. This method uses an existing view to construct the object list for the new view.


  Privilege:
               System.View



  Args:
    view (`vim.view.View <vim/view/View.rst>`_):
       The view that will provide the object list for the new ListView object.




  Returns:
    `vim.view.ListView <vim/view/ListView.rst>`_:
         


