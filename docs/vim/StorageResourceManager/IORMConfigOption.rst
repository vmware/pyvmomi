.. _enabled: ../../vim/StorageResourceManager/IORMConfigSpec.rst#enabled

.. _vSphere API 4.1: ../../vim/version.rst#vimversionversion6

.. _vmodl.DynamicData: ../../vmodl/DynamicData.rst

.. _congestionThreshold: ../../vim/StorageResourceManager/IORMConfigSpec.rst#congestionThreshold

.. _vim.option.IntOption: ../../vim/option/IntOption.rst

.. _vim.option.BoolOption: ../../vim/option/BoolOption.rst

.. _statsCollectionEnabled: ../../vim/StorageResourceManager/IORMConfigSpec.rst#statsCollectionEnabled


vim.StorageResourceManager.IORMConfigOption
===========================================
  Configuration setting ranges for IORMConfigSpec object.
:extends: vmodl.DynamicData_
:since: `vSphere API 4.1`_

Attributes:
    enabledOption (`vim.option.BoolOption`_):

       enabledOption provides default state value for `enabled`_ 
    congestionThresholdOption (`vim.option.IntOption`_):

       congestionThresholdOption defines value range which can be used for `congestionThreshold`_ 
    statsCollectionEnabledOption (`vim.option.BoolOption`_):

       statsCollectionEnabledOption provides default value for `statsCollectionEnabled`_ 
