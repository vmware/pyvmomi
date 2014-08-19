
vim.vm.RelocateSpec.DiskLocator
===============================
  The DiskLocator data object type specifies a virtual disk device (by ID) and a datastore locator for the disk's storage.
:extends: vmodl.DynamicData_

Attributes:
    diskId (`int <https://docs.python.org/2/library/stdtypes.html>`_):

       Device ID of the virtual disk.
    datastore (`vim.Datastore <vim/Datastore.rst>`_):

       Target datastore.
    diskMoveType (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Manner in which to move the virtual disk to the `target datastore <vim/vm/RelocateSpec/DiskLocator.rst#datastore>`_ . The set of possible values is described in `VirtualMachineRelocateDiskMoveOptions <vim/vm/RelocateSpec/DiskMoveOptions.rst>`_ .This property can only be set if `deltaDiskBackingsSupported <vim/host/Capability.rst#deltaDiskBackingsSupported>`_ is true.If left unset then `moveAllDiskBackingsAndDisallowSharing <vim/vm/RelocateSpec/DiskMoveOptions.rst#moveAllDiskBackingsAndDisallowSharing>`_ is assumed.
    diskBackingInfo (`vim.vm.device.VirtualDevice.BackingInfo <vim/vm/device/VirtualDevice/BackingInfo.rst>`_, optional):

       Backing information for the virtual disk at the destination. This can be used, for instance, to change the format of the virtual disk. If the specified backing is invalid or not supported at the destination, `InvalidDeviceBacking <vim/fault/InvalidDeviceBacking.rst>`_ is thrown. Specific property changes may be ignored if they are not supported.Supported BackingInfo types and properties:
        * `VirtualDiskFlatVer2BackingInfo <vim/vm/device/VirtualDisk/FlatVer2BackingInfo.rst>`_
        * 
        * 
        * thinProvisioned
        * eagerlyScrub
        * 
        * `VirtualDiskSeSparseBackingInfo <vim/vm/device/VirtualDisk/SeSparseBackingInfo.rst>`_
        * (ESX 5.1 or later)
    profile ([`vim.vm.ProfileSpec <vim/vm/ProfileSpec.rst>`_], optional):

       Virtual Disk Profile requirement. Profiles are solution specific. Profile Based Storage Management is a vSphere server extension. The API users who want to provision VMs using Storage Profiles, need to interact with it. This is an optional parameter and if user doesn't specify profile, the default behavior will apply.
