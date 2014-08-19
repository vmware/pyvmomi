
vim.host.PhysicalNic.Config
===========================
  The configuration of the physical network adapter containing both the configurable properties and identification information.
:extends: vmodl.DynamicData_

Attributes:
    device (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       PhysicalNic device to which configuration applies.
    spec (`vim.host.PhysicalNic.Specification <vim/host/PhysicalNic/Specification.rst>`_):

       The specification of the physical network adapter.
