.. _str: https://docs.python.org/2/library/stdtypes.html

.. _vim.Task: ../../vim/Task.rst

.. _FileQuery: ../../vim/host/DatastoreBrowser/Query.rst

.. _vim.Datastore: ../../vim/Datastore.rst

.. _vim.fault.FileFault: ../../vim/fault/FileFault.rst

.. _vim.fault.FileNotFound: ../../vim/fault/FileNotFound.rst

.. _vim.fault.InvalidDatastore: ../../vim/fault/InvalidDatastore.rst

.. _vim.fault.CannotDeleteFile: ../../vim/fault/CannotDeleteFile.rst

.. _vmodl.fault.InvalidArgument: ../../vmodl/fault/InvalidArgument.rst

.. _vim.host.DatastoreBrowser.Query: ../../vim/host/DatastoreBrowser/Query.rst

.. _vim.host.DatastoreBrowser.SearchSpec: ../../vim/host/DatastoreBrowser/SearchSpec.rst

.. _vim.host.DatastoreBrowser.SearchResults: ../../vim/host/DatastoreBrowser/SearchResults.rst


vim.host.DatastoreBrowser
=========================
  The DatastoreBrowser managed object type provides access to the contents of one or more datastores. The items in a datastore are files that contain configuration, virtual disk, and the other data associated with a virtual machine.Although datastores may often be implemented using a traditional file system, a full interface to a file system is not provided here. Instead, specialized access for virtual machine files is provided. A datastore implementation may completely hide the file directory structure.The intent is to provide functionality analogous to a file chooser in a user interface.Files on datastores do not have independent permissions through this API. Instead, the permissions for all the files on a datastore derive from the datastore object itself. It is not possible to change individual file permissions as the user browsing the datastore may not necessarily be a recognized user from the point of view of the host changing the permission. This occurs if the user browsing the datastore is doing so through the VirtualCenter management server.The DatastoreBrowser provides many ways to customize a search for files. A search can be customized by specifying the types of files to be searched, search criteria specific to a file type, and the amount of detail about each file. The most basic queries only use file details and are efficient with limited side effects. For these queries, file metadata details can be optionally retrieved, but the files themselves are opened and their contents examined. As a result, these files are not necessarily validated.More complicated queries can be formed by specifying the specific types of files to be searched, the parameters to filter for each type, and the desired level of detail about each file. This method of searching for files is convenient because it allows additional data about the virtual machine component to be retrieved. In addition, certain validation checks can be performed on matched files as an inherent part of the details collection process. However, gathering extra details or the use of type specific filters can sometimes only be implemented by examining the contents of a file. As a result, the use of these conveniences comes with the cost of additional latency in the request and possible side effects on the system as a whole.The DatastoreBrowser is referenced from various objects, including from `Datastore`_ , `ComputeResource`_ , `HostSystem`_ and `VirtualMachine`_ . Depending on which object is used, there are different requirements for the accessibility of the browsed datastore from the host (or hosts) associated with the object:
   * When referenced from the target
   * `Datastore`_
   * , it needs to be accessible from at least one host on which the datastore is mounted. See
   * `accessible`_
   * .
   * When referenced from a
   * `ComputeResource`_
   * , the target datastore needs to be accessible from at least one host in the ComputeResource. See
   * `accessible`_
   * .
   * When referenced from a
   * `HostSystem`_
   * , the target datastore needs to be accessible from that host. See
   * `accessible`_
   * .
   * When referenced from a
   * `VirtualMachine`_
   * , the target datastore needs to be accessible from the host on which the virtual machine is registered. See
   * `accessible`_
   * .
   * See FileInfo




Attributes
----------
    datastore ([`vim.Datastore`_]):
      privilege: System.View
       Set of datastores that can be searched on this DatastoreBrowser.The list of datastores available to browse on this DatastoreBrowser is contextual information that depends on the object being browsed. If the host is being browsed, the host's datastores are used. If the Datacenter is being browsed, the Datacenter's list of datastores is used.
    supportedType ([`vim.host.DatastoreBrowser.Query`_]):
       The list of supported file types. The supported file types are represented as items in this list. For each supported file type, there is an object in the list whose dynamic type is one of the types derived from the `FileQuery`_ data object type. In general, the properties in this query type are not set.Use the Query of the desired file type in the SearchSpec.query to indicate the desired file types.This property is used by clients to determine what kinds of file types are supported. Clients should consult this list to avoid querying for types of virtual machine components that are not supported.


Methods
-------


SearchDatastore(datastorePath, searchSpec):
   Returns the information for the files that match the given search criteria as a SearchResults object. Searches only the folder specified by the datastore path. The Datastore.Browse privilege must be held on the datastore identified by the datastore path.


  Privilege:
               dynamic



  Args:
    datastorePath (`str`_):


    searchSpec (`vim.host.DatastoreBrowser.SearchSpec`_, optional):




  Returns:
     `vim.Task`_:
         

  Raises:

    `vim.fault.InvalidDatastore`_: 
       if the operation cannot be performed on the target datastores. The server can throw InvalidDatastorePath to indicate a malformed datastorePath, or InaccessibleDatastore to indicate inaccessibility of the datastore.

    `vim.fault.FileFault`_: 
       vim.fault.FileFault

    `vmodl.fault.InvalidArgument`_: 
       if the SearchSpec contains duplicate file types.

    `vim.fault.FileNotFound`_: 
       if the file or folder specified by datastorePath is not found.


SearchDatastoreSubFolders(datastorePath, searchSpec):
   Returns the information for the files that match the given search criteria as a SearchResults[] object. Searches the folder specified by the datastore path and all subfolders. The Datastore.Browse privilege must be held on the datastore identified by the datastore path.


  Privilege:
               dynamic



  Args:
    datastorePath (`str`_):


    searchSpec (`vim.host.DatastoreBrowser.SearchSpec`_, optional):




  Returns:
     `vim.Task`_:
         

  Raises:

    `vim.fault.InvalidDatastore`_: 
       if the operation cannot be performed on the target datastores. Typically, a specific subclass of this exception is thrown.

    `vim.fault.FileFault`_: 
       vim.fault.FileFault

    `vmodl.fault.InvalidArgument`_: 
       if the SearchSpec contains duplicate file types.

    `vim.fault.FileNotFound`_: 
       if the file or folder specified by datastorePath is not found.


DeleteFile(datastorePath):
   Deletes the specified files from the datastore. If a valid virtual disk file is specified, then all the components of the virtual disk are deleted.


  Privilege:
               Datastore.DeleteFile



  Args:
    datastorePath (`str`_):




  Returns:
    None
         

  Raises:

    `vim.fault.InvalidDatastore`_: 
       if the operation cannot be performed on the target datastores. Typically, a specific subclass of this exception is thrown.

    `vim.fault.FileFault`_: 
       vim.fault.FileFault

    `vim.fault.FileNotFound`_: 
       if the file or folder specified by datastorePath is not found.

    `vim.fault.CannotDeleteFile`_: 
       if the delete operation on the file fails.

    `vmodl.fault.InvalidArgument`_: 
       if fileInfo is not a valid FileInfo type.


