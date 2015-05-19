.. _str: https://docs.python.org/2/library/stdtypes.html

.. _uuid: ../../vim/host/ScsiLun.rst#uuid

.. _vim.Task: ../../vim/Task.rst

.. _HostScsiDisk: ../../vim/host/ScsiDisk.rst

.. _vim.fault.NotFound: ../../vim/fault/NotFound.rst

.. _vmodl.fault.NotSupported: ../../vmodl/fault/NotSupported.rst

.. _vim.fault.HostConfigFault: ../../vim/fault/HostConfigFault.rst

.. _vmodl.fault.InvalidArgument: ../../vmodl/fault/InvalidArgument.rst

.. _vim.host.ScsiDisk.Partition: ../../vim/host/ScsiDisk/Partition.rst

.. _vim.host.DiagnosticPartition: ../../vim/host/DiagnosticPartition.rst

.. _vim.host.DiagnosticPartition.CreateSpec: ../../vim/host/DiagnosticPartition/CreateSpec.rst

.. _vim.host.DiagnosticPartition.CreateOption: ../../vim/host/DiagnosticPartition/CreateOption.rst

.. _vim.host.DiagnosticPartition.CreateDescription: ../../vim/host/DiagnosticPartition/CreateDescription.rst


vim.host.DiagnosticSystem
=========================
  The DiagnosticSystem managed object is used to configure the diagnostic mechanisms specific to the host. The DiagnosticSystem interface supports the following concepts:
   * Notion of an active diagnostic partition that is selected from a set of available partitions.
   * Ability to create a diagnostic partition that gets added to the list of available partitions and could be made active.
   * 




Attributes
----------
    activePartition (`vim.host.DiagnosticPartition`_):
       The currently active diagnostic partition.


Methods
-------


QueryAvailablePartition():
   Retrieves a list of available diagnostic partitions. The server will provide the list in order of preference. In general, local diagnostic partitions are better than shared diagnostic partitions because of the impossibility of multiple servers sharing the same partition. The most preferred diagnostic partition will be first in the array.


  Privilege:
               Host.Config.Storage



  Args:


  Returns:
    [`vim.host.DiagnosticPartition`_]:
         

  Raises:

    `vim.fault.HostConfigFault`_: 
       on some internal failure while setting the active partition.

    `vmodl.fault.NotSupported`_: 
       if the host is not an ESX Server.


SelectActivePartition(partition):
   Changes the active diagnostic partition to a different partition. Setting a NULL partition will result in unsetting the diagnostic partition.


  Privilege:
               Host.Config.Storage



  Args:
    partition (`vim.host.ScsiDisk.Partition`_, optional):




  Returns:
    None
         

  Raises:

    `vim.fault.NotFound`_: 
       if the diagnostic partition does not exist.

    `vim.fault.HostConfigFault`_: 
       on some internal failure while selecting the active partition.

    `vmodl.fault.NotSupported`_: 
       if the host is not an ESX Server.

    `vmodl.fault.InvalidArgument`_: 
       if the partition is not a diagnostic partition.


QueryPartitionCreateOptions(storageType, diagnosticType):
   Retrieves a list of disks that can be used to contain a diagnostic partition. This list will contain disks that have sufficient space to contain a diagnostic partition of the specific type.The choices will be returned in the order that is most preferable as determined by the system.


  Privilege:
               Host.Config.Storage



  Args:
    storageType (`str`_):


    diagnosticType (`str`_):




  Returns:
    [`vim.host.DiagnosticPartition.CreateOption`_]:
         

  Raises:

    `vim.fault.HostConfigFault`_: 
       on some internal failure while querying the create options.

    `vmodl.fault.NotSupported`_: 
       if the host is not an ESX Server.

    `vmodl.fault.InvalidArgument`_: 
       if an invalid storage type is specified.


QueryPartitionCreateDesc(diskUuid, diagnosticType):
   For a disk, query for the diagnostic partition creation description. The description details how the diagnostic partition will be created on the disk and provides a creation specification that is needed to invoke the create operation.See `HostScsiDisk`_ See `uuid`_ 


  Privilege:
               Host.Config.Storage



  Args:
    diskUuid (`str`_):
       See `HostScsiDisk`_ See `uuid`_ 


    diagnosticType (`str`_):
       See `HostScsiDisk`_ See `uuid`_ 




  Returns:
    `vim.host.DiagnosticPartition.CreateDescription`_:
         

  Raises:

    `vim.fault.NotFound`_: 
       if the specified disk cannot be found.See `HostScsiDisk`_ See `uuid`_ 

    `vim.fault.HostConfigFault`_: 
       on some internal failure while trying to query information about the disk.See `HostScsiDisk`_ See `uuid`_ 

    `vmodl.fault.NotSupported`_: 
       if the host is not an ESX Server.See `HostScsiDisk`_ See `uuid`_ 

    `vmodl.fault.InvalidArgument`_: 
       if an invalid storage type is specified or the specified disk is unable to accommodate a new diagnostic partition.See `HostScsiDisk`_ See `uuid`_ 


CreateDiagnosticPartition(spec):
   Creates a diagnostic partition according to the provided create specification. On success, this method will create the partition and make the partition the active diagnostic partition if specified. On failure, the diagnostic partition may exist but may not be active if the partition was supposed to be made active.


  Privilege:
               Host.Config.Storage



  Args:
    spec (`vim.host.DiagnosticPartition.CreateSpec`_):




  Returns:
    None
         

  Raises:

    `vim.fault.NotFound`_: 
       if the specified disk cannot be found.

    `vim.fault.HostConfigFault`_: 
       on some internal failure while trying to create the diagnostic partition or to activate the diagnostic partition.

    `vmodl.fault.NotSupported`_: 
       if the host is not an ESX Server.

    `vmodl.fault.InvalidArgument`_: 
       if an invalid storage type is specified or the specified disk is unable to accommodate a new diagnostic partition.


