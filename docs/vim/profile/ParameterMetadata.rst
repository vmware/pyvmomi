
vim.profile.ParameterMetadata
=============================
  The `ProfileParameterMetadata <vim/profile/ParameterMetadata.rst>`_ data object represents the metadata information for expressions, policy options, and host-specific configuration data.
:extends: vmodl.DynamicData_
:since: `vSphere API 4.0 <vim/version.rst#vimversionversion5>`_

Attributes:
    id (`vim.ExtendedElementDescription <vim/ExtendedElementDescription.rst>`_):

       Identifier for the parameter.
    type (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       Type of the parameter.
    optional (`bool <https://docs.python.org/2/library/stdtypes.html>`_):

       Whether the parameter is optional.
    defaultValue (`object <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Default value that can be used for the parameter.
