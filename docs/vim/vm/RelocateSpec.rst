.. _str: https://docs.python.org/2/library/stdtypes.html

.. _VirtualDisk: ../../vim/vm/device/VirtualDisk.rst

.. _diskMoveType: ../../vim/vm/RelocateSpec/DiskLocator.rst#diskMoveType

.. _vim.Datastore: ../../vim/Datastore.rst

.. _vim.HostSystem: ../../vim/HostSystem.rst

.. _target datastore: ../../vim/vm/RelocateSpec.rst#datastore

.. _vim.ResourcePool: ../../vim/ResourcePool.rst

.. _vmodl.DynamicData: ../../vmodl/DynamicData.rst

.. _vim.vm.ProfileSpec: ../../vim/vm/ProfileSpec.rst

.. _VirtualDiskConfigSpec: ../../vim/vm/device/VirtualDiskSpec.rst

.. _deltaDiskBackingsSupported: ../../vim/host/Capability.rst#deltaDiskBackingsSupported

.. _vim.vm.RelocateSpec.DiskLocator: ../../vim/vm/RelocateSpec/DiskLocator.rst

.. _vim.vm.device.VirtualDeviceSpec: ../../vim/vm/device/VirtualDeviceSpec.rst

.. _vim.vm.RelocateSpec.Transformation: ../../vim/vm/RelocateSpec/Transformation.rst

.. _VirtualMachineRelocateTransformation: ../../vim/vm/RelocateSpec/Transformation.rst

.. _moveAllDiskBackingsAndDisallowSharing: ../../vim/vm/RelocateSpec/DiskMoveOptions.rst#moveAllDiskBackingsAndDisallowSharing

.. _VirtualMachineRelocateDiskMoveOptions: ../../vim/vm/RelocateSpec/DiskMoveOptions.rst


vim.vm.RelocateSpec
===================
  Specification for moving or copying a virtual machine to a different datastore or host.
:extends: vmodl.DynamicData_

Attributes:
    datastore (`vim.Datastore`_, optional):

       The datastore where the virtual machine should be located. If not specified, the current datastore is used.
    diskMoveType (`str`_, optional):

       Manner in which to move the virtual disk to the `target datastore`_ . The set of possible values is described in `VirtualMachineRelocateDiskMoveOptions`_ .This property applies to all the disks which the virtual machine has, but can be overridden on a per-disk basis using `diskMoveType`_ . This property can only be set if `deltaDiskBackingsSupported`_ is true.If left unset then `moveAllDiskBackingsAndDisallowSharing`_ is assumed.
    pool (`vim.ResourcePool`_, optional):

       The resource pool to which this virtual machine should be attached. For a relocate or clone operation to a virtual machine, if the argument is not supplied, the current resource pool of virtual machine is used. For a clone operation to a template, this argument is ignored. For a clone operation from a template to a virtual machine, this argument is required.
    host (`vim.HostSystem`_, optional):

       The target host for the virtual machine. If not specified,
        * if resource pool is not specified, current host is used.
        * if resource pool is specified, and the target pool represents a stand-alone host, the host is used.
        * if resource pool is specified, and the target pool represents a DRS-enabled cluster, a host selected by DRS is used.
        * if resource pool is specified and the target pool represents a cluster without DRS enabled, an InvalidArgument exception be thrown.
    disk ([`vim.vm.RelocateSpec.DiskLocator`_], optional):

       An optional list that allows specifying the datastore location for each virtual disk.
    transform (`vim.vm.RelocateSpec.Transformation`_, optional):

       Transformation to perform on the disks. The backend is free to ignore this hint if it is not valid for the current operation. This can be used by clients, for example, to create sparse disks for templates.See `VirtualMachineRelocateTransformation`_ 
    deviceChange ([`vim.vm.device.VirtualDeviceSpec`_], optional):

       An optional list of virtual device specs that allow specifying the migrate options for the relocate operation. The supported device type is `VirtualDisk`_ For VirtualDisk device, `VirtualDiskConfigSpec`_ has to be used to specify migrateCache option for disk with vFlash cache.
    profile ([`vim.vm.ProfileSpec`_], optional):

       Storage profile requirement for Virtual Machine's home directory. Profiles are solution specific. Storage Profile Based Management(SPBM) is a vSphere server extension. The API users who want to provision VMs using Storage Profiles, need to interact with SPBM. This is an optional parameter and if user doesn't specify profile, the default behavior will apply.
