
vim.DatastoreNamespaceManager
=============================
  The DatastoreNamespaceManager managed object exposes APIs for manipulating top-level directories of datastores which do not support the traditional top-level directory creation.See `topLevelDirectoryCreateSupported <vim/Datastore/Capability.rst#topLevelDirectoryCreateSupported>`_ 


:since: `vSphere API 5.5 <vim/version.rst#vimversionversion9>`_


Attributes
----------


Methods
-------


CreateDirectory(datastore, displayName, policy):
   Creates a top-level directory on the given datastore, using the given user display name hint and opaque storage policy.The optional given display name hint may be used by the underlying storage system for user display purposes, but it may not be relied upon for future directory references.Clients must use the returned stable path for future directory references.See `DeleteDirectory <vim/DatastoreNamespaceManager.rst#DeleteDirectory>`_ 


  Privilege:
               Datastore.Config



  Args:
    datastore (`vim.Datastore <vim/Datastore.rst>`_):
       datastore on which to create a top-level directorySee `DeleteDirectory <vim/DatastoreNamespaceManager.rst#DeleteDirectory>`_ 


    displayName (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):
       display name hint for the directory to createSee `DeleteDirectory <vim/DatastoreNamespaceManager.rst#DeleteDirectory>`_ 


    policy (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):
       opaque storage policy to associate with the directorySee `DeleteDirectory <vim/DatastoreNamespaceManager.rst#DeleteDirectory>`_ 




  Returns:
    `str <https://docs.python.org/2/library/stdtypes.html>`_:
         a stable vmfs path which may be used for future reference of the created directory, of the form/vmfs/volumes/[datastore-uuid]/[directory-uuid]

  Raises:

    `vim.fault.CannotCreateFile <vim/fault/CannotCreateFile.rst>`_: 
       if a general system error occurred while creating directory on the datastoreSee `DeleteDirectory <vim/DatastoreNamespaceManager.rst#DeleteDirectory>`_ 

    `vim.fault.FileAlreadyExists <vim/fault/FileAlreadyExists.rst>`_: 
       if the given directory already existsSee `DeleteDirectory <vim/DatastoreNamespaceManager.rst#DeleteDirectory>`_ 

    `vim.fault.InvalidDatastore <vim/fault/InvalidDatastore.rst>`_: 
       if the given datastore is not supported by the DatastoreNamespaceManageSee `DeleteDirectory <vim/DatastoreNamespaceManager.rst#DeleteDirectory>`_ 


DeleteDirectory(datacenter, datastorePath):
   Deletes the given top-level directory from a datastore.The top-level directory must be a full path of the form/vmfs/volumes/[datastore-uuid]/[directory-uuid]as returned by `CreateDirectory <vim/DatastoreNamespaceManager.rst#CreateDirectory>`_ .See `CreateDirectory <vim/DatastoreNamespaceManager.rst#CreateDirectory>`_ 


  Privilege:
               Datastore.Config



  Args:
    datacenter (`vim.Datacenter <vim/Datacenter.rst>`_, optional):
       The datacenter of the datastore path. Needs to be set when making the call to VC; ignored when the call is made to ESX.See `CreateDirectory <vim/DatastoreNamespaceManager.rst#CreateDirectory>`_ 


    datastorePath (`str <https://docs.python.org/2/library/stdtypes.html>`_):
       Stable vmfs path of the directory to delete.See `CreateDirectory <vim/DatastoreNamespaceManager.rst#CreateDirectory>`_ 




  Returns:
    None
         

  Raises:

    `vim.fault.FileFault <vim/fault/FileFault.rst>`_: 
       if a generic system error happened.See `CreateDirectory <vim/DatastoreNamespaceManager.rst#CreateDirectory>`_ 

    `vim.fault.FileNotFound <vim/fault/FileNotFound.rst>`_: 
       if the given directory can not be foundSee `CreateDirectory <vim/DatastoreNamespaceManager.rst#CreateDirectory>`_ 

    `vim.fault.InvalidDatastore <vim/fault/InvalidDatastore.rst>`_: 
       if the given datastore is not supported by the DatastoreNamespaceManagerSee `CreateDirectory <vim/DatastoreNamespaceManager.rst#CreateDirectory>`_ 

    `vim.fault.InvalidDatastorePath <vim/fault/InvalidDatastorePath.rst>`_: 
       if the given path is not a top-level directorySee `CreateDirectory <vim/DatastoreNamespaceManager.rst#CreateDirectory>`_ 


