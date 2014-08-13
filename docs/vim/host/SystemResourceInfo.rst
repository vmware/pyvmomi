.. _str: https://docs.python.org/2/library/stdtypes.html

.. _ResourcePool: ../../vim/ResourcePool.rst

.. _vmodl.DynamicData: ../../vmodl/DynamicData.rst

.. _vim.ResourceConfigSpec: ../../vim/ResourceConfigSpec.rst

.. _vim.host.SystemResourceInfo: ../../vim/host/SystemResourceInfo.rst


vim.host.SystemResourceInfo
===========================
  The SystemResourceInfo data object describes the configuration of a single system resource group. System resource groups are analogous to `ResourcePool`_ objects for virtual machines; however, their structure is fixed and groups may not be created nor destroyed, only configured.
:extends: vmodl.DynamicData_

Attributes:
    key (`str`_):

       ID of the system resource group.
    config (`vim.ResourceConfigSpec`_, optional):

       Configuration of this system resource group.
    child ([`vim.host.SystemResourceInfo`_], optional):

       List of child resource groups.
