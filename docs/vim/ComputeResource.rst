.. _bool: https://docs.python.org/2/library/stdtypes.html

.. _vim.Task: ../vim/Task.rst

.. _VI API 2.5: ../vim/version.rst#vimversionversion2

.. _vim.Network: ../vim/Network.rst

.. _vim.Datastore: ../vim/Datastore.rst

.. _vim.HostSystem: ../vim/HostSystem.rst

.. _vim.ResourcePool: ../vim/ResourcePool.rst

.. _vim.ManagedEntity: ../vim/ManagedEntity.rst

.. _ClusterConfigInfoEx: ../vim/cluster/ConfigInfoEx.rst

.. _vim.EnvironmentBrowser: ../vim/EnvironmentBrowser.rst

.. _vim.ComputeResource.Summary: ../vim/ComputeResource/Summary.rst

.. _vim.ComputeResource.ConfigInfo: ../vim/ComputeResource/ConfigInfo.rst

.. _vim.ComputeResource.ConfigSpec: ../vim/ComputeResource/ConfigSpec.rst

.. _vim.fault.CannotDisableDrsOnClustersWithVApps: ../vim/fault/CannotDisableDrsOnClustersWithVApps.rst


vim.ComputeResource
===================
  Represents a set of physical compute resources for a set of virtual machines.The base type `ComputeResource`_ , when instantiated by calling `AddStandaloneHost_Task`_ , represents a single host. The subclass `ClusterComputeResource`_ represents a cluster of hosts and adds distributed management features such as availability and resource scheduling.A `ComputeResource`_ always has a root `ResourcePool`_ associated with it. Certain types of clusters such as those with VMware DRS enabled and standalone hosts (ESX Server 3) support the creation of `ResourcePool`_ hierarchies.


:extends: vim.ManagedEntity_


Attributes
----------
    resourcePool (`vim.ResourcePool`_):
      privilege: System.View
       Reference to root resource pool.
    host (`vim.HostSystem`_):
      privilege: System.View
       List of hosts that are part of this compute resource. If the compute resource is a standalone type, then this list contains just one element.
    datastore (`vim.Datastore`_):
      privilege: System.View
       The datastore property is the subset of datastore objects in the datacenter available in this ComputeResource.This property is computed as the aggregate set of datastores available from all the hosts that are part of this compute resource.
    network (`vim.Network`_):
      privilege: System.View
       The subset of network objects available in the datacenter that is available in this ComputeResource.This property is computed as the aggregate set of networks available from all the hosts that are part of this compute resource.
    summary (`vim.ComputeResource.Summary`_):
       Basic runtime information about a compute resource. This information is used on summary screens and in list views.
    environmentBrowser (`vim.EnvironmentBrowser`_):
      privilege: System.View
       The environment browser object that identifies the environments that are supported on this compute resource.
    configurationEx (`vim.ComputeResource.ConfigInfo`_):
       Configuration of the compute resource; applies to both standalone hosts and clusters. For a cluster this property will return a `ClusterConfigInfoEx`_ object.


Methods
-------


ReconfigureComputeResource(spec, modify):
   Change the compute resource configuration.
  since: `VI API 2.5`_


  Privilege:
               Host.Inventory.EditCluster



  Args:
    spec (`vim.ComputeResource.ConfigSpec`_):
       A set of configuration changes to apply to the compute resource. The specification can be a complete set of changes or a partial set of changes, applied incrementally. When invoking reconfigureEx on a cluster, this argument may be a `ClusterConfigSpecEx`_ object.


    modify (`bool`_):
       Flag to specify whether the specification ("spec") should be applied incrementally. If "modify" is false and the operation succeeds, then the configuration of the cluster matches the specification exactly; in this case any unset portions of the specification will result in unset or default portions of the configuration.




  Returns:
     `vim.Task`_:
         

  Raises:

    `vim.fault.CannotDisableDrsOnClustersWithVApps`_: 
       If DRS is being disabled and the cluster contains one or more vApps.


