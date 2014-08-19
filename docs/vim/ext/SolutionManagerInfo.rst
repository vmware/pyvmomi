
vim.ext.SolutionManagerInfo
===========================
  This data object encapsulates the Solution Manager configuration for this extension.
:extends: vmodl.DynamicData_
:since: `vSphere API 5.0 <vim/version.rst#vimversionversion7>`_

Attributes:
    tab ([`vim.ext.SolutionManagerInfo.TabInfo <vim/ext/SolutionManagerInfo/TabInfo.rst>`_], optional):

       List of tabs that must be shown in the Solution Manager for this extension. Tabs are shown ordered by their position in this array.
    smallIconUrl (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       URL for an icon for this extension. The icon will be shown in the Solution Manager for this extension. The icon must be 16x16, and should be in PNG format.
