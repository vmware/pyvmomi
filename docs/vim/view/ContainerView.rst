
vim.view.ContainerView
======================
  The `ContainerView <vim/view/ContainerView.rst>`_ managed object provides a means of monitoring the contents of a single container and, optionally, other containers. You can use a `ContainerView <vim/view/ContainerView.rst>`_ with a `PropertyCollector <vmodl/query/PropertyCollector.rst>`_ method to retrieve data or receive notification of changes. For information about using views with the `PropertyCollector <vmodl/query/PropertyCollector.rst>`_ , see the description of `ViewManager <vim/view/ViewManager.rst>`_ .When you invoke the `CreateContainerView <vim/view/ViewManager.rst#createContainerView>`_ method, you specify a managed object instance that provides the starting point for object selection. You can use the following managed objects as the basis of a container view:
   * 
   * `Folder <vim/Folder.rst>`_
   * 
   * 
   * `Datacenter <vim/Datacenter.rst>`_
   * 
   * 
   * `ComputeResource <vim/ComputeResource.rst>`_
   * 
   * 
   * `ResourcePool <vim/ResourcePool.rst>`_
   * 
   * 
   * `HostSystem <vim/HostSystem.rst>`_
   * 
   * 
   * Once you have created the view, the
   * `view <vim/view/ManagedObjectView.rst#view>`_
   * list always represents the current configuration of the virtual environment and reflects any subsequent changes that occur.


:extends: vim.view.ManagedObjectView_
:since: `VI API 2.5 <vim/version.rst#vimversionversion2>`_


Attributes
----------
    container (`vim.ManagedEntity <vim/ManagedEntity.rst>`_):
       The Folder, Datacenter, ComputeResource, ResourcePool, or HostSystem instance that provides the objects that the view presents.
    type ([`str <https://docs.python.org/2/library/stdtypes.html>`_]):
       An optional list of types to be applied to the set of objects in the view. The list of types indicates objects that are included in the view. If empty, all types are included.
    recursive (`bool <https://docs.python.org/2/library/stdtypes.html>`_):
       Whether to include only the immediate children of the container instance, or to include additional objects by following the paths beyond the immediate children.For information about recursive behavior, see the description of `CreateContainerView <vim/view/ViewManager.rst#createContainerView>`_ .


Methods
-------


