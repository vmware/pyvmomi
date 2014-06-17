.. _VirtualDevice: ../../../vim/vm/device/VirtualDevice.rst

.. _vmodl.DynamicData: ../../../vmodl/DynamicData.rst

.. _vim.vm.ProfileSpec: ../../../vim/vm/ProfileSpec.rst

.. _vim.vm.device.VirtualDevice: ../../../vim/vm/device/VirtualDevice.rst

.. _vim.vm.device.VirtualDeviceSpec.Operation: ../../../vim/vm/device/VirtualDeviceSpec/Operation.rst

.. _vim.vm.device.VirtualDeviceSpec.FileOperation: ../../../vim/vm/device/VirtualDeviceSpec/FileOperation.rst


vim.vm.device.VirtualDeviceSpec
===============================
  The VirtualDeviceSpec data object type encapsulates change specifications for an individual virtual device. The virtual device being added or modified must be fully specified.
:extends: vmodl.DynamicData_

Attributes:
    operation (`vim.vm.device.VirtualDeviceSpec.Operation`_, optional):

       Type of operation being performed on the specified virtual device. If no operation is specified, the spec. is ignored.
    fileOperation (`vim.vm.device.VirtualDeviceSpec.FileOperation`_, optional):

       Type of operation being performed on the backing of the specified virtual device. If no file operation is specified in the VirtualDeviceSpec, then any backing filenames in the `VirtualDevice`_ must refer to files that already exist. The "replace" and "delete" values for this property are only applicable to virtual disk backing files.
    device (`vim.vm.device.VirtualDevice`_):

       Device specification, with all necessary properties set.
    profile (`vim.vm.ProfileSpec`_, optional):

       Virtual Device Profile requirement. Profiles are solution specifics. Storage Profile Based Management(SPBM) is a vSphere server extension. The API users who want to provision VMs using Storage Profiles, need to interact with SPBM service. This is an optional parameter and if user doesn't specify profile, the default behavior will apply.
