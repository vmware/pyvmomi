
vim.vm.device.VirtualDevice.FileBackingInfo
===========================================
   `VirtualDeviceFileBackingInfo <vim/vm/device/VirtualDevice/FileBackingInfo.rst>`_ is a data object type for information about file backing for a device in a virtual machine.
:extends: vim.vm.device.VirtualDevice.BackingInfo_

Attributes:
    fileName (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       Filename for the host file used in this backing.
    datastore (`vim.Datastore <vim/Datastore.rst>`_, optional):

       Reference to the datastore managed object where this file is stored. If the file is not located on a datastore, then this reference is null. This is not used for configuration.
    backingObjectId (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Backing object's durable and unmutable identifier. Each backing object has a unique identifier which is not settable.
