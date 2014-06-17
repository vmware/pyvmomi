.. _long: https://docs.python.org/2/library/stdtypes.html

.. _VI API 2.5: ../../vim/version.rst#vimversionversion2

.. _vim.vm.ProfileSpec: ../../vim/vm/ProfileSpec.rst

.. _vim.VirtualDiskManager.VirtualDiskSpec: ../../vim/VirtualDiskManager/VirtualDiskSpec.rst


vim.VirtualDiskManager.FileBackedVirtualDiskSpec
================================================
  Specification used to create a file based virtual disk
:extends: vim.VirtualDiskManager.VirtualDiskSpec_
:since: `VI API 2.5`_

Attributes:
    capacityKb (`long`_):

       Specify the capacity of the virtual disk in Kb.
    profile (`vim.vm.ProfileSpec`_, optional):

       Virtual Disk Profile requirement. Profiles are solution specifics. Profile Based Storage Management is a vSphere server extension. The API users who want to provision VMs using Storage Profiles, need to interact with it. This is an optional parameter and if user doesn't specify profile, the default behavior will apply.
