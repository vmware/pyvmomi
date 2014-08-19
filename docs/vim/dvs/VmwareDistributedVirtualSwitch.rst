
vim.dvs.VmwareDistributedVirtualSwitch
======================================
  The `VmwareDistributedVirtualSwitch <vim/dvs/VmwareDistributedVirtualSwitch.rst>`_ managed object is the VMware implementation of a distributed virtual switch. The functionality listed here is for a VMware distributed virtual switch only.When you use a VMware distributed virtual switch, you can perform backup and restore operations on the VMware switch. You can also perform rollback operations on the switch and on portgroups associated with the VMware switch. See the description for the following methods:
   * `DVSManagerExportEntity_Task <vim/dvs/DistributedVirtualSwitchManager.rst#exportEntity>`_
   * `DVSManagerImportEntity_Task <vim/dvs/DistributedVirtualSwitchManager.rst#importEntity>`_
   * `DVSRollback_Task <vim/DistributedVirtualSwitch.rst#rollback>`_
   * `DVPortgroupRollback_Task <vim/dvs/DistributedVirtualPortgroup.rst#rollback>`_


:extends: vim.DistributedVirtualSwitch_
:since: `vSphere API 4.0 <vim/version.rst#vimversionversion5>`_


Attributes
----------


Methods
-------


UpdateDVSLacpGroupConfig(lacpGroupSpec):
   Update Link Aggregation Control Protocol groups. It can be called if the value of `lacpApiVersion <vim/dvs/VmwareDistributedVirtualSwitch/ConfigInfo.rst#lacpApiVersion>`_ is LacpApiVersion#multipleLag else an exception ConflictingConfiguration will be thrown.
  since: `vSphere API 5.5 <vim/version.rst#vimversionversion9>`_


  Privilege:
               DVSwitch.Modify



  Args:
    lacpGroupSpec (`vim.dvs.VmwareDistributedVirtualSwitch.LacpGroupSpec <vim/dvs/VmwareDistributedVirtualSwitch/LacpGroupSpec.rst>`_):
       The Link Aggregation Control Protocol groups to be configured.




  Returns:
     `vim.Task <vim/Task.rst>`_:
         

  Raises:

    `vim.fault.DvsFault <vim/fault/DvsFault.rst>`_: 
       if operation fails on any host or if there are other update failures.

    `vmodl.fault.NotSupported <vmodl/fault/NotSupported.rst>`_: 
       if multiple Link Aggregation Control Protocol is not supported on the switch.


