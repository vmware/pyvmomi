.. _vim.Task: ../../vim/Task.rst

.. _lacpApiVersion: ../../vim/dvs/VmwareDistributedVirtualSwitch/ConfigInfo.rst#lacpApiVersion

.. _vSphere API 4.0: ../../vim/version.rst#vimversionversion5

.. _vSphere API 5.5: ../../vim/version.rst#vimversionversion9

.. _vim.fault.DvsFault: ../../vim/fault/DvsFault.rst

.. _vmodl.fault.NotSupported: ../../vmodl/fault/NotSupported.rst

.. _vim.DistributedVirtualSwitch: ../../vim/DistributedVirtualSwitch.rst

.. _vim.dvs.VmwareDistributedVirtualSwitch.LacpGroupSpec: ../../vim/dvs/VmwareDistributedVirtualSwitch/LacpGroupSpec.rst


vim.dvs.VmwareDistributedVirtualSwitch
======================================
  The `VmwareDistributedVirtualSwitch`_ managed object is the VMware implementation of a distributed virtual switch. The functionality listed here is for a VMware distributed virtual switch only.When you use a VMware distributed virtual switch, you can perform backup and restore operations on the VMware switch. You can also perform rollback operations on the switch and on portgroups associated with the VMware switch. See the description for the following methods:
   * `DVSManagerExportEntity_Task`_
   * `DVSManagerImportEntity_Task`_
   * `DVSRollback_Task`_
   * `DVPortgroupRollback_Task`_


:extends: vim.DistributedVirtualSwitch_
:since: `vSphere API 4.0`_


Attributes
----------


Methods
-------


UpdateDVSLacpGroupConfig(lacpGroupSpec):
   Update Link Aggregation Control Protocol groups. It can be called if the value of `lacpApiVersion`_ is LacpApiVersion#multipleLag else an exception ConflictingConfiguration will be thrown.
  since: `vSphere API 5.5`_


  Privilege:
               DVSwitch.Modify



  Args:
    lacpGroupSpec (`vim.dvs.VmwareDistributedVirtualSwitch.LacpGroupSpec`_):
       The Link Aggregation Control Protocol groups to be configured.




  Returns:
     `vim.Task`_:
         

  Raises:

    `vim.fault.DvsFault`_: 
       if operation fails on any host or if there are other update failures.

    `vmodl.fault.NotSupported`_: 
       if multiple Link Aggregation Control Protocol is not supported on the switch.


