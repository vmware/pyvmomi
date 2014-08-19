
vim.vm.FileLayout.DiskLayout
============================
  Enumerats the set of files for each virtual disk.
:extends: vmodl.DynamicData_

Attributes:
    key (`int <https://docs.python.org/2/library/stdtypes.html>`_):

       Identification of the disk in `config <vim/vm/ConfigInfo.rst>`_ .
    diskFile ([`str <https://docs.python.org/2/library/stdtypes.html>`_]):

       List of files that makes up the virtual disk. At least one entry always exists in this array. The first entry is the main descriptor of the virtual disk (the one used when adding the disk to a virtual machine). These are complete datastore paths, not relative paths.
