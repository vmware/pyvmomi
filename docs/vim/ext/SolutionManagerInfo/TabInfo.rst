.. _str: https://docs.python.org/2/library/stdtypes.html

.. _vSphere API 5.0: ../../../vim/version.rst#vimversionversion7

.. _vmodl.DynamicData: ../../../vmodl/DynamicData.rst


vim.ext.SolutionManagerInfo.TabInfo
===================================
  This data object contains information about a tab to show in the Solution Manager for this extension.
:extends: vmodl.DynamicData_
:since: `vSphere API 5.0`_
**deprecated**


Attributes:
    label (`str`_):

       The name of the tab.
    url (`str`_):

       The URL for the webpage to show in the tab. Extra parameters will be added to this URL when vSphere Client loads it. See the "Customizing the vSphere Client" technical note for more information.
