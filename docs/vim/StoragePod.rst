.. _vim.Task: ../vim/Task.rst

.. _vim.Folder: ../vim/Folder.rst

.. _vSphere API 5.0: ../vim/version.rst#vimversionversion7

.. _vim.StoragePod.Summary: ../vim/StoragePod/Summary.rst

.. _vim.StorageResourceManager.PodStorageDrsEntry: ../vim/StorageResourceManager/PodStorageDrsEntry.rst


vim.StoragePod
==============
  The `StoragePod`_ data object aggregates the storage resources of associated `Datastore`_ objects into a single storage resource for use by virtual machines. The storage services such as Storage DRS (Distributed Resource Scheduling), enhance the utility of the storage pod.Use the `Folder`_ . `CreateStoragePod`_ method to create an instance of this object.


:extends: vim.Folder_
:since: `vSphere API 5.0`_


Attributes
----------
    summary (`vim.StoragePod.Summary`_):
      privilege: System.View
       Storage pod summary.
    podStorageDrsEntry (`vim.StorageResourceManager.PodStorageDrsEntry`_):
      privilege: System.Read
       Storage DRS related attributes of the Storage Pod.


Methods
-------


