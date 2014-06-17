.. _str: https://docs.python.org/2/library/stdtypes.html

.. _vim.Datastore: ../../../../vim/Datastore.rst

.. _VirtualDeviceFileBackingInfo: ../../../../vim/vm/device/VirtualDevice/FileBackingInfo.rst

.. _vim.vm.device.VirtualDevice.BackingInfo: ../../../../vim/vm/device/VirtualDevice/BackingInfo.rst


vim.vm.device.VirtualDevice.FileBackingInfo
===========================================
   `VirtualDeviceFileBackingInfo`_ is a data object type for information about file backing for a device in a virtual machine.
:extends: vim.vm.device.VirtualDevice.BackingInfo_

Attributes:
    fileName (`str`_):

       Filename for the host file used in this backing.
    datastore (`vim.Datastore`_, optional):

       Reference to the datastore managed object where this file is stored. If the file is not located on a datastore, then this reference is null. This is not used for configuration.
    backingObjectId (`str`_, optional):

       Backing object's durable and unmutable identifier. Each backing object has a unique identifier which is not settable.
