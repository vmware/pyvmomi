.. _str: https://docs.python.org/2/library/stdtypes.html

.. _vSphere API 4.0: ../../vim/version.rst#vimversionversion5

.. _vmodl.DynamicData: ../../vmodl/DynamicData.rst

.. _vim.LicenseManager.LicenseSource: ../../vim/LicenseManager/LicenseSource.rst


vim.host.LicenseSpec
====================
  
:extends: vmodl.DynamicData_
:since: `vSphere API 4.0`_

Attributes:
    source (`vim.LicenseManager.LicenseSource`_, optional):

       License source to be used
    editionKey (`str`_, optional):

       License edition to use
    disabledFeatureKey (`str`_, optional):

       Disabled features. When an edition is set, all the features in it are enabled by default. The following parameter gives a finer control on which features are disabled.
    enabledFeatureKey (`str`_, optional):

       Enabled features
