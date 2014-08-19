
vim.fault.CannotChangeVsanNodeUuid
==================================
    :extends:

        `vim.fault.VsanFault <vim/fault/VsanFault.rst>`_

  Fault thrown for cases that a VSAN node UUID may not be changed. For example, the VSAN node UUID for a host may not be changed so long as that host is enabled for VSAN.See `UpdateVsan_Task <vim/host/VsanSystem.rst#update>`_ See `ReconfigureComputeResource_Task <vim/ComputeResource.rst#reconfigureEx>`_ 

Attributes:




