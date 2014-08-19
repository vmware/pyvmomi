
vim.cluster.DrsVmConfigInfo
===========================
  DRS configuration for a single virtual machine. This makes it possible to override the default behavior for an individual virtual machine.
:extends: vmodl.DynamicData_

Attributes:
    key (`vim.VirtualMachine <vim/VirtualMachine.rst>`_):

       Reference to the virtual machine.
    enabled (`bool <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Flag to indicate whether or not VirtualCenter is allowed to perform any DRS migration or initial placement recommendations for this virtual machine. If this flag is false, the virtual machine is effectively excluded from DRS.If no individual DRS specification exists for a virtual machine, this property defaults to true.
    behavior (`vim.cluster.DrsConfigInfo.DrsBehavior <vim/cluster/DrsConfigInfo/DrsBehavior.rst>`_, optional):

       Specifies the particular DRS behavior for this virtual machine.See `ClusterDrsConfigInfo <vim/cluster/DrsConfigInfo.rst>`_ 
