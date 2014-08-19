
vim.profile.ComplianceResult.ComplianceFailure
==============================================
  
:extends: vmodl.DynamicData_
:since: `vSphere API 4.0 <vim/version.rst#vimversionversion5>`_

Attributes:
    failureType (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       String uniquely identifying the failure.
    message (`vmodl.LocalizableMessage <vmodl/LocalizableMessage.rst>`_):

       Message which describes the compliance failures message.key serves as a key to the localized message catalog.
    expressionName (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Name of the Expression which generated the ComplianceFailure
