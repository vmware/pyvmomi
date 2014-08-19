
vim.host.ConnectInfo.LicenseInfo
================================
  This data object type describes license information stored on the host.
:extends: vmodl.DynamicData_
:since: `vSphere API 4.0 <vim/version.rst#vimversionversion5>`_

Attributes:
    license (`vim.LicenseManager.LicenseInfo <vim/LicenseManager/LicenseInfo.rst>`_):

       License information.
    evaluation (`vim.LicenseManager.EvaluationInfo <vim/LicenseManager/EvaluationInfo.rst>`_):

       Evaluation information.
    resource (`vim.LicenseManager.LicensableResourceInfo <vim/LicenseManager/LicensableResourceInfo.rst>`_, optional):

       Licensable resources information.NOTE: The values in this property may not be accurate for pre-5.0 hosts when returned by vCenter 5.0
