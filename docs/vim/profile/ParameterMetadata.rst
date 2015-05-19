.. _str: https://docs.python.org/2/library/stdtypes.html

.. _bool: https://docs.python.org/2/library/stdtypes.html

.. _object: https://docs.python.org/2/library/stdtypes.html

.. _vSphere API 4.0: ../../vim/version.rst#vimversionversion5

.. _vmodl.DynamicData: ../../vmodl/DynamicData.rst

.. _ProfileParameterMetadata: ../../vim/profile/ParameterMetadata.rst

.. _vim.ExtendedElementDescription: ../../vim/ExtendedElementDescription.rst


vim.profile.ParameterMetadata
=============================
  The `ProfileParameterMetadata`_ data object represents the metadata information for expressions, policy options, and host-specific configuration data.
:extends: vmodl.DynamicData_
:since: `vSphere API 4.0`_

Attributes:
    id (`vim.ExtendedElementDescription`_):

       Identifier for the parameter.
    type (`str`_):

       Type of the parameter.
    optional (`bool`_):

       Whether the parameter is optional.
    defaultValue (`object`_, optional):

       Default value that can be used for the parameter.
