.. _str: https://docs.python.org/2/library/stdtypes.html

.. _vmodl.DynamicData: ../../vmodl/DynamicData.rst


vim.vm.FileInfo
===============
  The FileInfo data object type contains the locations of virtual machine files other than the virtual disk files. The configurable parameters are all in the FileInfo object.The object also contains a FileLayout object that returns a complete list of additional files that makes up the virtual machine configuration. This is a read-only structure and is returned when the configuration is read. This is ignored during configuration and can be left out.
:extends: vmodl.DynamicData_

Attributes:
    vmPathName (`str`_, optional):

       Path name to the configuration file for the virtual machine, e.g., the .vmx file. This also implicitly defines the configuration directory.
    snapshotDirectory (`str`_, optional):

       Path name of the directory that holds suspend and snapshot files belonging to the virtual machine. Prior to vSphere 5.0, this directory also holds snapshot redo files. Starting with vSphere 5.0, the redo files will stay in the same directory as the snapshotted disk, thus this directory will no longer hold the snapshot redo files.This path name defaults to the same directory as the configuration file.ESX Server requires this to indicate a VMFS volume or NAS volume (for ESX Server 3). In case the configuration file is not stored on VMFS or NAS, this property must be set explicitly.
    suspendDirectory (`str`_, optional):

       Some products allow the suspend directory to be different than the snapshot directory. On products where this is not possible, setting of this property is ignored.
    logDirectory (`str`_, optional):

       Directory to store the log files for the virtual machine. If not specified, this defaults to the same directory as the configuration file,
