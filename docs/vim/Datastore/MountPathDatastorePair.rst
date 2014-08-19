
vim.Datastore.MountPathDatastorePair
====================================
  Contains a mapping of an old mount path and its corresponding resignatured or remounted datastore
:extends: vmodl.DynamicData_
:since: `vSphere API 4.1 <vim/version.rst#vimversionversion6>`_

Attributes:
    oldMountPath (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       Old file path where file system volume is mounted, which should be `path <vim/host/MountInfo.rst#path>`_ value in `HostMountInfo <vim/host/MountInfo.rst>`_ 
    datastore (`vim.Datastore <vim/Datastore.rst>`_):

       The resignatured or remounted datastore corresponding to the oldMountPath
