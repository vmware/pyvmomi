.. _str: https://docs.python.org/2/library/stdtypes.html

.. _vSphere API 4.0: ../../../vim/version.rst#vimversionversion5

.. _vmodl.DynamicData: ../../../vmodl/DynamicData.rst

.. _vmodl.LocalizableMessage: ../../../vmodl/LocalizableMessage.rst


vim.profile.ComplianceResult.ComplianceFailure
==============================================
  
:extends: vmodl.DynamicData_
:since: `vSphere API 4.0`_

Attributes:
    failureType (`str`_):

       String uniquely identifying the failure.
    message (`vmodl.LocalizableMessage`_):

       Message which describes the compliance failures message.key serves as a key to the localized message catalog.
    expressionName (`str`_, optional):

       Name of the Expression which generated the ComplianceFailure
