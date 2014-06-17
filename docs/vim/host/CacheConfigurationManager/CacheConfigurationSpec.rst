.. _long: https://docs.python.org/2/library/stdtypes.html

.. _freeSpace: ../../../vim/Datastore/Summary.rst#freeSpace

.. _vim.Datastore: ../../../vim/Datastore.rst

.. _vSphere API 5.0: ../../../vim/version.rst#vimversionversion7

.. _vmodl.DynamicData: ../../../vmodl/DynamicData.rst


vim.host.CacheConfigurationManager.CacheConfigurationSpec
=========================================================
  Host cache configuration specification.
:extends: vmodl.DynamicData_
:since: `vSphere API 5.0`_

Attributes:
    datastore (`vim.Datastore`_):

       Datastore used for swap performance enhancement.
    swapSize (`long`_):

       Space to allocate on this datastore to implement swap performance enhancements, in MB. This value should be less or equal to free space capacity on the datastore `freeSpace`_ .
