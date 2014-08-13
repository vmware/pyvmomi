.. _str: https://docs.python.org/2/library/stdtypes.html

.. _bool: https://docs.python.org/2/library/stdtypes.html

.. _vim.Task: ../../vim/Task.rst

.. _VI API 2.5: ../../vim/version.rst#vimversionversion2

.. _vim.ManagedEntity: ../../vim/ManagedEntity.rst

.. _CreateContainerView: ../../vim/view/ViewManager.rst#createContainerView

.. _vim.view.ManagedObjectView: ../../vim/view/ManagedObjectView.rst


vim.view.ContainerView
======================
  The `ContainerView`_ managed object provides a means of monitoring the contents of a single container and, optionally, other containers. You can use a `ContainerView`_ with a `PropertyCollector`_ method to retrieve data or receive notification of changes. For information about using views with the `PropertyCollector`_ , see the description of `ViewManager`_ .When you invoke the `CreateContainerView`_ method, you specify a managed object instance that provides the starting point for object selection. You can use the following managed objects as the basis of a container view:
   * 
   * `Folder`_
   * 
   * 
   * `Datacenter`_
   * 
   * 
   * `ComputeResource`_
   * 
   * 
   * `ResourcePool`_
   * 
   * 
   * `HostSystem`_
   * 
   * 
   * Once you have created the view, the
   * `view`_
   * list always represents the current configuration of the virtual environment and reflects any subsequent changes that occur.


:extends: vim.view.ManagedObjectView_
:since: `VI API 2.5`_


Attributes
----------
    container (`vim.ManagedEntity`_):
       The Folder, Datacenter, ComputeResource, ResourcePool, or HostSystem instance that provides the objects that the view presents.
    type ([`str`_]):
       An optional list of types to be applied to the set of objects in the view. The list of types indicates objects that are included in the view. If empty, all types are included.
    recursive (`bool`_):
       Whether to include only the immediate children of the container instance, or to include additional objects by following the paths beyond the immediate children.For information about recursive behavior, see the description of `CreateContainerView`_ .


Methods
-------


