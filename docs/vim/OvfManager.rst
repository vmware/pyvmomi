.. _str: https://docs.python.org/2/library/stdtypes.html

.. _vim.Task: ../vim/Task.rst

.. _ImportSpec: ../vim/ImportSpec.rst

.. _VirtualApp: ../vim/VirtualApp.rst

.. _vim.Datastore: ../vim/Datastore.rst

.. _OvfOptionInfo: ../vim/OvfManager/OvfOptionInfo.rst

.. _vim.HostSystem: ../vim/HostSystem.rst

.. _VirtualMachine: ../vim/VirtualMachine.rst

.. _vSphere API 5.1: ../vim/version.rst#vimversionversion8

.. _vSphere API 4.0: ../vim/version.rst#vimversionversion5

.. _vim.ResourcePool: ../vim/ResourcePool.rst

.. _vim.ManagedEntity: ../vim/ManagedEntity.rst

.. _vim.fault.FileFault: ../vim/fault/FileFault.rst

.. _VirtualApp.exportVApp: ../vim/VirtualApp.rst#exportVApp

.. _vim.fault.InvalidState: ../vim/fault/InvalidState.rst

.. _vim.fault.VmConfigFault: ../vim/fault/VmConfigFault.rst

.. _VirtualMachine.exportVm: ../vim/VirtualMachine.rst#exportVm

.. _vim.fault.TaskInProgress: ../vim/fault/TaskInProgress.rst

.. _vim.fault.InvalidDatastore: ../vim/fault/InvalidDatastore.rst

.. _vim.fault.ConcurrentAccess: ../vim/fault/ConcurrentAccess.rst

.. _vim.OvfManager.OvfOptionInfo: ../vim/OvfManager/OvfOptionInfo.rst

.. _vim.OvfManager.ValidateHostParams: ../vim/OvfManager/ValidateHostParams.rst

.. _vim.OvfManager.ValidateHostResult: ../vim/OvfManager/ValidateHostResult.rst

.. _vim.OvfManager.ParseDescriptorResult: ../vim/OvfManager/ParseDescriptorResult.rst

.. _vim.OvfManager.ParseDescriptorParams: ../vim/OvfManager/ParseDescriptorParams.rst

.. _vim.OvfManager.CreateDescriptorResult: ../vim/OvfManager/CreateDescriptorResult.rst

.. _vim.OvfManager.CreateDescriptorParams: ../vim/OvfManager/CreateDescriptorParams.rst

.. _vim.OvfManager.CreateImportSpecResult: ../vim/OvfManager/CreateImportSpecResult.rst

.. _vim.OvfManager.CreateImportSpecParams: ../vim/OvfManager/CreateImportSpecParams.rst


vim.OvfManager
==============
  Service interface to parse and generate OVF descriptors.The purpose of this interface is to make it easier for callers to import VMs and vApps from OVF packages and to export VI packages to OVF. In the following description, the term "client" is used to mean any caller of the interface.This interface only converts between OVF and VI types. To actually import and export entities, use `ResourcePool.importVApp`_ , `VirtualMachine.exportVm`_ and `VirtualApp.exportVApp`_ .ImportFor the import scenario, the typical sequence of events is as follows:The client calls parseDescriptor to obtain information about the OVF descriptor. This typically includes information (such as a list of networks) that must be mapped to VI infrastructure entities.The OVF descriptor is validated against the OVF Specification, and any errors or warnings are returned as part of the ParseResult. For example, the parser might encounter a section marked required that it does not understand, or the XML descriptor might be malformed.The client decides on network mappings, datastore, properties etc. It then calls createImportSpec to obtain the parameters needed to call `ResourcePool.importVApp`_ .If any warnings are present, the client will review these and decide whether to proceed or not. If errors are present, the ImportSpec will be missing, so the client is forced to give up or fix the problems and then try again.The client now calls `ResourcePool.importVApp`_ , passing the ImportSpec as a parameter. This will create the virtual machines and `VirtualApp`_ objects in VI and return locations to which the files of the entity can be uploaded. It also returns a lease that controls the duration of the lock taken on the newly created inventory objects. When all files have been uploaded, the client must release this lease.ExportCreating the OVF descriptor is the last part of exporting an entity to OVF. At this point, the client has already downloaded all files for the entity, optionally compressing and/or chunking them (however, the client may do a "dry run" of creating the descriptor before downloading the files. See `OvfManager.createDescriptor`_ ).In addition to the entity reference itself, information about the choices made on these files is passed to createDescriptor as a list of OvfFile instances.The client must inspect and act upon warnings and errors as previously described.No matter if the export succeeds or fails, the client is responsible for releasing the shared state lock taken on the entity (by `VirtualMaching.exportVm`_ or `VirtualApp.exportVApp`_ ) during the export.Error handlingAll result types contain warning and error lists. Warnings do not cause processing to fail, but the caller (typically, the user of a GUI client) may choose to reject the result based on the warnings issued.Errors cause processing to abort by definition.


:since: `vSphere API 4.0`_


Attributes
----------
    ovfImportOption (`vim.OvfManager.OvfOptionInfo`_):
      privilege: System.View
       Returns an array of `OvfOptionInfo`_ object that specifies what options the server support for modifing/relaxing the OVF import process.
    ovfExportOption (`vim.OvfManager.OvfOptionInfo`_):
      privilege: System.View
       Returns an array of `OvfOptionInfo`_ object that specifies what options the server support for exporting an OVF descriptor.


Methods
-------


