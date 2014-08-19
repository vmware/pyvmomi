
vim.OvfManager.OvfFile
======================
  Represents a file that the caller has downloaded and stored somewhere appropriate.An instance of this class is used to tell OvfManager about the choices the caller made about a file. This information is needed when the OVF descriptor is generated with createDescriptor.
:extends: vmodl.DynamicData_
:since: `vSphere API 4.0 <vim/version.rst#vimversionversion5>`_

Attributes:
    deviceId (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       The ID of the device backed by this file. This ID uniquely identifies the device within the entity hierarchy.The caller will have received this along with the URL needed to download the file (this is handled by another service interface).
    path (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       The path chosen by the caller for this file. This path becomes the value of the "href" attribute of the corresponding "File" element in the OVF descriptor.This path must be relative to the path chosen for the OVF descriptor. This implies that the caller must decide in advance on the path to which it will write the OVF descriptor, once it is returned.The folder separator must be "/" (forward slash).The path must not begin with a slash - ie. it must not be an absolute path.
    compressionMethod (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       The compression method the caller chose to employ for this file.
    chunkSize (`long <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       The chunksize chosen by the caller.When using chunking, the caller must adhere to the method described in the OVF specification.
    size (`long <https://docs.python.org/2/library/stdtypes.html>`_):

       The file size, as observed by the caller during download.
    capacity (`long <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       The capacity of the disk backed by this file. This should only be set if the device backed by this file is a disk. This value will be written in the "capacity" attribute of the corresponding "Disk" element in the OVF descriptor.Note that the "capacity" attribute is normally set to the capacity of the corresponding `VirtualDisk <vim/vm/device/VirtualDisk.rst>`_ . Setting this variable overrides the capacity from the VirtualDisk.
    populatedSize (`long <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       The populated size of the disk backed by this file. This should only be set if the device backed by this file is a disk. This value will be written in the "populatedSize" attribute of the corresponding "Disk" element in the OVF descriptor.
