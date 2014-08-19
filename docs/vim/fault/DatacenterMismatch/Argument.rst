
vim.fault.DatacenterMismatch.Argument
=====================================
  An input entity argument that belongs to a mismatched datacenter.
:extends: vmodl.DynamicData_

Attributes:
    entity (`vim.ManagedEntity <vim/ManagedEntity.rst>`_):

       The invalid input entity.
    inputDatacenter (`vim.Datacenter <vim/Datacenter.rst>`_, optional):

       The datacenter for this entity.
