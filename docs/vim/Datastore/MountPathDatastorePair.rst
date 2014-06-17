.. _str: https://docs.python.org/2/library/stdtypes.html

.. _path: ../../vim/host/MountInfo.rst#path

.. _HostMountInfo: ../../vim/host/MountInfo.rst

.. _vim.Datastore: ../../vim/Datastore.rst

.. _vSphere API 4.1: ../../vim/version.rst#vimversionversion6

.. _vmodl.DynamicData: ../../vmodl/DynamicData.rst


vim.Datastore.MountPathDatastorePair
====================================
  Contains a mapping of an old mount path and its corresponding resignatured or remounted datastore
:extends: vmodl.DynamicData_
:since: `vSphere API 4.1`_

Attributes:
    oldMountPath (`str`_):

       Old file path where file system volume is mounted, which should be `path`_ value in `HostMountInfo`_ 
    datastore (`vim.Datastore`_):

       The resignatured or remounted datastore corresponding to the oldMountPath
