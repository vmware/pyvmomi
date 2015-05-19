.. _vSphere API 4.0: ../../vim/version.rst#vimversionversion5

.. _vmodl.DynamicData: ../../vmodl/DynamicData.rst

.. _vim.profile.ParameterMetadata: ../../vim/profile/ParameterMetadata.rst

.. _vim.ExtendedElementDescription: ../../vim/ExtendedElementDescription.rst


vim.profile.ExpressionMetadata
==============================
  DataObject to represent the metadata associated with a SimpleExpression.
:extends: vmodl.DynamicData_
:since: `vSphere API 4.0`_

Attributes:
    expressionId (`vim.ExtendedElementDescription`_):

       Id of the SimpleExpression
    parameter ([`vim.profile.ParameterMetadata`_], optional):

       Parameters that can be specified for this SimpleExpression
