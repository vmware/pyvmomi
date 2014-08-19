
vim.StoragePod
==============
  The `StoragePod <vim/StoragePod.rst>`_ data object aggregates the storage resources of associated `Datastore <vim/Datastore.rst>`_ objects into a single storage resource for use by virtual machines. The storage services such as Storage DRS (Distributed Resource Scheduling), enhance the utility of the storage pod.Use the `Folder <vim/Folder.rst>`_ . `CreateStoragePod <vim/Folder.rst#createStoragePod>`_ method to create an instance of this object.


:extends: vim.Folder_
:since: `vSphere API 5.0 <vim/version.rst#vimversionversion7>`_


Attributes
----------
    summary (`vim.StoragePod.Summary <vim/StoragePod/Summary.rst>`_):
      privilege: System.View
       Storage pod summary.
    podStorageDrsEntry (`vim.StorageResourceManager.PodStorageDrsEntry <vim/StorageResourceManager/PodStorageDrsEntry.rst>`_):
      privilege: System.Read
       Storage DRS related attributes of the Storage Pod.


Methods
-------


