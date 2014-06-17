.. _bool: https://docs.python.org/2/library/stdtypes.html

.. _vim.vm.Snapshot: ../../vim/vm/Snapshot.rst

.. _vim.vm.ConfigSpec: ../../vim/vm/ConfigSpec.rst

.. _vmodl.DynamicData: ../../vmodl/DynamicData.rst

.. _vim.vm.RelocateSpec: ../../vim/vm/RelocateSpec.rst

.. _snapshotConfigSupported: ../../vim/vm/Capability.rst#snapshotConfigSupported

.. _vim.vm.customization.Specification: ../../vim/vm/customization/Specification.rst

.. _supports cloning from a snapshot point: ../../vim/host/Capability.rst#cloneFromSnapshotSupported


vim.vm.CloneSpec
================
  Specification for a virtual machine cloning operation.
:extends: vmodl.DynamicData_

Attributes:
    location (`vim.vm.RelocateSpec`_):

       A type of RelocateSpec that specifies the location of resources the newly cloned virtual machine will use. The location specifies:
        * A datastore where the virtual machine will be located on physical storage. This is always provided because it indicates where the newly created clone will be copied.
        * a resource pool and optionally a host. The resource pool determines what compute resources will be available to the clone and the host indicates which machine will host the clone.
        * 
    template (`bool`_):

       Specifies whether or not the new virtual machine should be marked as a template.
    config (`vim.vm.ConfigSpec`_, optional):

       An optional specification of changes to the virtual hardware. For example, this can be used to, (but not limited to) reconfigure the networks the virtual switches are hooked up to in the cloned virtual machine.
    customization (`vim.vm.customization.Specification`_, optional):

       An optional guest operating system customization specification. This value is ignored if a template is being created.
    powerOn (`bool`_):

       Specifies whether or not the new VirtualMachine should be powered on after creation. As part of a customization, this flag is normally set to true, since the first power-on operation completes the customization process. This flag is ignored if a template is being created.
    snapshot (`vim.vm.Snapshot`_, optional):

       Snapshot reference from which to base the clone.If this parameter is set, the clone is based off of the snapshot point. This means that the newly created virtual machine will have the same configuration as the virtual machine at the time the snapshot was taken.If this property is not set then the clone is based off of the virtual machine's current configuration.Setting this is only supported if the host this virtual machine is currently residing on `supports cloning from a snapshot point`_ . Such support does not need to exist on the destination host for the clone.Setting this is only supported if the virtual machine supports reporting snapshot configuration information. See `snapshotConfigSupported`_ . Such support does not need to exist on the destination host for the clone.
    memory (`bool`_, optional):

       Flag indicating whether to retain a copy of the source virtual machine's memory state in the clone. Retaining the memory state during clone results in a clone in suspended state with all network adapters removed to avoid network conflicts, except those with a VirtualEthernetCard.addressType of "manual". Users of this flag should take special care so that, when adding a network adapter back to the clone, the VM is not resumed on the same VM network as the source VM, or else MAC address conflicts could occur. When cloning between two hosts with different CPUs outside an EVC cluster, users of this flag should be aware that vCenter does not verify CPU compatibility between the clone's memory state and the target host prior to the clone operation, so the clone may fail to resume until it is migrated to a host with a compatible CPU.This flag is ignored if the snapshot parameter is unset. This flag only applies for a snapshot taken on a running or suspended virtual machine with the 'memory' parameter set to true, because otherwise the snapshot has no memory state. This flag defaults to false.
