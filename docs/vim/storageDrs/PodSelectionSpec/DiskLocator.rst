
vim.storageDrs.PodSelectionSpec.DiskLocator
===========================================
  The disk locator class.
:extends: vmodl.DynamicData_
:since: `vSphere API 5.0 <vim/version.rst#vimversionversion7>`_

Attributes:
    diskId (`int <https://docs.python.org/2/library/stdtypes.html>`_):

       The disk ID.
    diskMoveType (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       The disk move type.
    diskBackingInfo (`vim.vm.device.VirtualDevice.BackingInfo <vim/vm/device/VirtualDevice/BackingInfo.rst>`_, optional):

       The disk backing info.
    profile ([`vim.vm.ProfileSpec <vim/vm/ProfileSpec.rst>`_], optional):

       Virtual Disk Profile requirement. Profiles are solution specific. Profile Based Storage Management is a vSphere server extension. The API users who want to provision VMs using Storage Profiles, need to interact with it. This is an optional parameter and if user doesn't specify profile, the default behavior will apply.
