.. _int: https://docs.python.org/2/library/stdtypes.html

.. _str: https://docs.python.org/2/library/stdtypes.html

.. _vim.Datastore: ../../../vim/Datastore.rst

.. _target datastore: ../../../vim/vm/RelocateSpec/DiskLocator.rst#datastore

.. _vmodl.DynamicData: ../../../vmodl/DynamicData.rst

.. _vim.vm.ProfileSpec: ../../../vim/vm/ProfileSpec.rst

.. _InvalidDeviceBacking: ../../../vim/fault/InvalidDeviceBacking.rst

.. _deltaDiskBackingsSupported: ../../../vim/host/Capability.rst#deltaDiskBackingsSupported

.. _VirtualDiskFlatVer2BackingInfo: ../../../vim/vm/device/VirtualDisk/FlatVer2BackingInfo.rst

.. _VirtualDiskSeSparseBackingInfo: ../../../vim/vm/device/VirtualDisk/SeSparseBackingInfo.rst

.. _VirtualMachineRelocateDiskMoveOptions: ../../../vim/vm/RelocateSpec/DiskMoveOptions.rst

.. _moveAllDiskBackingsAndDisallowSharing: ../../../vim/vm/RelocateSpec/DiskMoveOptions.rst#moveAllDiskBackingsAndDisallowSharing

.. _vim.vm.device.VirtualDevice.BackingInfo: ../../../vim/vm/device/VirtualDevice/BackingInfo.rst


vim.vm.RelocateSpec.DiskLocator
===============================
  The DiskLocator data object type specifies a virtual disk device (by ID) and a datastore locator for the disk's storage.
:extends: vmodl.DynamicData_

Attributes:
    diskId (`int`_):

       Device ID of the virtual disk.
    datastore (`vim.Datastore`_):

       Target datastore.
    diskMoveType (`str`_, optional):

       Manner in which to move the virtual disk to the `target datastore`_ . The set of possible values is described in `VirtualMachineRelocateDiskMoveOptions`_ .This property can only be set if `deltaDiskBackingsSupported`_ is true.If left unset then `moveAllDiskBackingsAndDisallowSharing`_ is assumed.
    diskBackingInfo (`vim.vm.device.VirtualDevice.BackingInfo`_, optional):

       Backing information for the virtual disk at the destination. This can be used, for instance, to change the format of the virtual disk. If the specified backing is invalid or not supported at the destination, `InvalidDeviceBacking`_ is thrown. Specific property changes may be ignored if they are not supported.Supported BackingInfo types and properties:
        * `VirtualDiskFlatVer2BackingInfo`_
        * 
        * 
        * thinProvisioned
        * eagerlyScrub
        * 
        * `VirtualDiskSeSparseBackingInfo`_
        * (ESX 5.1 or later)
    profile (`vim.vm.ProfileSpec`_, optional):

       Virtual Disk Profile requirement. Profiles are solution specific. Profile Based Storage Management is a vSphere server extension. The API users who want to provision VMs using Storage Profiles, need to interact with it. This is an optional parameter and if user doesn't specify profile, the default behavior will apply.
