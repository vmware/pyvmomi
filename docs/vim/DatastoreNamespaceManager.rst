.. _str: https://docs.python.org/2/library/stdtypes.html

.. _vim.Task: ../vim/Task.rst

.. _vim.Datastore: ../vim/Datastore.rst

.. _vim.Datacenter: ../vim/Datacenter.rst

.. _DeleteDirectory: ../vim/DatastoreNamespaceManager.rst#DeleteDirectory

.. _vSphere API 5.5: ../vim/version.rst#vimversionversion9

.. _CreateDirectory: ../vim/DatastoreNamespaceManager.rst#CreateDirectory

.. _vim.fault.FileFault: ../vim/fault/FileFault.rst

.. _vim.fault.FileNotFound: ../vim/fault/FileNotFound.rst

.. _vim.fault.InvalidDatastore: ../vim/fault/InvalidDatastore.rst

.. _vim.fault.CannotCreateFile: ../vim/fault/CannotCreateFile.rst

.. _vim.fault.FileAlreadyExists: ../vim/fault/FileAlreadyExists.rst

.. _vim.fault.InvalidDatastorePath: ../vim/fault/InvalidDatastorePath.rst


vim.DatastoreNamespaceManager
=============================
  The DatastoreNamespaceManager managed object exposes APIs for manipulating top-level directories of datastores which do not support the traditional top-level directory creation.See `topLevelDirectoryCreateSupported`_ 


:since: `vSphere API 5.5`_


Attributes
----------


Methods
-------


CreateDirectory(datastore, displayName, policy):
   Creates a top-level directory on the given datastore, using the given user display name hint and opaque storage policy.The optional given display name hint may be used by the underlying storage system for user display purposes, but it may not be relied upon for future directory references.Clients must use the returned stable path for future directory references.See `DeleteDirectory`_ 


  Privilege:
               Datastore.Config



  Args:
    datastore (`vim.Datastore`_):
       datastore on which to create a top-level directorySee `DeleteDirectory`_ 


    displayName (`str`_, optional):
       display name hint for the directory to createSee `DeleteDirectory`_ 


    policy (`str`_, optional):
       opaque storage policy to associate with the directorySee `DeleteDirectory`_ 




  Returns:
    `str`_:
         a stable vmfs path which may be used for future reference of the created directory, of the form/vmfs/volumes/[datastore-uuid]/[directory-uuid]

  Raises:

    `vim.fault.CannotCreateFile`_: 
       if a general system error occurred while creating directory on the datastoreSee `DeleteDirectory`_ 

    `vim.fault.FileAlreadyExists`_: 
       if the given directory already existsSee `DeleteDirectory`_ 

    `vim.fault.InvalidDatastore`_: 
       if the given datastore is not supported by the DatastoreNamespaceManageSee `DeleteDirectory`_ 


DeleteDirectory(datacenter, datastorePath):
   Deletes the given top-level directory from a datastore.The top-level directory must be a full path of the form/vmfs/volumes/[datastore-uuid]/[directory-uuid]as returned by `CreateDirectory`_ .See `CreateDirectory`_ 


  Privilege:
               Datastore.Config



  Args:
    datacenter (`vim.Datacenter`_, optional):
       The datacenter of the datastore path. Needs to be set when making the call to VC; ignored when the call is made to ESX.See `CreateDirectory`_ 


    datastorePath (`str`_):
       Stable vmfs path of the directory to delete.See `CreateDirectory`_ 




  Returns:
    None
         

  Raises:

    `vim.fault.FileFault`_: 
       if a generic system error happened.See `CreateDirectory`_ 

    `vim.fault.FileNotFound`_: 
       if the given directory can not be foundSee `CreateDirectory`_ 

    `vim.fault.InvalidDatastore`_: 
       if the given datastore is not supported by the DatastoreNamespaceManagerSee `CreateDirectory`_ 

    `vim.fault.InvalidDatastorePath`_: 
       if the given path is not a top-level directorySee `CreateDirectory`_ 


