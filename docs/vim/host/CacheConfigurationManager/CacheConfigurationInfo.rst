.. _long: https://docs.python.org/2/library/stdtypes.html

.. _vim.Datastore: ../../../vim/Datastore.rst

.. _vSphere API 5.0: ../../../vim/version.rst#vimversionversion7

.. _vmodl.DynamicData: ../../../vmodl/DynamicData.rst


vim.host.CacheConfigurationManager.CacheConfigurationInfo
=========================================================
  Host solid state drive cache configuration information.
:extends: vmodl.DynamicData_
:since: `vSphere API 5.0`_

Attributes:
    key (`vim.Datastore`_):

       Datastore used for swap performance enhancements.
    swapSize (`long`_):

       Space allocated on this datastore to implement swap performance enhancements, in MB.
