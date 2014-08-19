
vim.host.FeatureVersionInfo
===========================
  Feature-specific version information for a host
:extends: vmodl.DynamicData_
:since: `vSphere API 4.1 <vim/version.rst#vimversionversion6>`_

Attributes:
    key (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       A unique key that identifies a feature, list of possible values are specified in `HostFeatureVersionKey <vim/host/FeatureVersionInfo/FeatureVersionKey.rst>`_ 
    value (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       The version string of this feature
