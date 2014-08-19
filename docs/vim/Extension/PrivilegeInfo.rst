
vim.Extension.PrivilegeInfo
===========================
  This data object type describes privileges defined by the extension.
:extends: vmodl.DynamicData_
:since: `VI API 2.5 <vim/version.rst#vimversionversion2>`_

Attributes:
    privID (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       The ID of the privilege. The format should begroup name.privilege name. The group name should be the same as the privGroupName property.The privilege name should follow java package naming conventions for uniqueness. The set of characters allowed follow the same rules as `key <vim/Extension.rst#key>`_ .
    privGroupName (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       Hierarchical group name. Each level of the grouping hierarchy is separated by a "." so group names may not include a ".". `privGroupName <vim/AuthorizationManager/Privilege.rst#privGroupName>`_ .
