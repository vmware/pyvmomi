
vim.host.SystemResourceInfo
===========================
  The SystemResourceInfo data object describes the configuration of a single system resource group. System resource groups are analogous to `ResourcePool <vim/ResourcePool.rst>`_ objects for virtual machines; however, their structure is fixed and groups may not be created nor destroyed, only configured.
:extends: vmodl.DynamicData_

Attributes:
    key (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       ID of the system resource group.
    config (`vim.ResourceConfigSpec <vim/ResourceConfigSpec.rst>`_, optional):

       Configuration of this system resource group.
    child ([`vim.host.SystemResourceInfo <vim/host/SystemResourceInfo.rst>`_], optional):

       List of child resource groups.
