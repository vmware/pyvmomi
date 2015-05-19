.. _vim.Datacenter: ../../../vim/Datacenter.rst

.. _vmodl.DynamicData: ../../../vmodl/DynamicData.rst

.. _vim.ManagedEntity: ../../../vim/ManagedEntity.rst


vim.fault.DatacenterMismatch.Argument
=====================================
  An input entity argument that belongs to a mismatched datacenter.
:extends: vmodl.DynamicData_

Attributes:
    entity (`vim.ManagedEntity`_):

       The invalid input entity.
    inputDatacenter (`vim.Datacenter`_, optional):

       The datacenter for this entity.
