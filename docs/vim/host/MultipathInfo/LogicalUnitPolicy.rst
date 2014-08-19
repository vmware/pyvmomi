
vim.host.MultipathInfo.LogicalUnitPolicy
========================================
  The `HostMultipathInfoLogicalUnitPolicy <vim/host/MultipathInfo/LogicalUnitPolicy.rst>`_ data object describes a path selection policy for a device. This policy determines how paths should be utilized when accessing a device.
:extends: vmodl.DynamicData_

Attributes:
    policy (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       String representing the path selection policy for a device. Use one of the following strings:
        * VMW_PSP_FIXED
        * - Use a preferred path whenever possible.
        * VMW_PSP_RR
        * - Load balance.
        * VMW_PSP_MRU
        * - Use the most recently used path.
        * You can also use the
        * `QueryPathSelectionPolicyOptions <vim/host/StorageSystem.rst#queryPathSelectionPolicyOptions>`_
        * method to retrieve the set of valid strings. Use the key from the resulting structure
        * `HostPathSelectionPolicyOption <vim/host/PathSelectionPolicyOption.rst>`_
        * .
