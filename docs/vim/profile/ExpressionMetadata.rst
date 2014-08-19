
vim.profile.ExpressionMetadata
==============================
  DataObject to represent the metadata associated with a SimpleExpression.
:extends: vmodl.DynamicData_
:since: `vSphere API 4.0 <vim/version.rst#vimversionversion5>`_

Attributes:
    expressionId (`vim.ExtendedElementDescription <vim/ExtendedElementDescription.rst>`_):

       Id of the SimpleExpression
    parameter ([`vim.profile.ParameterMetadata <vim/profile/ParameterMetadata.rst>`_], optional):

       Parameters that can be specified for this SimpleExpression
