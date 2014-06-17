.. _bool: https://docs.python.org/2/library/stdtypes.html

.. _vmodl.DynamicData: ../../vmodl/DynamicData.rst

.. _vim.VirtualMachine: ../../vim/VirtualMachine.rst

.. _ClusterDrsConfigInfo: ../../vim/cluster/DrsConfigInfo.rst

.. _vim.cluster.DrsConfigInfo.DrsBehavior: ../../vim/cluster/DrsConfigInfo/DrsBehavior.rst


vim.cluster.DrsVmConfigInfo
===========================
  DRS configuration for a single virtual machine. This makes it possible to override the default behavior for an individual virtual machine.
:extends: vmodl.DynamicData_

Attributes:
    key (`vim.VirtualMachine`_):

       Reference to the virtual machine.
    enabled (`bool`_, optional):

       Flag to indicate whether or not VirtualCenter is allowed to perform any DRS migration or initial placement recommendations for this virtual machine. If this flag is false, the virtual machine is effectively excluded from DRS.If no individual DRS specification exists for a virtual machine, this property defaults to true.
    behavior (`vim.cluster.DrsConfigInfo.DrsBehavior`_, optional):

       Specifies the particular DRS behavior for this virtual machine.See `ClusterDrsConfigInfo`_ 
