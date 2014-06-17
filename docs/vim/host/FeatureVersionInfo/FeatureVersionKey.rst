.. _build: ../../../vim/AboutInfo.rst#build

.. _vim.host.FeatureVersionInfo: ../../../vim/host/FeatureVersionInfo.rst

.. _vim.host.FeatureVersionInfo.FeatureVersionKey: ../../../vim/host/FeatureVersionInfo/FeatureVersionKey.rst

vim.host.FeatureVersionInfo.FeatureVersionKey
=============================================
  Set of possible values for `key`_ , which is a unique key that identifies a feature.
  :contained by: `vim.host.FeatureVersionInfo`_

  :type: `vim.host.FeatureVersionInfo.FeatureVersionKey`_

  :name: faultTolerance

values:
--------

faultTolerance
   VMware Fault Tolerance feature. For pre-4.1 hosts, the version value reported will be empty in which case `build`_ should be used. For all other hosts, the version number reported will be a component-specific version identifier of the form X.Y.Z, where: X refers to host agent Fault Tolerance version number, Y refers to VMX Fault Tolerance version number, Z refers to VMkernal Fault Tolerance version
