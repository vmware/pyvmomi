
vim.cluster.DrsVmConfigSpec
===========================
  Updates the per-virtual-machine DRS configuration.To update the DRS configuration of a virtual machine, a copy of this object is included in the `ClusterConfigSpecEx <vim/cluster/ConfigSpecEx.rst>`_ object passed to the method `ReconfigureComputeResource_Task <vim/ComputeResource.rst#reconfigureEx>`_ .IfreconfigureExis used to incrementally update the cluster configuration (i.e., the parametermodifyis true), then three operations are provided for updating the DRS configuration for a virtual machine. These operations are listed below (see `ArrayUpdateSpec <vim/option/ArrayUpdateSpec.rst>`_ for more information on these operations).
   * add: add a configuration for the virtual machine, overwritting the existing configuration if one exists
   * edit: incrmentally update the existing configuration; an existing configuration must exist
   * remove: remove the existing configuration; an existing configuration must exist
   * If, instead, this method is used to overwrite the cluster configuration (i.e., the parameter
   * modify
   * is false) thereby creating a new configuration, only the add operation is allowed. In this case,
   * add
   * creates a DRS configuration for a virtual machine in the new cluster configuration.
:extends: vim.option.ArrayUpdateSpec_

Attributes:
    info (`vim.cluster.DrsVmConfigInfo <vim/cluster/DrsVmConfigInfo.rst>`_, optional):

