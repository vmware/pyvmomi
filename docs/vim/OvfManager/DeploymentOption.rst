
vim.OvfManager.DeploymentOption
===============================
  A deployment option as defined in the OVF specfication.This corresponds to the Configuration element of the DeploymentOptionSection in the specification.
:extends: vmodl.DynamicData_
:since: `vSphere API 4.0 <vim/version.rst#vimversionversion5>`_

Attributes:
    key (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       The key of the deployment option, corresponding to the ovf:id attribute in the OVF descriptor
    label (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       A localized label for the deployment option
    description (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       A localizable description for the deployment option.
