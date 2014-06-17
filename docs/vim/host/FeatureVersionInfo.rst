.. _str: https://docs.python.org/2/library/stdtypes.html

.. _vSphere API 4.1: ../../vim/version.rst#vimversionversion6

.. _vmodl.DynamicData: ../../vmodl/DynamicData.rst

.. _HostFeatureVersionKey: ../../vim/host/FeatureVersionInfo/FeatureVersionKey.rst


vim.host.FeatureVersionInfo
===========================
  Feature-specific version information for a host
:extends: vmodl.DynamicData_
:since: `vSphere API 4.1`_

Attributes:
    key (`str`_):

       A unique key that identifies a feature, list of possible values are specified in `HostFeatureVersionKey`_ 
    value (`str`_):

       The version string of this feature
