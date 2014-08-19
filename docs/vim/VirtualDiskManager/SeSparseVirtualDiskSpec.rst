
vim.VirtualDiskManager.SeSparseVirtualDiskSpec
==============================================
  Specification used to create an Flex-SE based virtual disk
:extends: vim.VirtualDiskManager.FileBackedVirtualDiskSpec_
:since: `vSphere API 5.1 <vim/version.rst#vimversionversion8>`_

Attributes:
    grainSizeKb (`int <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       The grain size in kB for Flex-SE disk types. Default value will be used if unset.