ValidateHost(ovfDescriptor, host, vhp):
   Validate that the given OVF can be imported on the host.More specifically, this means whether or not the host supports the virtual hardware required by the OVF descriptor.


  Privilege:
               System.View



  Args:
    ovfDescriptor (`str`_):
       The OVF descriptor to examine.


    host (`vim.HostSystem`_):
       The host to validate against.


    vhp (`vim.OvfManager.ValidateHostParams`_):
       Additional parameters for validateHost, wrapped in a ValidateHostParams instance.




  Returns:
    `vim.OvfManager.ValidateHostResult`_:
         A ValidateResult instance containing any warnings and/or errors from the validation.

  Raises:

    `vim.fault.TaskInProgress`_: 
       if a required managed entity is busy.

    `vim.fault.ConcurrentAccess`_: 
       if a concurrency issue prevents the operation from succeeding.

    `vim.fault.FileFault`_: 
       if there is a generic file error

    `vim.fault.InvalidState`_: 
       if the operation failed due to the current state of the system.


ParseDescriptor(ovfDescriptor, pdp):
   Parse the OVF descriptor and return as much information about it as possible without knowing the host on which it will be imported.Typically, this method is called once without a deploymentOption parameter to obtain the values for the default deployment option. Part of the result is the list of possible deployment options. To obtain the values for a particular deployment option, call this method again, specifying that option.


  Privilege:
               System.View



  Args:
    ovfDescriptor (`str`_):
       The OVF descriptor to examine.


    pdp (`vim.OvfManager.ParseDescriptorParams`_):
       Additional parameters for parseDescriptor, wrapped in an instance of ParseDescriptorParams.




  Returns:
    `vim.OvfManager.ParseDescriptorResult`_:
         The information about the descriptor

  Raises:

    `vim.fault.TaskInProgress`_: 
       if a required managed entity is busy.

    `vim.fault.VmConfigFault`_: 
       if a configuration issue prevents the operation from succeeding. Typically, a more specific subclass is thrown.

    `vim.fault.ConcurrentAccess`_: 
       if a concurrency issue prevents the operation from succeeding.

    `vim.fault.FileFault`_: 
       if there is a generic file error

    `vim.fault.InvalidState`_: 
       if the operation failed due to the current state of the system.


CreateImportSpec(ovfDescriptor, resourcePool, datastore, cisp):
   Validate the OVF descriptor against the hardware supported by the host system. If the validation succeeds, return a result containing:
    * An
    * `ImportSpec`_
    * to use when importing the entity.
    * A list of items to upload (for example disk backing files, ISO images etc.)


  Privilege:
               System.View



  Args:
    ovfDescriptor (`str`_):
       The OVF descriptor of the entity.


    resourcePool (`vim.ResourcePool`_):
       The resource pool to import the entity to. May be a vApp.


    datastore (`vim.Datastore`_):
       The datastore on which to create the inventory objects of the entity, for example "storage1". The privilege Datastore.AllocateSpace is required on the datastore.


    cisp (`vim.OvfManager.CreateImportSpecParams`_):
       Additional parameters to the method, bundled in an instance of CreateImportSpecParams.




  Returns:
    `vim.OvfManager.CreateImportSpecResult`_:
         

  Raises:

    `vim.fault.TaskInProgress`_: 
       if a required managed entity is busy.

    `vim.fault.VmConfigFault`_: 
       if a configuration issue prevents the operation from succeeding. Typically, a more specific subclass is thrown.

    `vim.fault.ConcurrentAccess`_: 
       if a concurrency issue prevents the operation from succeeding.

    `vim.fault.FileFault`_: 
       if there is a generic file error

    `vim.fault.InvalidState`_: 
       if the operation failed due to the current state of the system.

    `vim.fault.InvalidDatastore`_: 
       vim.fault.InvalidDatastore


CreateDescriptor(obj, cdp):
   Create an OVF descriptor for the specified ManagedEntity, which may be a `VirtualMachine`_ or a `VirtualApp`_ .To create the complete OVF descriptor, the client must already have downloaded the files that are part of the entity, because information about these files (compression, chunking, filename etc.) is part of the descriptor.However, these downloads can be quite time-consuming, so if the descriptor for some reason cannot be generated, the client will want to know this before downloading the files.For this reason, the client may do an initial "dry run" with the ovfFiles parameter unset. Default filenames will then be used in the descriptor, and the client can examine any warnings and/or errors before downloading the files.After the final call to this method, client must release the lock on the entity given to it by `VirtualMachine.exportVm`_ or `VirtualApp.exportVApp`_ .


  Privilege:
               System.View



  Args:
    obj (`vim.ManagedEntity`_):
       The entity to export. Supported types are `VirtualMachine`_ and `VirtualApp`_ .


    cdp (`vim.OvfManager.CreateDescriptorParams`_):
       Parameters to the method, bundled in an instance of CreateDescriptorParams.




  Returns:
    `vim.OvfManager.CreateDescriptorResult`_:
         An instance of CreateDescriptorResult

  Raises:

    `vim.fault.TaskInProgress`_: 
       if a required managed entity is busy.

    `vim.fault.VmConfigFault`_: 
       if a configuration issue prevents the operation from succeeding. Typically, a more specific subclass is thrown.

    `vim.fault.ConcurrentAccess`_: 
       if a concurrency issue prevents the operation from succeeding.

    `vim.fault.FileFault`_: 
       if there is a generic file error

    `vim.fault.InvalidState`_: 
       if the operation failed due to the current state of the system.


