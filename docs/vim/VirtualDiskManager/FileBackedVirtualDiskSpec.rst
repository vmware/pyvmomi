
vim.VirtualDiskManager.FileBackedVirtualDiskSpec
================================================
  Specification used to create a file based virtual disk
:extends: vim.VirtualDiskManager.VirtualDiskSpec_
:since: `VI API 2.5 <vim/version.rst#vimversionversion2>`_

Attributes:
    capacityKb (`long <https://docs.python.org/2/library/stdtypes.html>`_):

       Specify the capacity of the virtual disk in Kb.
    profile ([`vim.vm.ProfileSpec <vim/vm/ProfileSpec.rst>`_], optional):

       Virtual Disk Profile requirement. Profiles are solution specifics. Profile Based Storage Management is a vSphere server extension. The API users who want to provision VMs using Storage Profiles, need to interact with it. This is an optional parameter and if user doesn't specify profile, the default behavior will apply.
